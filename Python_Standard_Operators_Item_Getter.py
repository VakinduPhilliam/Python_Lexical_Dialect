# Python Standard Operators
# operator — Standard operators as functions
# The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.
# For example, operator.add(x, y) is equivalent to the expression x+y.
# Many function names are those used for special methods, without the double underscores. For backward compatibility, many of these have a variant with the
# double underscores kept.
# The variants without the double underscores are preferred for clarity.
# The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.

#
# operator.itemgetter(item) operator.itemgetter(*items): 
# Return a callable object that fetches item from its operand using the operand’s __getitem__() method.
# If multiple items are specified, returns a tuple of lookup values.
#
# For example:
# > After f = itemgetter(2), the call f(r) returns r[2].
# > After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
# 

#
# Equivalent to:
# 

def itemgetter(*items):

    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)

    return g

# 
# The items can be any type accepted by the operand’s __getitem__() method.
# Dictionaries accept any hashable value. Lists, tuples, and strings accept an index or a slice:
# 

itemgetter(1)('ABCDEFG')

# OUTPUT: 'B'

itemgetter(1,3,5)('ABCDEFG')

# OUTPUT: '('B', 'D', 'F')'

itemgetter(slice(2,None))('ABCDEFG')

# OUTPUT: 'CDEFG'
 
soldier = dict(rank='captain', name='dotterbart')

itemgetter('rank')(soldier)

# OUTPUT: 'captain'
 
#
# Example of using itemgetter() to retrieve specific fields from a tuple record:
# 

inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]

getcount = itemgetter(1)

list(map(getcount, inventory))

# OUTPUT: '[3, 2, 5, 1]'

sorted(inventory, key=getcount)

# OUTPUT: '[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]'
