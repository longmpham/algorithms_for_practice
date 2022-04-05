function parenthesisIsValid(str) {

  if (str.length % 2 === 1) return false
  if (str.length === 0) return false

  const openBrackets = ["(","[","{"]
  // const closeBrackets = [")","]","}"]
  // console.log(str)
  let stack = []

  // strArr = str.split('')

  for (char of str) {
    if (openBrackets.includes(char)) {
      stack.push(char)
      // console.log(stack)
    }
    else {
      // its a closing bracket...
      // console.log(`compliment bracker: ${char}`)
      if (char === ")") {
        if (stack[stack.length-1] !== "(") return false
        stack.pop()
      } else if (char === "]") {
        if (stack[stack.length-1] !== "[") return false
        stack.pop()
      } else {
        // char === "}"
        if (stack[stack.length-1] !== "{") return false
        stack.pop()
      }
      // console.log(`the stack: ${stack}`)
    }
  }

  if (stack.length !== 0) return false
  return true;

}


function parenthesisIsValid2 (str) {
  const bracketMap = {
    ")":"(",
    "}":"{",
    "]":"[",
  }

  let stack = []
  strArr = str.split('')

  for (char of strArr) {
    // console.log(char)
    if (char === "(" || char === "{" || char === "[") {
      stack.push(char)
    } else {
      if (stack[stack.length -1] === bracketMap[char]) {
        stack.pop()
      } else {
        return false
      }
    }
    // stack.length === 0 ? console.log("empty") : console.log(stack)
  }
  return (stack.length === 0 ? true : false)

}

str = "[]()[()]"
// str = "[)"
// str = "[[[]]]"
const output = parenthesisIsValid2(str)
console.log(output)