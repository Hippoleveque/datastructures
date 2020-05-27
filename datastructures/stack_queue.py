#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datastructures.queue_linked_list import Queue

class StackQueue:
    """ Stack abstraction with two queues as underlying representation"""

    def __init__(self):
        self._queue_first = Queue()
        self._queue_second = Queue()
        self._push_to_first = True
    
    def __len__(self):
        if self._push_to_first:
            return len(self._queue_second)
        else:
            return len(self._queue_first)
    
    def empty(self):
        return len(self) == 0
    
    @property
    def top(self):
        if self._push_to_first:
            return self._queue_second.head
        else:
            return self._queue_first.head
    
    def pop(self):
        if self._push_to_first:
            return self._queue_second.dequeue()
        else: 
            return self._queue_first.dequeue()
    
    def push(self,el):
        if self._push_to_first:
            self._queue_first.enqueue(el)
            while(not self._queue_second.empty()):
                self._queue_first.enqueue(self._queue_second.dequeue())
            self._push_to_first = False
        else:
            self._queue_second.enqueue(el)
            while(not self._queue_first.empty()):
                self._queue_second.enqueue(self._queue_first.dequeue())
            self._push_to_first = True