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
# operator.attrgetter(attr) operator.attrgetter(*attrs): 
# Return a callable object that fetches attr from its operand. If more than one attribute is requested, returns a tuple of attributes.
# The attribute names can also contain dots.
#
# For example:
# > After f = attrgetter('name'), the call f(b) returns b.name.
# > After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
# > After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
#

# 
# Equivalent to:
# 

def attrgetter(*items):

    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')

    if len(items) == 1:
        attr = items[0]

        def g(obj):
            return resolve_attr(obj, attr)

    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)

    return g

def resolve_attr(obj, attr):

    for name in attr.split("."):
        obj = getattr(obj, name)

    return obj
