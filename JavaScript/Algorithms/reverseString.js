// Method 1: using the Array.join method and Array.reverse method
function reverseString1(str) {
  // const stringArray = str.split('').reverse().join('')

  const strArr = str.split('');
  revStr = strArr.reverse();
  joinStr = revStr.join('');

  // return stringArray
  return joinStr;
}

function reverseString2(str) {
  const strArr = str.split('')
  let revStr = ''
  for (let i = 0; i < strArr.length; i++ ) {
    revStr = strArr[i] + revStr
  }
  return revStr
}

function reverseString3(str) {
  const strArr = str.split('')
  let revStr = ''
  for (let i = strArr.length - 1; i >= 0; i--) {
    revStr = revStr + strArr[i]
  }
  return revStr
}

function reverseString4(str) {
  let revString = ''
  for(let char of str) {
    revString = char + revString
  }
  return revString
}

function reverseString5(str) {
  let revString = ''
  strArr = str.split('').forEach(char => {
    revString = char + revString
  });
  return revString
}

const output = reverseString5("hello world");
console.log(output);
