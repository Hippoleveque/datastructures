#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datastructures.pqueue_heap import PriorityQueue
from datastructures.stack_linked_list import Stack
from datastructures.queue_linked_list import Queue
from copy import deepcopy


class Graph:

    class Node:

        def __init__(self,value):
            self._value = value
            self._arcs = []


        @property
        def value(self):
            return self._value

        @property
        def arcs(self):
            return self._arcs
        
        @value.setter
        def value(self,new_value):
            self._value = new_value
        
        def add_arc(self,new_arc):
            if not isinstance(new_arc, Graph.Arc):
                raise TypeError("Arc must be Graph.Arc type")
            self._arcs.append(new_arc)
    
        def __repr__(self):
            return self.value

    class Arc:

        def __init__(self,start,finish,value):
            # checking if start and finish are Nodes
            if not isinstance(start,Graph.Node) or not isinstance(finish,Graph.Node):
                raise TypeError("Nodes in Arc must be Graph.Node type")
            self._start = start
            self._finish = finish
            self._value = value
        
        @property
        def value(self):
            return self._value
        
        @property
        def start(self):
            return self._start
        
        @property
        def finish(self):
            return self._finish
        
        def __repr__(self):
            return str(self.start.value) + " -> " + str(self.finish.value)
        

    def __init__(self):
        self._nodes = set()
        self._arcs = set()
    

    def __len__(self):
        # returns the number of nodes in the Graph
        return len(self._nodes)



    @property
    def nodes(self):
        return self._nodes
    
    @property
    def arcs(self):
        return self._arcs

    def empty(self):
        return len(self) == 0
    
    def clear(self):
        self._nodes = set()
        self._arcs = set()
    
    def find_node(self,value):
        """return a set of nodes which value are equal to value"""
        to_ret = set()
        for el in self._nodes:
            if el.value == value:
                to_ret.add(el)
        return to_ret

    def add_node(self,value):
        # return new_node 
        new_node = self.Node(value)
        self._nodes.add(new_node)
        return new_node 

    def remove_node(self, node):
        # you must provide the node to delete because you can have duplicate values etc
        # return the node in case
        self._nodes.remove(node)
        return node

    def add_arc(self,start,finish,value,bidir=True):
        new_arc = self.Arc(start,finish,value)
        start.add_arc(new_arc)
        if bidir:
            new_arc_inv = self.Arc(finish,start,value)
            finish.add_arc(new_arc_inv)
        self._arcs.add(new_arc)
        return new_arc
    
    def remove_arc(self,arc):
        self._arcs.remove(arc)
        return arc

    def print_dfs(self,start):
        tagged = set()
        self._print_dfs(start,tagged)

    def _print_dfs(self, start, tagged):
        print(start.value)
        tagged.add(start)
        for arc in start.arcs:
            if arc.finish not in tagged:
                self._print_dfs(arc.finish,tagged)

    def print_bfs(self,start):
        tagged = set() 
        to_process = Queue()
        to_process.enqueue(start)
        tagged.add(start)
        while(not to_process.empty()):
            curr = to_process.dequeue()
            print(curr.value)
            for el in curr.arcs:
                if el.finish not in tagged:
                    tagged.add(el.finish)
                    to_process.enqueue(el.finish)


    def shortest_path(self,start,finish):
        """ Returns shortest path as a stack of arcs"""
        pqueue = PriorityQueue()
        distances = {}
        # a pqueue composed of path stack of arcs
        for arc in start.arcs:
            path = Stack()
            path.push(arc)
            pqueue.enqueue(path, arc.value)
        while(True):
            # get the shortest path so far
            path, cost = pqueue.dequeue_with_priority()
            arc = path.top
            distances[hash(arc.finish)] = cost
            if arc.start == finish:
                path.pop()
                return path
            for el in arc.finish.arcs:
                if hash(el.finish) not in distances.keys():
                    # checking if you're not turning back
                    path_to_add = deepcopy(path)
                    path_to_add.push(el)
                    pqueue.enqueue(path_to_add,cost+arc.value)
                   
            if pqueue.empty():
                break
        return None

    


    def shortest_path_list(self,start,finish):
        """ Returns shortest path as a list of arcs"""
        pqueue = PriorityQueue()
        distances = {}
        path = []
        # a pqueue composed of path stack of arcs
        distances[hash(start)] = 0
        cost = None
        while(start != finish):
            if cost is None:
                cost = 0
            distances[hash(start)] = cost
            for el in start.arcs:
                if hash(el.finish) not in distances.keys():
                    # checking if you're not turning back
                    path_to_add = path + [el]
                    pqueue.enqueue(path_to_add,cost + el.value)
                    print("Adding path : ", path_to_add, " with priority : ", cost + el.value)
            if pqueue.empty():
                return []
            path, cost = pqueue.dequeue_with_priority()
            start = path[-1].finish
        return path


    def neighbours(self,node):
        to_ret = set()
        for el in node.arcs:
            to_ret.add(el.finish)
        return to_ret

if __name__ == "__main__":
    g = Graph()
    portland = g.add_node("Portland")
    sf = g.add_node("San Francisco")
    seattle = g.add_node("Seattle")
    boston = g.add_node("Boston")
    ny = g.add_node("New York")
    atlanta = g.add_node("Atlanta")
    chicago = g.add_node("Chicago")
    denver = g.add_node("Denver")
    dallas = g.add_node("Dallas")
    la = g.add_node("Los Angeles")
    g.add_arc(portland,sf,550)
    g.add_arc(portland,seattle,130)
    g.add_arc(sf,denver,954)
    g.add_arc(sf,dallas,1468)
    g.add_arc(la,dallas,1240)
    g.add_arc(dallas,denver,650)
    g.add_arc(denver,chicago,907)
    g.add_arc(dallas,atlanta,725)
    g.add_arc(chicago,atlanta,599)
    g.add_arc(atlanta,ny, 756)
    g.add_arc(ny,boston,191)
    g.add_arc(boston,seattle,2489)
    g.print_dfs(sf)
    print("--------------------------------------------------------------------------------------------")
    g.print_bfs(sf)
    path = g.shortest_path_list(sf,boston)
    print("--------------------------------------------------------------------------------------------")
    print(path)