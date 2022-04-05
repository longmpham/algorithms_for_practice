// Last in First Out LIFO
class Stack {
  constructor() {
    this.s1 = []
  }

  // add item on top of stack
  stackPush(value) {
    this.s1.push(value)
  }

  // returns top of stack
  stackPop() {
    if(this.s1 === 0) {
      return "nothing there"
    }
    this.s1.pop()
  }

  stackPeek() {
    if(this.s1 === 0) {
      return "nothing there"
    }
    return this.s1[this.s1.length -1]
  }

  size() {
    if(this.s1 === 0) {
      return 0
    }
    return this.s1.length
  }
}


let myStack = new Stack()
console.log(myStack.size())
myStack.stackPush(1)
myStack.stackPush(2)
myStack.stackPush(3)
myStack.stackPush(4)

console.log(myStack)

myStack.stackPeek()

myStack.stackPop()

console.log(myStack)

console.log(myStack.size())