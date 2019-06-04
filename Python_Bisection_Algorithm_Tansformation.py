# Python Bisection Algorithm.
# bisect — Array bisection algorithm.
# This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
# For long lists of items with expensive comparison operations, this can be an improvement over the more common approach.
# The module is called bisect because it uses a basic bisection algorithm to do its work. 
#
# Searching Sorted Lists.
# 
# The above bisect() functions are useful for finding insertion points but can be tricky or awkward to use for common searching tasks.
#
# The following five functions show how to transform them into the standard lookups for sorted lists:
# 

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)

    if i != len(a) and a[i] == x:
        return i

    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)

    if i:
        return a[i-1]

    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)

    if i:
        return a[i-1]

    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)

    if i != len(a):
        return a[i]

    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)

    if i != len(a):
        return a[i]

    raise ValueError
