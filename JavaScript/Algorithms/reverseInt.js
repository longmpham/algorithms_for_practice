// logic: turn it into a str and reverse it that way
function reverseInt(int) {
  const strArr = int.toString()
  const revString = strArr.split('').reverse().join('')
  const revInt = parseInt(revString)
  // return int > 0 ? revInt : revInt * (-1)
  return revInt * Math.sign(int)
}



const output = reverseInt(-10023)
console.log(output)