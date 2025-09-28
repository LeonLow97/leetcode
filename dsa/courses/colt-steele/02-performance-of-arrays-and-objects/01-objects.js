let instructor = {
    firstName: "Leon",
    isHuman: true,
    favouriteNumbers: [1,2,3,4]
}

console.log(Object.keys(instructor), "\n")
console.log(Object.values(instructor), "\n")
console.log(Object.entries(instructor), "\n")

console.log(instructor.hasOwnProperty("firstName"))
