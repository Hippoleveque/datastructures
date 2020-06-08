#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.hash_map import HashMap

@pytest.fixture
def empty_map():
    """ Return an empty map"""
    return HashMap()

@pytest.fixture
def map():
    """ Return a map with one element """
    hash_map = HashMap()
    hash_map["France"] = 2000
    return hash_map

def test_empty(empty_map):
    assert empty_map.empty()

def test_getitem(map):
    assert map["France"] == 2000

def test_setitem_add(empty_map):
    empty_map["United States"] = 14000
    assert empty_map.contains("United States")
    assert empty_map["United States"] == 14000

def test_setitem_change(map):
    map["France"] = 2200
    assert map["France"] == 2200

def test_add_and_resize(map):
    map["United States"] = 14000
    map["United Kingdom"] = 2300
    map["Germany"] = 2650
    map["Italy"] = 1500
    map["Spain"] = 1200
    map["Belgium"] = 700
    map["Netherlands"] = 850
    assert map["United Kingdom"] == 2300
    assert map["Germany"] == 2650
    assert map["Italy"] == 1500
    assert map["Spain"] == 1200
    assert map["Belgium"] == 700
    assert map["Netherlands"] == 850
