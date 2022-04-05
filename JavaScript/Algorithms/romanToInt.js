// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

function romanToInt(str) {
  // create a dict 
  const romanNumerals = {
    I:1,
    V:5,
    X:10,
    L:50,
    C:100,
    D:500,
    M:1000
  }

  let total = 0

  // check if current number is less than the next number 
  for (let i = 0; i < str.length; i++) {
    // add a subtraction and skip the next letter (takes 2 letters)
    if(romanNumerals[str[i]] < romanNumerals[str[i+1]]) {
      total += romanNumerals[str[i+1]] - romanNumerals[str[i]]
      i++
    } else {
      // add an addition!
      total += romanNumerals[str[i]]
    }
    console.log(total)
  }

  return total


}

const str = 'MCMXCIV' // 1994
const str2 = 'LVIII' // 58
const output = romanToInt(str)
console.log(output)