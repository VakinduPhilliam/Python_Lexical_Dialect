# Python Bisection Algorithm.
# bisect — Array bisection algorithm.
# This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
# For long lists of items with expensive comparison operations, this can be an improvement over the more common approach.
# The module is called bisect because it uses a basic bisection algorithm to do its work. 
# The bisect() function can be useful for numeric table lookups.
# This example uses bisect() to look up a letter grade for an exam score (say) based on a set of ordered numeric breakpoints: 90 and up is an ‘A’, 80 to
# 89 is a ‘B’, and so on:
 
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect(breakpoints, score)

        return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

#
# OUTPUT: '['F', 'A', 'C', 'C', 'B', 'A', 'A']'
#
