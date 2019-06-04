# Python Bisection Algorithm.
# bisect — Array bisection algorithm.
# This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
# For long lists of items with expensive comparison operations, this can be an improvement over the more common approach.
# The module is called bisect because it uses a basic bisection algorithm to do its work. 
# Unlike the sorted() function, it does not make sense for the bisect() functions to have key or reversed arguments because that would lead to an
# inefficient design (successive calls to bisect functions would not “remember” all of the previous key lookups).
# 
# Instead, it is better to search a list of precomputed keys to find the index of the record in question:
# 

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])

keys = [r[1] for r in data]         # precomputed list of keys

data[bisect_left(keys, 0)]

# OUTPUT: '('black', 0)'

data[bisect_left(keys, 1)]

# OUTPUT: '('blue', 1)'

data[bisect_left(keys, 5)]

# OUTPUT: '('red', 5)'

data[bisect_left(keys, 8)]

# OUTPUT: '('yellow', 8)'
