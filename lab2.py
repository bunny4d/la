  # implement a singly linked list in python with a node class (data,next) and methods:
    #   inset at front ad end
      #   delete at front and treaverse
       #   implement a stcak useing a  linked list puds,pop,end is empty 
         # test linked list insert(10,20,30) delete front test slack,push (5,10) ,pop once ,peek

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

# Testing Linked List
sll = SinglyLinkedList()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
print("Linked list after inserts:")
sll.traverse()  # Output: 10 20 30

sll.delete_front()
print("Linked list after deleting front:")
sll.traverse()  # Output: 20 30

# Testing Stack
stack = Stack()
stack.push(5)
stack.push(10)
print("Stack peek after pushes:", stack.peek())  # Output: 10

print("Stack pop:", stack.pop())                  # Output: 10
print("Stack peek after pop:", stack.peek())     # Output: 5
print("Is stack empty?", stack.is_empty())       # Output: False

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
