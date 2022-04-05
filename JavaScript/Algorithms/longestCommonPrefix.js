// just looking at prefix (beginning of word), 
// take shortest string as the length, and check 
// each other words until 1 doesnt match.

function longestCommonPrefix (str) {
  let prefix = ''
  // let shortestWord = {
  //   length: 999,
  //   index: 0
  // }
  // str.forEach((s,index) => {
  //   if (s.length < shortestWord.length) {
  //     shortestWord.length = s.length;
  //     shortestWord.index = index
  //   }
  // })
  // console.log(shortestWord)
  let firstWord = 0
  for (let letter = 0; letter < str[firstWord].length; letter++ ){ // "flower -> 6 length"
    for (let word = 1; word < str.length; word++) {
      if (str[firstWord][letter] !== str[word][letter]) return prefix
    }
    prefix += str[firstWord][letter]
  }

}


const str = ["flower", "flow", "flight"] // "fl"

const output = longestCommonPrefix(str)
console.log(output)