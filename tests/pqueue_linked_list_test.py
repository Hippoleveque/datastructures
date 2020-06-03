#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.pqueue_linked_list import PriorityQueueList


@pytest.fixture
def empty_pqueue():
    """Return an empty pqueue"""
    return PriorityQueueList()

@pytest.fixture
def pqueue():
    """Return a queue with one element"""
    pqueue = PriorityQueueList()
    pqueue.enqueue("Learn everything you can",1)
    return pqueue

def test_head(pqueue):
    assert pqueue.head == "Learn everything you can"

def test_empty(empty_pqueue):
    assert empty_pqueue.empty()

def test_enqueue(empty_pqueue):
    empty_pqueue.enqueue(10,1)
    assert empty_pqueue.head == 10

def test_dequeue(pqueue):
    assert pqueue.dequeue() == "Learn everything you can"
    assert pqueue.empty()

def test_raise_error_when_empty_dequeue(empty_pqueue):
    with pytest.raises(ValueError):
        empty_pqueue.dequeue()

def test_raise_error_when_empty_head(empty_pqueue):
    with pytest.raises(ValueError):
        empty_pqueue.head()

def test_priority(pqueue):
    pqueue.enqueue("do smth",3)
    pqueue.enqueue("hello",.5)
    assert pqueue.dequeue() == "hello"
    assert pqueue.dequeue() == "Learn everything you can"
    assert pqueue.dequeue() == "do smth"
