from pygments.lexer import RegexLexer, words
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator, Punctuation

class GleamLexer(RegexLexer):
    name = 'Gleam'
    aliases = ['gleam']
    filenames = ['*.gleam']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Comments and TODOs
            (r'//.*?$', Comment.Single),
            (r'\b(TODO|FIXME|XXX|NB|NOTE)\b', Comment.Special),

            # Keywords
            (words((
                'import', 'pub', 'panic', 'use', 'type', 'let', 'as', 'if', 
                'else', 'todo', 'const', 'case', 'assert', 'try', 'opaque'
            ), suffix=r'\b'), Keyword),

            # Function definitions
            (r'\bfn\b\s+([a-z][a-z0-9_]*)', Name.Function),

            # Numbers
            (r'\b0[bB][01_]+\b', Number.Bin),  # Binary numbers
            (r'\b0[oO][0-7_]+\b', Number.Oct),  # Octal numbers
            (r'\b0[xX][0-9a-fA-F_]+\b', Number.Hex),  # Hexadecimal numbers
            (r'\b\d+\.\d+(e[-+]?\d+)?\b', Number.Float),  # Float numbers
            (r'\b\d+\b', Number.Integer),  # Integer numbers

            # Operators
            (r'[-+/*]=?|[%=]', Operator),  # Basic operators
            (r'<-|[-|]>', Operator),  # Arrows and pipelines
            (r'&&|\|\|', Operator),  # Boolean operators
            (r'[<>]=?|==|!=', Operator),  # Comparison operators
            (r'\.\.|<>|\|', Operator),  # Miscellaneous operators

            # Types (Capitalized identifiers)
            (r'\b[A-Z][a-zA-Z0-9_]*\b', Name.Class),

            # Strings
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r'\'(\\\\|\\\'|[^\'])*\'', String.Single),

            # Escape sequences within strings
            (r'\\[nrt\\"\'0]', String.Escape),

            # Attributes (e.g., @external)
            (r'@[a-z][a-z_]*', Name.Decorator),

            # Identifiers (variables)
            (r'\b[a-z][a-zA-Z0-9_]*\b', Name.Variable),

            # Punctuation
            (r'[\[\]{}().,:;]', Punctuation),
        ],

        'multiline-comment': [
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[/*]', Comment.Multiline)
        ],
    }

