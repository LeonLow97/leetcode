package main

const (
	filePath      = ALL
	noOfQuestions = 5
)

func main() {
	generate()

	questions, _ := readQuestions()

	if filePath == ALL {
		_ = updateQuestionsMarkdown(questions, "README.md")
		_ = updateQuestionsMarkdown(questions, "../README.md")
	}
}

const (
	ALL = "links.csv"

	SHOPEE = "./company/shopee.csv"
	JANESTREET = "./company/janestreet.csv"
)
