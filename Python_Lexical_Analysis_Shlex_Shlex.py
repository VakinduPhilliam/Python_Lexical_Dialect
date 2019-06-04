# Python Lexical Analysis.
# shlex — Simple lexical analysis.
# The shlex class makes it easy to write lexical analyzers for simple syntaxes resembling that of the Unix shell.
# This will often be useful for writing minilanguages, (for example, in run control files for Python applications) or for parsing quoted strings.
# The shlex module defines the following functions:
# shlex.split(s, comments=False, posix=True). 
# Split the string s using shell-like syntax.
# If comments is False (the default), the parsing of comments in the given string will be disabled (setting the commenters attribute of the shlex instance
# to the empty string). This function operates in POSIX mode by default, but uses non-POSIX mode if the posix argument is false.
#
# The shlex class provides compatibility with the parsing performed by common Unix shells like bash, dash, and sh. To take advantage of this compatibility, 
# specify the punctuation_chars argument in the constructor. This defaults to False, which preserves pre-3.6 behaviour.
# However, if it is set to True, then parsing of the characters ();<>|& is changed: any run of these characters is returned as a single token. 
# Instead of passing True as the value for the punctuation_chars parameter, you can pass a string with specific characters, which will be used to determine
# which characters constitute punctuation.
#

#
# For example:
# 

import shlex

s = shlex.shlex("a && b || c", punctuation_chars="|")

list(s)

# OUTPUT: '['a', '&', '&', 'b', '||', 'c']'
 

#
# Note: 
# When punctuation_chars is specified, the wordchars attribute is augmented with the characters ~-./*?=.
# That is because these characters can appear in file names (including wildcards) and command-line arguments (e.g. --color=auto).
#
# Hence:
# 

import shlex

s = shlex.shlex('~/a && b-c --color=auto || d *.py?',
                punctuation_chars=True)

list(s)

# OUTPUT: '['~/a', '&&', 'b-c', '--color=auto', '||', 'd', '*.py?']'
