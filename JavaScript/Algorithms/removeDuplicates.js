// Input: nums = [0,0,1,1,1,2,2,3,3,4]
// Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
function removeDuplicates (arr) {
  let pointer = 0
  let newArr = []
  newArr.push(arr[0])
  for (let i = 1; i < arr.length; i++){
    // console.log(newArr[pointer] +","+arr[i])
    if (newArr[pointer] !== arr[i]) {
      pointer++
      newArr[pointer] = arr[i]
      // console.log(newArr)
    } 
    // else {
    //   console.log('same')
    // }
  }
  console.log(newArr)
}

function removeDuplicatesInPlace (arr) {
  let pointer = 0
  for (let i = 1; i < arr.length; i++){

    if (arr[pointer] !== arr[i]) {
      pointer++
      arr[pointer] = arr[i]
      console.log(arr)
    } 
    else {
      console.log('same')
    }
  }
  console.log(arr)
}


const arr = [1,1,2,2,2,3,4,6,6,7]

const output = removeDuplicatesInPlace(arr)
console.log(output)