#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datastructures.graph import Graph


@pytest.fixture
def empty_graph():
    """Return an empty Graph"""
    return Graph()


@pytest.fixture
def graph():
    """Return a graph with the US air connexions"""
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
    return g

def test_empty(empty_graph):
    assert empty_graph.empty()

def test_clear(graph):
    graph.clear()
    assert graph.empty()

def test_add_node(graph):
    graph.add_node("Miami")
    assert len(graph.find_node("Miami")) == 1

def test_add_arc(graph):
    ny = graph.find_node("New York").pop()
    sf = graph.find_node("San Francisco").pop()
    size_arcs_ny = len(ny.arcs)
    size_arcs_sf = len(sf.arcs)
    graph.add_arc(ny,sf,2785)
    assert len(ny.arcs) == size_arcs_ny+1
    assert len(sf.arcs) == size_arcs_sf+1


