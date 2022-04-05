class Node {
  constructor(value, next) {
    this.value = value
    this.next = null
  }
}

class LinkedList {
  constructor(head = null) {
    this.head = head
  }

  add (value) {
    // create a new node and a node reference
    let node = new Node(value)
    let currentNode

    // if empty, the head is the new node
    if (this.head === null) {
      this.head = node
    } else {
      // if its not, we need to go through the linked list
      // and add it to the end by looping through each
      // node and saving the new pointer. When the pointer 
      // is finally null, we've reached the end that final 
      // node to the new node!
      currentNode = this.head

      while (currentNode.next) {
        currentNode = currentNode.next
      }
      currentNode.next = node
    }
  }

  addFirst (value) {
    let node = new Node(value)

    if(this.head === null) {
      this.head = node
    }
    else {
      let currentNode = this.head
      this.head = node
      node.next = currentNode
    }
    
  }

  addAtIndex(value, index) {
    let node = new Node(value)
    let currentNode = this.head
    let previousNode

    if (index === 0) {
      node.next = this.head
      this.head = node
    } else {
      currentNode = this.head
      let count = 0;
      while (count < index) {
        count++
        // console.log(`curr: ${currentNode.value}`)
        // console.log(`prev: ${previousNode}`)
        previousNode = currentNode
        currentNode = currentNode.next
      }

      // we've reached the index point to add!
      node.next = currentNode
      previousNode.next = node
    }
  }

  removeLast() {
    if(this.head === null) return "empty already"

    let currentNode = this.head
    let previousNode
    while(currentNode.next !== null) {
      previousNode = currentNode
      currentNode = currentNode.next
    }
    previousNode.next = null
    return previousNode
  }

  removeAtIndex(index) {
    if (this.head === null) return "no items left!"

    let currentNode = this.head
    let previousNode

    if (index === 0) {
      this.head = curr.next
    } else {
      let count = 0
      while(count < index) {
        count++
        previousNode = currentNode
        currentNode = currentNode.next
      }
      let returnNode = currentNode
      previousNode.next = currentNode.next
      // console.log(`return node: ${returnNode}`)
      return returnNode
    }
  }

  size () {
    let count = 0
    let currentNode = this.head
    while (currentNode) {
      count++
      currentNode = currentNode.next
    }
    return count
  }

  getList() {
    let currentNode = this.head
    if (currentNode === null) {
      return "empty"
    } else {
      let list = []
      while (currentNode) {
        // console.log(currentNode.value)
        list.push(currentNode.value)
        currentNode = currentNode.next
      }
      // console.log(list)
      return list
    }
  }

  // isEmpty() {
  //   if (this.head === null) return "List is empty"
  // }


}




// test the list

let node1 = new Node(2)
let node2 = new Node(5)
node1.next = node2
let list = new LinkedList(node1)
list.add(3)
list.add(4)
list.add(1)
list.addAtIndex(6,2)
console.log(list.getList())
console.log(list.removeAtIndex(2))
console.log(list.getList())
console.log(list.removeLast())
console.log(list.getList())
list.addFirst(8)
console.log(list.getList())

console.log(list.size())