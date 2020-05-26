#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.stack_with_list import StackList


@pytest.fixture
def empty_stack():
    """Return empty stack"""
    stk = StackList()
    return stk

@pytest.fixture
def stack():
    """Return stack with 10 inside"""
    stack = StackList()
    stack.push(10)
    return stack

def test_top(stack):
    assert stack.top == 10


def test_empty(empty_stack):
    assert empty_stack.empty() == True

def test_push(empty_stack):
    stk = empty_stack
    stk.push(20)
    assert empty_stack.top == 20


def test_pop(stack):
    assert stack.pop() == 10
    assert stack.empty() == True

def test_raise_error_when_empty(empty_stack):
    with pytest.raises(ValueError):
        empty_stack.pop()

@pytest.mark.parametrize("push,push_again,pop,pop_again",[
    (45,55,55,45),
    (34,16,16,34),
])
def test_multiple_pushes(empty_stack, push, push_again, pop, pop_again):
    empty_stack.push(push)
    empty_stack.push(push_again)
    assert empty_stack.pop() == pop
    assert empty_stack.pop() == pop_again
    assert empty_stack.empty() == True
