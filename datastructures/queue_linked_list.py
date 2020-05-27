#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    class Node:

        def __init__(self,value):
            self._value = value
            self._next = None
        
        @property
        def value(self):
            return self._value
        
        @property
        def next(self):
            return self._next
        
        @next.setter
        def next(self,next_node):
            if not isinstance(next_node,Queue.Node):
                raise TypeError("Node can only be linked to other nodes")
            self._next = next_node
        
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    

    def __len__(self):
        return self._size

    @property
    def head(self):
        if self.empty():
            raise ValueError("Queue is empty")
        return self._head.value
    
    def empty(self):
        return len(self) == 0
    
    def enqueue(self,el):
        new_node = self.Node(el)
        if self._head is None:
            self._head = new_node
        if self._tail is not None:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
    
    def dequeue(self):
        if self.empty():
            raise ValueError("Queue is Empty")
        to_ret = self.head
        self._head = self._head.next
        if self._head is None:
            #case the list is empty now
            self._tail = None
        self._size -= 1
        return to_ret

