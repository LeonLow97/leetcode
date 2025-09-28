// Creating Queues using Arrays (Easy Way)

// 1st method
var q = []
q.push("FIRST")
q.push("SECOND")
q.push("THIRD")

// remove from the beginning with shift (re-index - bad)
q.shift()  // FIRST
q.shift()  // SECOND
q.shift()  // THIRD

// 2nd method
var q = []
q.unshift("FIRST")
q.unshift("SECOND")
q.unshift("THIRD")

q.pop()  // FIRST
q.pop()  // SECOND
q.pop()  // THIRD
