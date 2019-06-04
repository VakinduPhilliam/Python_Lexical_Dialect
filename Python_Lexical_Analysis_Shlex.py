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
# This idiom would be unsafe:
# 

filename = 'somefile; rm -rf ~'
command = 'ls -l {}'.format(filename)

print(command)  # executed by a shell: boom!

# OUTPUT: 'ls -l somefile; rm -rf ~'

# 
# quote() lets you plug the security hole:
# 

from shlex import quote

command = 'ls -l {}'.format(quote(filename))

print(command)

# OUTPUT: 'ls -l 'somefile; rm -rf ~'

remote_command = 'ssh home {}'.format(quote(command))
print(remote_command)

# OUTPUT: 'ssh home 'ls -l '"'"'somefile; rm -rf ~'"'"''
 
#
# The quoting is compatible with UNIX shells and with split():
# 

from shlex import split

remote_command = split(remote_command)
remote_command

# OUTPUT: '['ssh', 'home', "ls -l 'somefile; rm -rf ~'"]'

command = split(remote_command[-1])
command

# OUTPUT: '['ls', '-l', 'somefile; rm -rf ~']'
