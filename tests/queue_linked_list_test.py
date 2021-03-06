#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.queue_linked_list import Queue

@pytest.fixture
def empty_queue():
    """Return empty Queue"""
    return Queue()

@pytest.fixture
def queue():
    """Return queue with 10 on top"""
    queue = Queue()
    queue.enqueue(10)
    return queue

def test_head(queue):
    assert queue.head == 10

def test_empty(empty_queue):
    assert empty_queue.empty()

def test_enqueue(empty_queue):
    empty_queue.enqueue(10)
    assert empty_queue.head == 10

def test_dequeue(queue):
    assert queue.dequeue() == 10
    assert queue.empty()

def test_rais_error_when_empty_head(empty_queue):
    with pytest.raises(ValueError):
        empty_queue.head()

def test_raise_error_when_empty_dequeue(empty_queue):
    with pytest.raises(ValueError):
        empty_queue.dequeue()
    
@pytest.mark.parametrize("enqueue,enqueue_again,dequeue,dequeue_again",[
    (45,55,45,55),
    (34,16,34,16)
])
def test_multiple_enqueues(empty_queue,enqueue,enqueue_again,dequeue,dequeue_again):
    empty_queue.enqueue(enqueue)
    empty_queue.enqueue(enqueue_again)
    assert empty_queue.dequeue() == dequeue
    assert empty_queue.dequeue() == dequeue_again
    assert empty_queue.empty()
