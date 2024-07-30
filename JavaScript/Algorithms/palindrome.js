// logic: reverse the string and check if the reversed string is the same as the original string.
function palindrome(str) {
  revString = str.split('').reverse().join('')
  return (str === revString)
}

// logic: using a for loop, use 2 pointers to check the front and back. If they are the same, return true, else return false
function palindrome1(str) {
  strArr = str.split('')

  for (let i = 0; i < strArr.length/2; i++) {
    if (strArr[i] !== strArr[strArr.length - 1 - i]) return false
  }
  return true;
}


str = "1001"
str = "racecar"
str = "10101"
const output = palindrome1("1001")
console.log(output)