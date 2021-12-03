# pp142 Strip off {{whitespace}} characters (\s, \t, \n)
"""Removing white spaces:
Use strip(), rstrip() and lstrip() ...
to strip off whitespace characters (\s, \t, \n)
"""

HELLO = ' Hello World '
HELLO_STRIP = HELLO.strip()
HELLO_LSTRIP = HELLO.lstrip()
HELLO_RSTRIP = HELLO.rstrip()

assert f'x{HELLO_STRIP}x' == 'xHello Worldx'
assert f'x{HELLO_LSTRIP}x' == 'xHello World x'
assert f'x{HELLO_RSTRIP}x' == 'x Hello Worldx'