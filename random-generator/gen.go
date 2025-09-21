package main

import (
	"encoding/csv"
	"fmt"
	"math/rand"
	"os"
	"os/exec"
	"runtime"
	"sort"
	"time"
)

type Question struct {
	Type         string
	Link         string
	LastAccessed time.Time
}

const (
	timeLayout = time.RFC3339
)

func readQuestions() ([]Question, error) {
	f, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	reader := csv.NewReader(f)
	rows, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	var questions []Question
	for i, row := range rows {
		if i == 0 {
			continue // skip header
		}
		if len(row) < 2 {
			continue // invalid row
		}
		qType := row[0]
		link := row[1]

		var t time.Time
		if len(row) >= 3 && row[2] != "" {
			t, err = time.Parse(timeLayout, row[2])
			if err != nil {
				t = time.Time{}
			}
		} else {
			t = time.Time{}
		}

		questions = append(questions, Question{
			Type:         qType,
			Link:         link,
			LastAccessed: t,
		})
	}
	return questions, nil
}

func writeQuestions(questions []Question) error {
	f, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer f.Close()

	writer := csv.NewWriter(f)
	defer writer.Flush()

	writer.Write([]string{"type", "link", "last_accessed"})

	for _, q := range questions {
		if q.LastAccessed.IsZero() {
			fmt.Printf("Filling missing timestamp for: %s\n", q.Link)
			loc, _ := time.LoadLocation("Asia/Singapore")
			q.LastAccessed = time.Now().In(loc)
		}
		writer.Write([]string{q.Type, q.Link, q.LastAccessed.Format(timeLayout)})
	}
	return nil
}

func openURL(url string) error {
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "windows":
		cmd = exec.Command("rundll32", "url.dll,FileProtocolHandler", url)
	case "darwin":
		cmd = exec.Command("open", "-a", "Google Chrome", url)
	default: // Linux
		cmd = exec.Command("google-chrome", url)
	}
	return cmd.Start()
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func generate() {
	questions, err := readQuestions()
	if err != nil {
		fmt.Printf("Error reading CSV: %v\n", err)
		return
	}

	if len(questions) == 0 {
		fmt.Println("No questions found in the CSV.")
		return
	}

	// Make a copy of the questions slice for sorting
	sorted := append([]Question(nil), questions...)

	// Sort the copy by oldest last accessed
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].LastAccessed.Before(sorted[j].LastAccessed)
	})

	// Select candidates from the sorted list
	cutoff := min(noOfQuestions*2, len(sorted))
	candidates := sorted[:cutoff]
	rand.Shuffle(len(candidates), func(i, j int) {
		candidates[i], candidates[j] = candidates[j], candidates[i]
	})
	selected := candidates[:min(noOfQuestions, len(candidates))]

	fmt.Printf("Opening %d links:\n", len(selected))
	loc, _ := time.LoadLocation("Asia/Singapore")
	now := time.Now().In(loc)
	opened := map[string]bool{}

	for _, q := range selected {
		fmt.Printf(" - [%s] %s\n", q.Type, q.Link)
		err := openURL(q.Link)
		if err != nil {
			fmt.Printf("Failed to open: %s, Error: %v\n", q.Link, err)
		}
		opened[q.Link] = true
	}

	// Update timestamps
	for i := range questions {
		if opened[questions[i].Link] {
			questions[i].LastAccessed = now
		}
	}

	err = writeQuestions(questions)
	if err != nil {
		fmt.Printf("Error writing CSV: %v\n", err)
	}
}

func updateQuestionsMarkdown(questions []Question, readmePath string) error {
	// Read the existing README.md
	content, err := os.ReadFile(readmePath)
	if err != nil {
		return err
	}

	// Remove all previous tables (## <type> ... table) using a regex
	// We'll keep everything before the first table, then add new tables
	lines := string(content)
	var header string
	idx := 0
	for i, line := range splitLines(lines) {
		if len(line) > 2 && line[:2] == "##" {
			idx = i
			break
		}
	}
	if idx > 0 {
		header = joinLines(splitLines(lines)[:idx])
	} else {
		header = lines
	}

	// Group questions by type
	grouped := make(map[string][]Question)
	for _, q := range questions {
		grouped[q.Type] = append(grouped[q.Type], q)
	}

	// Get sorted type order for consistent output
	typeOrder := make([]string, 0, len(grouped))
	for t := range grouped {
		typeOrder = append(typeOrder, t)
	}
	sort.Strings(typeOrder)

	// Build summary table
	summary := "\n| Type | No Of Question |\n|------|----------------|\n"
	total := 0
	for _, t := range typeOrder {
		count := len(grouped[t])
		summary += fmt.Sprintf("| %s | %d |\n", t, count)
		total += count
	}
	summary += fmt.Sprintf("| **Total** | **%d** |\n", total)

	// Build new tables
	var tables string
	for _, qType := range typeOrder {
		tables += fmt.Sprintf("\n## %s\n\n", qType)
		tables += "| S/N | Link | Last Accessed |\n|-----|------|---------------|\n"
		for i, q := range grouped[qType] {
			name := q.Link
			if idx := lastIndex(q.Link, "/"); idx != -1 && idx+1 < len(q.Link) {
				name = q.Link[idx+1:]
				if name == "" && idx > 0 {
					link := q.Link[:idx]
					idx2 := lastIndex(link, "/")
					if idx2 != -1 && idx2+1 < len(link) {
						name = link[idx2+1:]
					}
				}
			}
			loc, _ := time.LoadLocation("Asia/Singapore")
			formattedTime := q.LastAccessed.In(loc).Format("02 January 2006, 3.04 PM")
			row := fmt.Sprintf("| %d | [%s](%s) | %s |\n", i+1, name, q.Link, formattedTime)
			tables += row
		}
	}

	// Write back to README.md
	newContent := header + summary + tables
	return os.WriteFile(readmePath, []byte(newContent), 0644)
}

// Helper to split lines
func splitLines(s string) []string {
	var out []string
	start := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '\n' {
			out = append(out, s[start:i])
			start = i + 1
		}
	}
	if start < len(s) {
		out = append(out, s[start:])
	}
	return out
}

// Helper to join lines
func joinLines(lines []string) string {
	if len(lines) == 0 {
		return ""
	}
	out := lines[0]
	for i := 1; i < len(lines); i++ {
		out += "\n" + lines[i]
	}
	return out
}

// Returns the last index of sep in s, or -1 if not found
func lastIndex(s string, sep string) int {
	for i := len(s) - len(sep); i >= 0; i-- {
		if s[i:i+len(sep)] == sep {
			return i
		}
	}
	return -1
}
