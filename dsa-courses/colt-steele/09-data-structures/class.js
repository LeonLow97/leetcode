class Student {
  // "this" refers to the individual instance
  constructor(firstName, lastName, year) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.year = year;
    this.lateCount = 0;
    this.scores = []
  }

  fullName() {
    // console.log(this)
    return `Your full name is ${this.firstName} ${this.lastName}`;
  }
  markLate() {
    this.lateCount += 1;
    if (this.lateCount >= 3) {
        return "You are expelled!"
    }
    return `${this.firstName} ${this.lastName} has been late ${this.lateCount} times.`;
  }
  addScore(score) {
    this.scores.push(score)
    return this.scores
  }
  calculateAverage() {
    let sum = this.scores.reduce(function(a, b) {return a + b})
    return sum / this.scores.length
  }

  static EnrollStudents() {
    // maybe send an email here
    return "ENROLLING STUDENTS..."
  }
}

// Instantiate objects from a Class
let firstStudent = new Student("Colt", "Steele", 2018);
let secondStudent = new Student("Leon", "Low", 2022);

// console.log(firstStudent.firstName, firstStudent.lastName);

// console.log(secondStudent.year);
// secondStudent.year = 1997;
// console.log(secondStudent.year);

// console.log(secondStudent.fullName());

// console.log(secondStudent.markLate())
// console.log(secondStudent.markLate())
// console.log(secondStudent.markLate())

// console.log(secondStudent.scores)
// console.log(secondStudent.addScore(82))
// console.log(secondStudent.addScore(58))
// console.log(secondStudent.addScore(57))
// console.log(secondStudent.scores)

// console.log(secondStudent.calculateAverage())

// console.log(firstStudent.EnrollStudents()) // error: not relevant to an individual instance of the class
console.log(Student.EnrollStudents())




