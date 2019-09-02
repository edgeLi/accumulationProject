#!/usr/bin/python
# -*- coding:utf-8 -*-

def recursion_sum(n):
    if n == 1:
        return 1
    return  n + recursion_sum(n-1)

print(recursion_sum(100))