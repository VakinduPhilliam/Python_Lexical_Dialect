# Python Standard Operators
# operator — Standard operators as functions
# The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.
# For example, operator.add(x, y) is equivalent to the expression x+y.
# Many function names are those used for special methods, without the double underscores. For backward compatibility, many of these have a variant with the
# double underscores kept.
# The variants without the double underscores are preferred for clarity.
# The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.
#

#
# Inplace Operators:
# Many operations have an “in-place” version. Listed below are functions providing a more primitive access to in-place operators than the usual syntax does;
# for example, the statement x += y is equivalent to x = operator.iadd(x, y).
# Another way to put it is to say that z = operator.iadd(x, y) is equivalent to the compound statement z = x; z += y.
# In those examples, note that when an in-place method is called, the computation and assignment are performed in two separate steps.
# The in-place functions listed below only do the first step, calling the in-place method. The second step, assignment, is not handled.
#

# 
# For immutable targets such as strings, numbers, and tuples, the updated value is computed, but not assigned back to the input variable:
# 

a = 'hello'

iadd(a, ' world')

# OUTPUT: 'hello world'

a

# OUTPUT: 'hello'
 
#
# For mutable targets such as lists and dictionaries, the inplace method will perform the update, so no subsequent assignment is necessary:
# 

s = ['h', 'e', 'l', 'l', 'o']

iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])

# OUTPUT: '['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']'

s

# OUTPUT: '['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']'
