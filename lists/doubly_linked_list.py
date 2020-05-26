#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DoublyLinkedList:
    
    class Node:
        
        def __init__(self,value,next,prev):
            cond_next = isinstance(next,DoublyLinkedList.Node)
            cond_prev = isinstance(prev,DoublyLinkedList.Node)
            if not cond_next and cond_prev:
                raise TypeError("Next and prev must be Node Type")
            self._value = value
            self._next = next
            self._prev = prev
        
        @property
        def value(self):
            return self._value
        
        @property
        def next(self):
            return self._next
            
        @property
        def prev(self):
            return self._prev
        
        @next.setter
        def next(self,next):
            self._next = next
        
        @prev.setter
        def prev(self,prev):
            self._prev = prev
        
        def __repr__(self):
            return str(self._value)
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail
    
    def __len__(self):
        return self._size
    
    def enlist_front(self,value):
        node = DoublyLinkedList.Node(value,None,self._head)
        if not self._head:
            self._tail = node
        else:
            self._head.next = node
        self._head = node
        self._size += 1 
    
    def enlist_back(self,value):
        node = DoublyLinkedList.Node(value,self._tail,None)
        if not self._tail:
            self._head = node
        else:
            self._tail.prev = node
        self._tail = node
        self._size += 1
    
    def remove(self,index):
        if index < 0:
            current_node = self._tail
            for i in range(-2,index,-1):
                current_node = current_node.next
            to_remove = current_node.next
            to_remove.next.prev = current_node
            current_node.next = to_remove.next
            
        if index >= self._size:
            raise IndexError("Index out of range")
        current_node = self._head
        
        for i in range(index-1):
            current_node = current_node.prev
        to_remove = current_node.prev
        current_node.prev = to_remove.prev
        to_remove.prev.next = current_node
        return to_remove
        
    
    def __getitem__(self,index):
        if index < 0:
            index = self._size + index
        if index >= self._size | index < 0:
            raise IndexError("Index out of range")
        current_node = self._head
        for i in range(index):
            current_node = current_node.prev
        return current_node.value  
    
    def __repr__(self):
        list_str = "["
        current_node = self._head
        if current_node:
            for i in range(self._size-1):
                list_str += repr(current_node.value) + ' <-> '
                current_node = current_node.prev
            list_str += repr(current_node.value)
        list_str += "]"
        return list_str

if __name__ == "__main__":
    pass