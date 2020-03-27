class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def getval(self):
        return self.val
    
    def getnext(self):
        return self.next

class LinkedList:
    def __init__(self, list):
        previous = Node(list[0])
        self.head = previous
        for v in list[1:]:
            previous.next = Node(v)
            previous = previous.next

    def length(self):
        l = 1
        current = self.head
        while current.next != None:
            current = current.next
            l += 1
        return l
        
    def first(self):
        return self.head.getval()

    def last(self):
        current = self.head
        while current.next != None:
            current = current.next
        return current.getval()

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.getval()

    def append(self, val):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(val)

    def delete(self, index):
        current = self.head
        for i in range(index + 1):
            if current.next != None:
                current = current.next
        new_next = current
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = new_next

    def insert(self, val, index):
        before = self.head
        after = self.head
        for i in range(index - 1):
            if before.next != None:
                before = before.next
        for i in range(index):
            after = after.next
        before.next = Node(val, after)

    def reverse(self, index):
        pass