# Python Readline
# readline — GNU readline interface
# The readline module defines a number of functions to facilitate completion and reading/writing of history files from the Python interpreter.
# This module can be used directly, or via the rlcompleter module, which supports completion of Python identifiers at the interactive prompt.
# Settings made using this module affect the behaviour of both the interpreter’s interactive prompt and the prompts offered by the built-in input() function.
#
 
#
# Readline keybindings may be configured via an initialization file, typically .inputrc in your home directory. 
#

#
# The following example demonstrates how to use the readline module’s history reading and writing functions to automatically load and save a history file
# named .python_history from the user’s home directory.
# The code below would normally be executed automatically during interactive sessions from the user’s PYTHONSTARTUP file.
# 

import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)

    # default history len is -1 (infinite), which may grow unruly

    readline.set_history_length(1000)

except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)
