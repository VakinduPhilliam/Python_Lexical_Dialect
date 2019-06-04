# Python Stat
# stat — Interpreting stat() results
# The stat module defines constants and functions for interpreting the results of os.stat(), os.fstat() and os.lstat() (if they exist). 
#
# Normally, you would use the os.path.is*() functions for testing the type of a file; the functions here are useful when you are doing multiple tests of the
# same file and wish to avoid the overhead of the stat() system call for each test.
# These are also useful when checking for information about a file that isn’t handled by os.path, like the tests for block and character devices.
# 

#
# Example:
# 

import os, sys

from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)

        mode = os.stat(pathname).st_mode

        if S_ISDIR(mode):

            # It's a directory, recurse into it

            walktree(pathname, callback)

        elif S_ISREG(mode):

            # It's a file, call the callback function

            callback(pathname)

        else:

            # Unknown file type, print a message

            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':

    walktree(sys.argv[1], visitfile)
