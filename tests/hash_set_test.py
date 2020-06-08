#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.hash_set import HashSet

@pytest.fixture
def empty_set():
    """ Return an empty set """
    return HashSet()

@pytest.fixture
def set():
    """ Return a set with 10 inside"""
    hash_set = HashSet()
    hash_set.add(10)
    return hash_set

def test_empty(empty_set):
    assert empty_set.empty()

def test_contain(set):
    assert set.contains(10)

def test_remove(set):
    set.remove(10)
    assert set.empty()

def test_add_and_resize(empty_set):
    for i in range(10):
        empty_set.add(i)
    for i in range(10):
        assert empty_set.contains(i)