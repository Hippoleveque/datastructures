#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.binary_search_tree_avl import BinarySearchTree



@pytest.fixture
def empty_tree():
    """Return an empty tree"""
    return BinarySearchTree()

@pytest.fixture
def tree():
    """Return a tree with one element"""
    tree = BinarySearchTree()
    tree.insert(10)
    return tree

def test_root(tree):
    assert tree.root == 10

def test_len(tree):
    assert len(tree) == 1

def test_empty(empty_tree):
    assert empty_tree.empty()

def test_add_root(empty_tree):
    empty_tree.insert(11)
    assert empty_tree.root == 11

def test_remove(tree):
    tree.remove(10)
    assert tree.empty()

def test_insert_and_return_inorder(empty_tree):
    for i in range(10,0,-1):
        empty_tree.insert(i)
    assert empty_tree.return_inorder_list() == list(range(1,11))

def test_contains(empty_tree):
    for el in range(50):
        empty_tree.insert(el)
    assert empty_tree.contains(34)

def test_root_raises_error(empty_tree):
    with pytest.raises(ValueError):
        empty_tree.root()





