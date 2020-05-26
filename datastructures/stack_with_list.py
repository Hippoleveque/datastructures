#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StackList:

    def __init__(self):
        self._list = []
    
    @property
    def top(self):
        if self.empty():
            raise ValueError("Stack is empty")
        return self._list[-1]
    
    def __len__(self):
        return len(self._list)
        
    def empty(self):
        return len(self) == 0

    def pop(self):
        if self.empty():
            raise ValueError("Stack is empty")
        to_ret = self._list[-1]
        self._list = self._list[:-1]
        return to_ret
    
    def push(self,el):
        self._list.append(el)
    
    def __del__(self):
        while(not self.empty()):
            self.pop()
            
        
    