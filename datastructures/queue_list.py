#!/usr/bin/env python
# -*- coding: utf-8 -*-

class QueueList:

    def __init__(self):
        self._list = []
    
    @property
    def head(self):
        if self.empty():
            raise ValueError("Queue is empty")
        return self._list[0]
    
    def __len__(self):
        return len(self._list)
    
    def empty(self):
        return len(self) == 0
    
    def enqueue(self,el):
        self._list.append(el)
    
    def dequeue(self):
        if self.empty():
            raise ValueError("Queue is empty")
        to_ret, self._list = self.head, self._list[1:]
        return to_ret
    
    
