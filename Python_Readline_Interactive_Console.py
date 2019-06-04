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
# The following example extends the code.InteractiveConsole class to support history save/restore.
# 

import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):

    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):

        code.InteractiveConsole.__init__(self, locals, filename)

        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")

        if hasattr(readline, "read_history_file"):

            try:
                readline.read_history_file(histfile)

            except FileNotFoundError:
                pass

            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)

        readline.write_history_file(histfile)
