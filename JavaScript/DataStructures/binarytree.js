class Node {
  constructor(value) {
    this.left = null
    this.right = null
    this.value = value
  }
}

class BinarySearchTree {
  // constructor: value
  // add
  // remove
  // printDFS
  // printBFS
  // insert

  constructor() {
    this.root = null
  }

  add(value) {
    // base is if no values in the tree, it is the root
    const newNode = new Node(value)
    if (this.root === null) {
      this.root = newNode
    }
    else {
      this._add(this.root, newNode)
    }
  }

  _add(currentNode, newNode) {
    console.log(`currentNodeValue: ${currentNode.value} and newNodeValue: ${newNode.value}`)
    if (newNode.value < currentNode.value) {
      if (currentNode.left === null) {
        console.log(`adding: ${newNode.value} on the left`)
        currentNode.left = new Node(newNode.value)
      } else {
        console.log(`going LEFT with value: ${currentNode.value} and nodevalue: ${newNode.value}`)
        this._add(currentNode.left, newNode)
      }
    } else if (newNode.value > currentNode.value) {
      if (currentNode.right === null) {
        console.log(`adding: ${newNode.value} on the right`)
        currentNode.right = new Node(newNode.value)
      } else {
        console.log(`going RIGHT with currentNodeValue: ${currentNode.value} and newNodeValue: ${newNode.value}`)

        this._add(currentNode.right, newNode)
      }
    } else {
      console.log('value in tree already')
    }
  }
}


let myBST = new BinarySearchTree()
myBST.add(3)
myBST.add(2)
myBST.add(4)
myBST.add(1)
myBST.add(5)
myBST.add(5)

console.log(myBST)

// myBest.print()