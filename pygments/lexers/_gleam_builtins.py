"""
    pygments.lexers._gleam_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Gleam builtins.

    :copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Gleam keywords
KEYWORDS = [
    'let', 'fn', 'import', 'pub', 'case', 'of', 'type', 'as', 'if', 'else',
    'try', 'opaque', 'assert', 'todo', 'async', 'await'
]

# Gleam built-in types
BUILTINS = [
    'Int', 'Float', 'Bool', 'String', 'List', 'Result', 'Option', 'Iterator'
]

# Gleam constants
CONSTANTS = [
    'Nil', 'Ok', 'Error', 'Stop', 'Continue'
]
