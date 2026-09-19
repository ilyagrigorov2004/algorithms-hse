class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        current = Node(value)
        current.next = self.head
        self.head = current

    def pop(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        return current.value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def empty(self):
        return self.head is None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def empty(self):
        return self.head is None
