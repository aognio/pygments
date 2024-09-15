import sys
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.gleam import GleamLexer  # Make sure this file is in the same directory or installed as a package

def highlight_gleam_file(file_path):
    # Read the contents of the .gleam file
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)

    # Use Pygments to highlight the code
    lexer = GleamLexer()
    formatter = TerminalFormatter()
    highlighted_code = highlight(code, lexer, formatter)
    
    # Print the highlighted code to the terminal
    print(highlighted_code)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python highlight_gleam.py <path_to_gleam_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    highlight_gleam_file(file_path)

