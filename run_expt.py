#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
# This script generates X copies a random ddsf and ba graph and compares their
# densiites
# Fri May 13 14:41:35 IST 2022
# Author: Vikram Singh (PhD Scholar)
'''

from ddsf import ddsf

g = ddsf(50, 120)
print("Nodes", g.number_of_nodes(), g.number_of_edges())
