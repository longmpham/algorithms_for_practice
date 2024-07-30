function quickSort(array) {

  if (array.length <= 1) {
    return array
  }

  // create a pivot
  const pivot = array[array.length -1]
  // console.log(array, pivot)
  const smallerArray = []
  const equalArray = [pivot]
  const largerArray = []

  for (let i = 0; i < array.length -1; i++) {
    if (array[i] < pivot) {
      smallerArray.push(array[i])
    } else if (array[i] > pivot) {
      largerArray.push(array[i])
    }
    else {
      equalArray.push(array[i])
    }
  }
  return [...quickSort(smallerArray), ...equalArray, ...quickSort(largerArray)]
}

const array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
const output = quickSort(array)
console.log(output)