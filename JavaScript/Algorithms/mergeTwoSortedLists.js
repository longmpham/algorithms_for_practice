// given a singly-linked list, that assumes a Node class with value
// and next, create a function that merges two sorted linked lists

// ex. [1,3,4] + [1,2,5] = [1,1,2,3,4,5]
// notice adding the same number applies and is not discarded

class Node {
  constructor(value){
    this.value = value
    this.next = null
  }
}

class LinkedList {
  constructor(head = null) {
    this.head = head
  }

  add (value) {
    let node = new Node(value)
    
    let currentNode = this.head
    if (currentNode === null) {
      // node is the new head!
      this.head = node
    } else {

      while(currentNode.next) {
        currentNode = currentNode.next
      }
      // after the loop, currentNode.next should be null.
      currentNode.next = node
    }
  }

  print() {
    let arr = []
    if(this.head === null) {
      return "empty"
    } else {
      let currentNode = this.head
      while(currentNode) {
        // console.log(currentNode.value)
        arr.push(currentNode.value)
        currentNode = currentNode.next
      }
    }
    return arr
  }
}

let myLL1 = new LinkedList()

myLL1.add(1)
myLL1.add(3)
myLL1.add(5)
myLL1.add(5)
myLL1.add(5)
console.log(myLL1.print())

let myLL2 = new LinkedList()

myLL2.add(1)
myLL2.add(2)
myLL2.add(4)
myLL2.add(4)
myLL2.add(6)
console.log(myLL2.print())

// takes in two linked lists and returns a new list
function sortLL(l1, l2) {
  let newList = new Node()
  let head = newList
  let p1 = l1.head
  let p2 = l2.head

  while(p1 && p2) {
    console.log(`p1: ${p1.value} p2: ${p2.value}`)
    if(p1.value < p2.value) {
      newList.next = p1
      p1 = p1.next
    } else {
      newList.next = p2
      p2 = p2.next
    }
    newList = newList.next
  }
  newList.next = (p1 || p2)
  return head.next
}

const newList = sortLL(myLL1, myLL2)

console.log(newList)

let mergeLL = new LinkedList(newList)
console.log(mergeLL.print())


