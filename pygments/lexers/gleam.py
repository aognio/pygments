"""
    pygments.lexers.gleam
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for Gleam language

    :copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator, Punctuation

# Import built-ins from _gleam_builtins.py
from ._gleam_builtins import KEYWORDS, BUILTINS, CONSTANTS


__all__ = ['GleamLexer']


class GleamLexer(RegexLexer):
    name = 'Gleam'
    aliases = ['gleam']
    filenames = ['*.gleam']
    mimetypes = ['text/x-gleam']

    # Character sets and tokens
    ID = r'[a-z_][a-zA-Z0-9_]*'
    MODULE_METHOD_CALL = r'([a-z_][a-zA-Z0-9_]*)([.])([a-zA-Z_][a-zA-Z0-9_]*)'
    WHITESPACE = r'\s+'
    NEWLINE = r'\n'

    # Operators and punctuation
    OPERATORS = r'[-+/*%=!<>&|^~]|>>|<<|\|>'
    PUNCTUATION = r'[()\[\]{}.,:;]'

    # Numbers
    BINARY_NUMBER = r'\b0b[01_]+\b'
    OCTAL_NUMBER = r'\b0o[0-7_]+\b'
    HEX_NUMBER = r'\b0x[0-9a-fA-F_]+\b'
    FLOAT_NUMBER = r'\b\d+\.\d+(e[+-]?\d+)?\b'
    INTEGER_NUMBER = r'\b\d+\b'

    # Strings
    DOUBLE_QUOTED_STRING = r'"(\\\\|\\"|[^"])*"'
    SINGLE_QUOTED_STRING = r"'(\\\\|\\'|[^'])*'"
    ESCAPE_SEQUENCE = r'\\[nrt\\"\'0]'

    # Comments
    LINE_COMMENT = r'//.*?$'
    MULTILINE_COMMENT_START = r'/\*'
    MULTILINE_COMMENT_END = r'\*/'

    tokens = {
        'root': [
            (WHITESPACE, Text),
            (NEWLINE, Text),

            # Comments
            (LINE_COMMENT, Comment.Single),
            (MULTILINE_COMMENT_START, Comment.Multiline, 'multiline-comment'),

            # Keywords, built-ins, constants
            (r'\b(?:' + '|'.join(KEYWORDS) + r')\b', Keyword),
            (r'\b(?:' + '|'.join(BUILTINS) + r')\b', Keyword.Type),
            (r'\b(?:' + '|'.join(CONSTANTS) + r')\b', Keyword.Constant),

            # Function definitions
            (r'\bfn\b\s+(' + ID + r')', Name.Function),

            # Module and method calls (e.g., list.map)
            (MODULE_METHOD_CALL, bygroups(Name.Namespace, Punctuation, Name.Function)),

            # Identifiers (variables, fields)
            (r'\b' + ID + r'\b', Name.Variable),

            # Function calls
            (r'([.]\s*)?(' + ID + r')(?=\()', Name.Function),

            # Operators and punctuation
            (OPERATORS, Operator),
            (PUNCTUATION, Punctuation),

            # Numbers
            (BINARY_NUMBER, Number.Bin),
            (OCTAL_NUMBER, Number.Oct),
            (HEX_NUMBER, Number.Hex),
            (FLOAT_NUMBER, Number.Float),
            (INTEGER_NUMBER, Number.Integer),

            # Strings and escape sequences
            (DOUBLE_QUOTED_STRING, String.Double),
            (SINGLE_QUOTED_STRING, String.Single),
            (ESCAPE_SEQUENCE, String.Escape),

            # Attributes
            (r'@' + ID, Name.Decorator),
        ],

        # Multiline comments with nesting
        'multiline-comment': [
            (MULTILINE_COMMENT_START, Comment.Multiline, '#push'),
            (MULTILINE_COMMENT_END, Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[*/]', Comment.Multiline),
        ],
    }
