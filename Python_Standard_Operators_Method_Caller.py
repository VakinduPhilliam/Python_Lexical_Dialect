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
# operator.methodcaller(name[, args...]): 
# Return a callable object that calls the method name on its operand.
# If additional arguments and/or keyword arguments are given, they will be given to the method as well.
#
# For example:
# > After f = methodcaller('name'), the call f(b) returns b.name().
# > After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).
#
 
#
# Equivalent to:
# 

def methodcaller(name, *args, **kwargs):

    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)

    return caller
