/*
    Function that prints all numbers from 1 to 100. For every multiple of 3,
    print Fizz, and every multiple of 5, print Buzz. If number is multiple of 
    3 and 5, print FizzBuzz
*/

function fizzBuzz() {
  const fizz = "Fizz";
  const buzz = "Buzz";

  for (let i = 1; i <= 100; i++) {
    let str = ""
    if(i%3 === 0) {
      str += fizz
    }
    if(i%5 === 0) {
      str += buzz
    }
    if(str === "") {
      str = i
    }
    console.log(str)
  }
}

const output = fizzBuzz()