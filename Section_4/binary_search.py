#!/usr/bin/env python3

def do_bs (target, range):
    
    low = 0
    high = len(range) - 1

    while low <= high:

        mid = (low + high) // 2

        if target == range[mid]: 
            return mid
        if range[mid] > target:
            high = mid - 1
        if range[mid] < target:
            low = mid + 1

print(do_bs(5, [1,2,3,4,5]))