"""
pygments.lexers.odin
~~~~~~~~~~~~~~~~~~~~~

Lexers for the Odin programming language

:copyright: Copyright 2006-2024.
:license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator, Punctuation

__all__ = ['OdinLexer']

class OdinLexer(RegexLexer):
    name = 'Odin'
    aliases = ['odin']
    filenames = ['*.odin']
    mimetypes = ['text/x-odin']

    keywords = {
        'if', 'else', 'for', 'switch', 'case', 'break', 'continue', 'return', 'defer', 'proc', 'struct', 'enum',
        'import', 'foreign', 'package', 'using', 'in', 'cast', 'typeid', 'map', 'dynamic'
    }

    builtins = {
        'int', 'float', 'string', 'bool', 'rune', 'byte', 'uintptr', 'complex', 'rawptr', 'any', 'void'
    }

    constants = {'true', 'false', 'nil'}

    tokens = {
        'root': [
            # Whitespace and newline handling
            (r'\s+', Text),
            (r'\n', Text),

            # Comments
            (r'//.*?$', Comment.Single),
            (r'/\*', Comment.Multiline, 'multiline-comment'),

            # Keywords, built-ins, and constants
            (words(keywords, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(builtins, prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (words(constants, prefix=r'\b', suffix=r'\b'), Keyword.Constant),

            # Function definitions
            (r'\b(proc)\b\s+([a-z_][a-zA-Z0-9_]*)', bygroups(Keyword, Name.Function)),

            # Identifiers (variables, fields)
            (r'\b[a-z_][a-zA-Z0-9_]*\b', Name.Variable),

            # Numbers (binary, octal, hex, float, integer)
            (r'\b0b[01_]+\b', Number.Bin),
            (r'\b0o[0-7_]+\b', Number.Oct),
            (r'\b0x[0-9a-fA-F_]+\b', Number.Hex),
            (r'\b\d+\.\d+(e[+-]?\d+)?\b', Number.Float),
            (r'\b\d+\b', Number.Integer),

            # Strings and escape sequences
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'\\[nrt\\"\'0]', String.Escape),

            # Attributes (e.g., `@[attribute]`)
            (r'@[a-zA-Z_][a-zA-Z0-9_]*', Name.Decorator),

            # Operators (detailed handling)
            (r'[-+/*%=!<>&|^~]', Operator),
            (r'(\bnot\b|\band\b|\bor\b)', Operator.Word),  # Logical operators

            # Punctuation (blocks, tuples, arrays, maps)
            (r'[()\[\]{}.,:;]', Punctuation),
        ],

        # Handle multiline comments with nesting
        'multiline-comment': [
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[/*]', Comment.Multiline),
        ],
    }
