class Node:
    def __init__(self, val, next =None):
        self.val = val
        self.next = next

class Stack:
    '''
    Implement a Stack class with push, pop, peek operations.
    Everything should be implemented in O(1) worst-case runtime using a singly
    linked list to implement it. If you have questions about the requirements you
    can ask me.
    '''
    def __init__(self):
        self.head = None

    def push(self, val):
        '''Push new val to head of linked list'''
        new_head = Node(val, self.head)
        self.head = new_head

    def peek(self):
        '''Return current head of linked list'''
        return self.head

    def pop(self):
        '''
        Raises exception if head is none, else makes the next value in the
        linked list the new head and returns the old head.
        '''
        if not self.peek():
            raise IndexError("pop from empty stack")
        old_head = self.head
        self.head = self.head.next
        return old_head

class Queue:
    '''
    Implement a Queue class with enqueue, dequeue, peek operations all in O(1).
    It should use a singly linked list as well.
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        '''Return current head of linked list'''
        return self.head

    def enqueue(self, val):
        '''
        Adds the new val to the end of the linked list by making it the new
        tail. If the linked list is empty by using peek to see if the head is
        None, it then makes the new value both the head and the tail.
        '''
        new_tail = Node(val, None)
        if not self.peek():
            # queue is empty
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

    def dequeue(self):
        '''
        Raises exception if head is none, else makes the next value in the
        linked list the new head and returns the old head.
        '''
        if not self.peek():
            raise IndexError("dequeue from empty queue")
        old_head = self.head
        self.head = self.head.next
        return old_head
