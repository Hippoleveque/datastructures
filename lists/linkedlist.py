#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LinkedList:
    """
    A class implementing the linkedlist datastructure
    """
    class Node:
        """
        A wrapper class for a node inside the list
        """
        def __init__(self,value,next):
            if isinstance(next,LinkedList.Node) or next is None:
                self._value = value
                self._next = next
            else:
                raise TypeError("Node element must be linked to another node")
                
        @property
        def value(self):
            return self._value
        
        @property
        def next(self):
            return self._next
        
        @next.setter
        def next(self,next):
            if isinstance(next,LinkedList.Node) or next is None:
                self._next = next
            else:
                raise TypeError("Node element must be linked to another node")
        
        @value.setter
        def value(self,value):
            self._value = value
        
        
        def __repr__(self):
            return str(self._value)
        
        
        
    def __init__(self,*args):
        self._head = None
        self._size = 0
        for el in args[::-1]:
            self.add(el)
    
    def __len__(self):
        return self._size
        
    @property
    def head(self):
        return self._head
    
    def add(self,value): 
        # Add an element on the head of the list with complexity O(1)
        node = LinkedList.Node(value,self._head)
        self._head = node
        self._size += 1
    
    def access(self,index):
        # Access the indexth element of the list, starting at the head (O(size))
        if index >= self._size:
            raise IndexError("Index out of range")
        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        return current_node.value    
    
    def print(self):
        # Print the linkedlist in the format el_1 -> ... -> el_k -> ... -> el_n
        list_str = "["
        current_node = self._head
        if current_node:
            for i in range(self._size-1):
                list_str += repr(current_node.value) + ' -> '
                current_node = current_node.next
            list_str += repr(current_node.value)
        list_str += "]"
        return list_str
    
    def insert(self,value,index):
        # Insert a new node with value at index
        if index > self._size:
            raise IndexError("Index out of range")
        current_node = self._head
        if index > 0:
            for i in range(index-1):
                current_node = current_node.next
            node = LinkedList.Node(value,current_node.next)
            current_node.next = node
        elif index == 0:
            self.add(value)
        self._size += 1
        return None
        
    def remove(self,index):
        # Remove the node located at index
        if index > self._size:
            raise IndexError("Index out of range")
        current_node = self._head
        if index > 0:
            for i in range(index-1):
                current_node = current_node.next
            to_remove = current_node.next
            current_node.next = to_remove.next 
        elif index == 0:
            to_remove = self._head
            self._head = None
        self._size -= 1
        return to_remove
    
    def __repr__(self):
        return self.print()
    
    def __getitem__(self,index):
        return self.access(index)
    
    