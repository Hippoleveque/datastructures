#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class PriorityQueue:
    """ Priority abstraction with heap as underlying representation, objects are
    stored in tuple (value, priority) inside the heap"""

    def __init__(self):
        self._heap = []
    
    def __len__(self):
        return len(self._heap)
    
    def empty(self):
        return len(self) == 0 
    
    @property
    def head(self):
        if self.empty():
            raise ValueError("pqueue is empty")
        return self._heap[0][0]
    
    def enqueue(self, value, priority):
        new_index = len(self._heap)
        self._heap.append((value,priority))
        self._fix_heap_upward(new_index)
    
    def dequeue(self):
        to_ret = self.head
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        self._heap = self._heap[:-1]
        self._fix_heap_downward(0)
        return to_ret


    def _fix_heap_upward(self,index):
        if index == 0:
            return None
        parent_index = math.floor((index-1)/2)
        # if parent has lesser priority than node swap them
        if self._heap[parent_index][1] > self._heap[index][1]:
            self._heap[parent_index],self._heap[index] = self._heap[index],self._heap[parent_index]
        self._fix_heap_upward(parent_index)

      
    def _fix_heap_downward(self,index):
        last_index = len(self) - 1
        if last_index < index * 2 + 2:
            return None
        elif last_index == index * 2 + 1:
            # only one children for the righmost parent node
            if self._heap[index][1] > self._heap[index*2+1][1]:
                self._heap[index], self._heap[index*2+1] = self._heap[index*2+1], self._heap[index]
        else:
            # both children are in the tree
            # cond1 : parent node has lesser priority than left child
            cond1 = self._heap[index][1] > self._heap[2*index+1][1]
            # cond2 : right child has lesser priority than left child
            cond2 = self._heap[2*index+2][1] >= self._heap[2*index+1][1]
            if cond1 and cond2:
                self._heap[index], self._heap[2*index+1] = self._heap[2*index+1],self._heap[index]
                self._fix_heap_downward(2*index+1)
            # cond3 : parent node has lesser priority than right child
            elif self._heap[index][1] > self._heap[2*index+2][1]:
                self._heap[index],self._heap[2*index+2] = self._heap[2*index+2], self._heap[index]
                self._fix_heap_downward(2*index+2)
    