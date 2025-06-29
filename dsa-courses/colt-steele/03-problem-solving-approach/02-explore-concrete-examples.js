// Write a function which takes in a string
// and returns counts of each character in the string

charCount("aaaa"); // {a:4}
charCount("hello") // {h:1, e:1, l:2, o:1}

// More complex examples
"my phone number is 182763" // accounts for spaces? put numbers?
"Hello hi" // do we ignore casing? do we store uppercase H or lowercase h?

// Empty inputs
charCount("") // what do we return? error? empty object {}?

// Invalid inputs
charCount(null)