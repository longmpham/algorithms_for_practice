function capitalizeFirstLetters1(str) {
  const splitString = str.split(' ');

  for (let i = 0; i < splitString.length; i++) {
    splitString[i] = splitString[i].substring(0,1).toUpperCase() + splitString[i].substring(1)
  }
  const joinString = splitString.join(' ')
  return joinString;
}

function capitalizeFirstLetters2(str) {
  const splitString = str.split(' ');

  let newArr = []
  splitString.map(word => {
    newArr.push(word[0].toUpperCase() + word.substring(1))
  });


  newArr = newArr.join(' ')
  return newArr;
}


const output = capitalizeFirstLetters2('hello world my name is long');
console.log(output);
