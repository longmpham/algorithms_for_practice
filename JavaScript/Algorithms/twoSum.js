// using memo: take the compliment and add it to a memo map. 
// this map will contain all the compliments of each element
// when going through the array, if the compliment exists,
// there is a sum. If its not in the array, add the compliment
// in the memo map and go next. 

// this is a one pass therefore it is O(n) time complexity.
// Since there is only 1 map required, it is O(n) space complexity



function twoSum (nums, target) {
  const seen = {}
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i]
    let compliment = target - num
    if (compliment in seen) {
      // return the index of the array given
      return [seen[compliment], i]

      // return the values found from the array given
      // return `num1: ${compliment}, num2: ${num}`
    }
    else {
      seen[num] = i
    }
  }
}


const nums = [1,2,3,4,5]
const target = 5
const output = twoSum(nums, target)
console.log(output)