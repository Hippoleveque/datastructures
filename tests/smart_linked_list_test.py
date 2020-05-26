#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datastructures.smart_linked_list import LinkedList
import pytest

@pytest.fixture
def empty_linked_list():
    """ returns an empty LinkedList"""
    return LinkedList()

@pytest.fixture
def linked_list():
    """ returns a LinkedList with 3,2,1 inside"""
    return LinkedList(3,2,1)


def test_empty(empty_linked_list):
    assert empty_linked_list.empty() == True

def test_clear(linked_list):
    linked_list.clear()
    assert linked_list.empty() == True


@pytest.mark.parametrize("index,value",[(2,3),(1,2),(0,1)])
def test_indexes(linked_list,index,value):
    assert linked_list.access(index) == value

@pytest.mark.parametrize("index,value",[(0,3),(1,2),(2,1)])
def test_indexes_reverse(linked_list,index,value):
    assert linked_list.access(index,list_indexing=True) == value


def test_contains(linked_list):
    assert linked_list.contains(3) == True

def test_contains2(linked_list):
    assert linked_list.contains(4)
