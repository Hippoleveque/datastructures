#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HashSet:

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
    

        @value.setter
        def value(self,value):
            self._value = value
        
        @next.setter
        def next(self,next):
            self._next = next

    def __init__(self):
        self._list = [None for i in range(4)]
        self._capacity = 4
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def empty(self):
        return len(self) == 0
    
    def add(self,value):
        new_node = self.Node(value)
        hash_code = hash(value) % self._capacity
        if self._contains(value,hash_code):
            return None
        new_node.next = self._list[hash_code]
        self._list[hash_code] = new_node
        self._size += 1
        if self._size / self._capacity > .7:
            self._resize()
        
    
    def contains(self,value):
        hash_code = hash(value) % self._capacity
        return self._contains(value,hash_code)
    
    def _contains(self,value,hash_code):
        curr = self._list[hash_code]
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False
    
    def _resize(self):
        print("resizing")
        new_list = [None for i in range(self._capacity * 2)]
        for el in self._list:
            curr = el
            while curr is not None:
                new_node = self.Node(curr.value)
                new_hash = hash(new_node.value) % (self._capacity * 2)
                new_node.next = new_list[new_hash]
                new_list[new_hash] = new_node
                curr = curr.next
        self._capacity *= 2
        self._list = new_list
    
    def remove(self,value):
        hash_code = hash(value) % self._capacity
        if not self._contains(value,hash_code):
            return None
        self._remove(value,hash_code)
        self._size -= 1
    
    def _remove(self,value,hash_code):
        curr = self._list[hash_code]
        if curr.value == value:
            self._list[hash_code] = curr.next
        else:
            prev = curr
            curr = curr.next
            while curr.value != value:
                prev = curr
                curr = curr.next
            prev.next = curr.next
        