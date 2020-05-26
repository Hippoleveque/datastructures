#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections.abc import Iterable

class LinkedList:

    class Node:

        def __init__(self,value):
            self._value = value
            self._next = None
        
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self,val):
            self._value = val
        
        @property
        def next(self):
            return self._next
        
        @next.setter
        def next(self,next):
            if isinstance(next, LinkedList.Node) or next is None:
                self._next = next
            else:
                raise TypeError("Node element in the list can only be linked to another node")
    

    def __init__(self,*args):
        """ Possible initialization a list or just numbers"""
        self._head = None
        self._size = 0
        self.add_all(*args)
        
        
    def __len__(self):
        return self._size
    
    def add(self,el):
        # Add a new elements in the front of the list
        new_node = self.Node(el)
        if not self.empty():
            new_node.next = self._head
        self._head = new_node
        self._size += 1

    def empty(self):
        return len(self) == 0
    
    def add_all(self,*args):
        for element in args:
            if isinstance(element,Iterable):
                for el in element:
                    self.add(el)
            else:
                self.add(element)
    
    def access(self,index,list_indexing=False):
        # by default the list is indexed as first in, first indexed
        if list_indexing:
            steps = len(self) - 1 - index
        else:
            steps = index
        curr_node = self._head
        print(curr_node.value)
        for i in range(steps):
            curr_node = curr_node.next
        return curr_node.value

    def clear(self):
        # clear the list 
        self._head = None
        self._size = 0

    def contains(self,value):
        # return True if the linkedlist contains the object else False
        curr_node = self._head
        while(curr_node != None):
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False


    def __getitem__(self,index):
        # returns the item located at index with default indexing
        return self.access(index)

