// First In First Out (FIFO)
// this method of queue is costly to add as it requires 2 stacks.
class Queue {
  constructor (){
    this.q1 = []
    this.q2 = []
  }

  queue (value) {

    // pop all items into q2 and then pop q2 back 
    // into q1 after adding
    while(this.q1.length !== 0) {
      this.q2.push(this.q1.pop())
    }
    this.q1.push(value)
    while(this.q2.length !==0) {
      this.q1.push(this.q2.pop())
    }
  }

  // return the last element
  dequeue () {
    return this.q1.pop()
  }

}

let myqueue = new Queue()
myqueue.queue(1) // [1] 
myqueue.queue(2) // [2,1]
myqueue.queue(3) // [3,2,1]
myqueue.queue(4) // [4,3,2,1]

console.log(myqueue)

console.log(`Dequeing: ${myqueue.dequeue()}`) // returns 1
console.log(`Dequeing: ${myqueue.dequeue()}`) // returns 2
console.log(`Dequeing: ${myqueue.dequeue()}`) // returns 3

console.log(myqueue) // prints 4 in the queue.