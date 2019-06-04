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
# The following example achieves the same goal but supports concurrent interactive sessions, by only appending the new history.
# 

import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)

    h_len = readline.get_current_history_length()

except FileNotFoundError:
    open(histfile, 'wb').close()

    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()

    readline.set_history_length(1000)

    readline.append_history_file(new_h_len - prev_h_len, histfile)

atexit.register(save, h_len, histfile)
