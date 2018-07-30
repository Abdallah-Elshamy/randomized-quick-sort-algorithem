#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:25:02 2018

@author: Abdallah-Elshamy
"""
from random import randrange
            
def quick_sort(ints_list,begin=0, end=None):
    if end is None:
        end = len(ints_list)   
    i= begin +1
    if end - begin >1:
        pivot =randrange(begin ,end)      
        ints_list[pivot],ints_list[begin] = ints_list[begin],ints_list[pivot]
        for j in range(i,end):
            if ints_list[begin] > ints_list[j]:
                ints_list[i] , ints_list[j] = ints_list[j] ,ints_list[i]
                i += 1
        ints_list[begin],ints_list[i-1] = ints_list[i-1],ints_list[begin]
        quick_sort(ints_list,begin,i-1)
        quick_sort(ints_list,i,end)



ints = open('QuickSort.txt','r')
ints_list = list(map(int,ints.read().split('\n')[:-1]))
ints.close()

quick_sort(ints_list)
print((ints_list))










