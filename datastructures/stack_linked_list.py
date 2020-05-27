#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datastructures.linked_list import LinkedList

class Stack:

    def __init__(self):
        self._list = LinkedList()
    
    @property
    def top(self):
        return self._list.head
    
    def __len__(self):
        return len(self._list)
    
    def empty(self):
        return self._list.empty()
    
    def pop(self):
        if self.empty():
            raise ValueError("Stack is empty")
        to_ret = self.top
        self._list.remove_front()
        return to_ret
    
    def push(self,el):
        self._list.add(el)
    
