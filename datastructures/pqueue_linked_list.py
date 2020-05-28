#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PriorityQueueList:
    """ A priority queue with a linked list as its underlying representation"""


    class Node:

        def __init__(self,value,priority):
            self._value = value
            self._priority = priority
            self._next = None
        
        @property
        def value(self):
            return self._value
        
        @property
        def priority(self):
            return self._priority

        @property
        def next(self):
            return self._next
        
        @next.setter
        def next(self,new_next):
            self._next = new_next
    

    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def empty(self):
        return len(self) == 0
    
    @property
    def head(self):
        if self.empty():
            raise ValueError("The priority queue is empty")
        return self._head.value

    def enqueue(self,el, priority):
        new_node = self.Node(el,priority)
        if self._head is None:
            self._head = new_node
        elif new_node.priority < self._head.priority:
            # handle special case where the node must be inserted at the front
            new_node.next = self._head
            self._head = new_node
        else: 
            prevcurr = self._head
            curr = self._head.next
            while (curr is not None and curr.priority < new_node.priority):
                prevcurr = curr
                curr = curr.next
            # now curr is the first Node which priority is lesser than new node
            prevcurr.next = new_node
            new_node.next = curr
        self._size += 1
    
    
    

    def dequeue(self):
        if self.empty():
            raise ValueError("The priority queue is empty")
        to_ret = self.head
        self._head = self._head.next
        self._size -= 1
        return to_ret
    


        