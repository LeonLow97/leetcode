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
	filePath      = "links.csv"
	noOfQuestions = 5
	timeLayout    = time.RFC3339
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
			q.LastAccessed = time.Now().UTC()
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

func main() {
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
	now := time.Now().UTC()
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
