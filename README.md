# Random Leetcode Questions Generator

This Go program helps you regularly review a set of question links saved in a CSV file (links.csv). Each entry has a type, a URL, and the last time you opened it. The program picks the questions you haven’t looked at in a while, randomly selects up to five from that group, and opens them in your browser (using Chrome by default). After opening, it updates their "last accessed" time so the next run can prioritize different ones. It’s a handy way to rotate through study or reference materials without repeating the same links too often.
