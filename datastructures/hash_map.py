#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HashMap:

    class Node:

        def __init__(self,key,value):
            self._key = key
            self._value = value
            self._next = None
        
        @property
        def key(self):
            return self._key
        
        @property
        def value(self):
            return self._value
        
        @property
        def next(self):
            return self._next
        
        @key.setter
        def key(self,new_key):
            self._key = new_key
        
        @value.setter
        def value(self,new_value):
            self._value = new_value
        
        @next.setter
        def next(self,new_next):
            self._next = new_next
        

    def __init__(self):
        self._list = [None for i in range(4)]
        self._capacity = 4
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def empty(self):
        return len(self) == 0
    
    @property
    def capacity(self):
        return self._capacity
    
    def contains(self,key):
        hash_code = hash(key) % self.capacity
        return self._contains(key,hash_code)
    
    def _contains(self,key,hash_code):
        curr = self._list[hash_code]
        while curr != None:
            if curr.key == key:
                return True
        return False
    
    def add(self,key,value):
        found = self._find(key)
        if found is not None:
            found.value = value
            return None
        new_node = self.Node(key,value)
        hash_code = hash(key) % self._capacity
        new_node.next = self._list[hash_code]
        self._list[hash_code] = new_node
        if (len(self) + 1) / self.capacity > .7:
            self._resize()
        self._size += 1
    
    def _find(self,key):
        hash_code = hash(key) % self.capacity
        curr = self._list[hash_code]
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None
    
    def _resize(self):
        new_list = [None for i in range(self.capacity * 2)]
        for el in self._list:
            curr = el
            while curr is not None:
                new_node = self.Node(curr.key,curr.value)
                new_hash = hash(new_node.key) % (self.capacity  * 2)
                new_node.next = new_list[new_hash]
                new_list[new_hash] = new_node
                curr = curr.next
        self._list = new_list
        self._capacity *= 2


    def _find_value(self,key):
        found = self._find(key)
        if found is None:
            raise KeyError("Invalid key")
        return found.value
        
    def __getitem__(self,key):
        return self._find_value(key)
    
    def __setitem__(self,key,value):
        self.add(key,value)
    
