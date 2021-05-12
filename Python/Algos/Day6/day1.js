// singly linked lists
// ListNode class: we'll be using this

class ListNode {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
}

// var x = new ListNode(7);

// var y = new ListNode(3);
// x.next = y;

// var z = new ListNode(29);
// y.next = z;

// console.log(y);

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // addToFront - adds a node with the given value to the head of the list
    addToFront(value) {
        var new_node = new ListNode(value);

        // if list is empty
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        // otherwise
        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    // addToBack - adds a node with the given value to the tail of the list
    addToBack(value) {
        var new_node = new ListNode(value);

        // if list is empty
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }
    // contains - returns true if target is in the linked list (as a node value),
    // false otherwise
    contains(target) {
        var runner = this.head;

        while (runner != null) {

            if (runner.value == target) {
                return true;
            }

            runner = runner.next;
        }

        return false;
    }
    
    // display()
    // return a string with the value of every node from the
    // linked list - like "3 - 7 - 13 - 4 - 8"
    display() {

        if (this.head == null) {
            return null;
        }

        var output = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            output += " - " + runner.value;
            runner = runner.next;
        }

        return output;
    }
}

var new_sll = new SinglyLinkedList();
new_sll.addToFront(7);
new_sll.addToFront(3);
new_sll.addToFront(11);
new_sll.addToBack(4);

console.log(new_sll.contains(4));
console.log(new_sll.contains(3));
console.log(new_sll.contains(27));

