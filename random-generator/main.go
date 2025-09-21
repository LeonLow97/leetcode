package main

const (
	filePath      = ALL
	noOfQuestions = 5
)

func main() {
	generate()

	questions, _ := readQuestions()
	_ = updateQuestionsMarkdown(questions, "README.md")
}

const (
	ALL = "links.csv"

	SHOPEE = "./company/shopee.csv"
)
