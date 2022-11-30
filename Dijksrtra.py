#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:50:24 2022

@author: chenzhenhua
"""
import numpy as np
import pandas as pd

def Dijkstra(o,d,Ca):
    node = Ca.shape[0]
    C = 1e+100*np.ones(node) #set c(o,n) is inf
    C[o] = 0 #set c(0,0) is 0;
    nodeactive = np.zeros(node) #set the node n that is inactive
    nodeactive[o] = 1 #set the node O that is active
    backnode = np.zeros(node) #set the array of backnode
    while 1:
        # minimum cost
        pos = np.where(nodeactive ==1)[0]
        least_cost = np.concatenate(([C[pos]],[pos]),axis=0)
        n = np.argmin(least_cost[0,:])  #select a node at least cost
        n = int(least_cost[1,n])
        for m in range(node):
            if C[n]+Ca[n][m]<C[m]:
                C[m] = C[n]+Ca[n][m]  # minimum cost to reach;
                backnode[m] = n  #(backnode of m);
                # set the node m that is active
                nodeactive[m] = 1     
        nodeactive[n] = 0 # set the node 1 that is inactive
        if np.all(nodeactive==0): # if there is an active node,then return to step1
            break
    
    # output the route
    route=[d]
    i = d
    while i!=o:
        i=int(backnode[i])
        route.insert(0,i)
    print('the shortest route is:', end=' ')
    for r in route:
        if r!=d:
            print(r, end=' -> ')
        else:
            print(r)
    print('The shortest distance is:'+' '+str(C[d]))
    return C,route

if __name__=="__main__":
    dij = pd.read_excel("dij.xlsx",header=None)
    s=0;t=23
    C,route= Dijkstra(s,t,dij)