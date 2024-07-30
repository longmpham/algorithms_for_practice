// given a string "123 456 789", take the sum of each digit
// and multiple every even digit by 2. if there is an overflow
// (ie. 8x2 = 16), take each number and add them together 
// (ie. 16 => 1 + 6 = 7) and finally divide the sum by 10


function checkSIN(sin) {

  let splitString = sin.split(" ")
  newArr = splitString.join("")
  console.log(newArr)
  let sum = 0

  for (let i = 0; i < newArr.length; i++) {
    if(i % 2 === 1) {
      sum += parseInt(newArr[i])
    } else {
      let num2x = parseInt(newArr[i]) * 2
      if(num2x > 10) {
        num2x = num2x - 9
      }
      sum += num2x
    }
  }
  console.log(sum/10)
  // return Number.isInteger(sum/10)
  return (sum/10 % 1 === 0)
}

// const sin = "123 456 789" // false
const sin = "046 454 286" // true
const output = checkSIN(sin)
console.log(output)