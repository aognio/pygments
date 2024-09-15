from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.gleam import GleamLexer

code = '''// This is a comment TODO: Fix this
pub fn main() {
  let number = 42
  let binary_number = 0b1010
  let hex_number = 0x1A3F
  let float_number = 3.14e-2
  let result = if number > 0 { "Positive" } else { "Negative" }
  import my_module as mod
  @external fn add(x: Int, y: Int) -> Int
  let List = [1, 2, 3]
  case result {
    True -> "It's true!"
    False -> "It's false!"
  }
}'''
print(highlight(code, GleamLexer(), TerminalFormatter()))

