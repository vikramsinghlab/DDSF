#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
MIT License

Copyright (c) 2022 Vikram Singh (PhD Scholar at Centre for Computational Biology
and Bioinformatics, Central University of Himachal Pradesh) and Vikram Singh
(Assistant Professor at Centre for Computational Biology and Bioinformatics, 
Central University of Himachal Pradesh)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import networkx as nx
import numpy as np
from .utils import *
from math import modf
import random

def _seed(G, PrefAry, avg_deg, N_current):
    r"""Initially it starts with one edge between two nodes and then new nodes 
    are consecutively added with degree k = n - 1 untill average degree of the 
    order of seed less than average degree of the real network.
    """
    while N_current <= avg_deg:
        preferential_attachment(N_current, PrefAry, G, N_current - 1)
        N_current += 1
    return N_current
    
def _extend_seed(n, m, PrefAry, G, N_current):
    r"""Extends the seed network by consecutively adding new nodes with degree
    recalculating the average degree of remaining network
    """
    while N_current < n:
        deg_av = avg_deg(n - N_current, 2 * (m - len(PrefAry) / 2))
        i = int(deg_av)
        
        if deg_av < 1: 
            k_rem = 1
        else:
            N_rand = random.random()
            
            if N_rand < (deg_av - i):
                k_rem = i
            else:
                k_rem = i + 1

        preferential_attachment(N_current, PrefAry, G, k_rem)
                
        N_current += 1
    
    return N_current
    
    
def ddsf(n, m, c = 0):
    r"""Returns a random scale free graph having approximately similar average
    degree to that of a real network.
 
    Usage
    -----
    G_ddsf = ddsf(n, m, [c])
    
    Parameters
    ----------
    n : int
            Number of nodes

    m : int
            number of edges 
    
    c : float (optional)
              average degree of real network

    Returns
    -------
    G : Graph


    References
    ----------
    .. [1] A. L. Barabási and R. Albert "Emergence of scaling in
       random networks", Science 286, pp 509-512, 1999.
    """

    G = nx.Graph()
    G.add_edge(0, 1)
    N_current = 2
    # List of existing nodes, with nodes repeated once for each adjacent edge
    repeated_nodes = [0, 1]
    if not c: c = avg_deg(n, 2 * m)
    
    # Construct seed network
    N_current = _seed(G, repeated_nodes, c, N_current)
    
    # Extend the seed network
    N_current = _extend_seed(n, m, repeated_nodes, G, N_current)
    
    return G
    
if __name__ == '__main__':
    g = ddsf(50, 120)
    print("Nodes", g.number_of_nodes(), g.number_of_edges())
#    nx.write_edgelist(g, "_edgelist.txt", data=['time_stamp'])
