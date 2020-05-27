#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datastructures.stack_linked_list import Stack

class QueueStack:
    """ Queue abstraction with stack as underlying container"""

    def __init__(self):
        self._stack_main = Stack()
        self._stack_temp = Stack()
    
    def __len__(self):
        return len(self._stack_main)
    
    def empty(self):
        return len(self) == 0


    @property
    def head(self):
        if self.empty():
            raise ValueError("Queue is Empty")
        while(not self._stack_main.empty()):
            self._stack_temp.push(self._stack_main.pop())
        to_ret = self._stack_temp.top
        while(not self._stack_temp.empty()):
            self._stack_main.push(self._stack_temp.pop())
        return to_ret
    
    def enqueue(self,el):
        self._stack_main.push(el)
    
    def dequeue(self):
        if self.empty():
            raise ValueError("Queue is empty")
        while(not self._stack_main.empty()):
            self._stack_temp.push(self._stack_main.pop())
        to_ret = self._stack_temp.pop()
        while(not self._stack_temp.empty()):
            self._stack_main.push(self._stack_temp.pop())
        return to_ret