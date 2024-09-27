from Node import Node

class MUStack():
    def __init__(self):
        self.head = Node("head")
        self.count = 0

    def pop(self):
        if self.count == 0:
            return "Cannot pop from stack because stack is empty."
        else:
            remove = self.head.next
            self.head.next = remove.next
            self.count -= 1
            return remove.value
    
    def peek(self):
        if self.count == 0:
            return None
        else:
            return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.count += 1 
        
    def size(self):
        return self.count

    