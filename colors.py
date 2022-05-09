white= "\u001b[38;2;255;255;255m"
tan = "\u001b[38;2;189;189;78m"
brown= "\u001b[38;2;196;98;16m"
cyan= "\u001b[38;2;0;255;255m"
green= "\u001b[38;2;0;128;0m"
orange= "\033[0;33m"
pink= "\033[1;31m"
blue= "\033[0;34m"
purple= "\033[95m"
darkcyan= "\033[36m"
yellow= "\033[93m"
red= "\033[31m"
dark_red = "\u001b[38;2;255;0;0m"
black= "\033[0;30m"
magenta= "\u001b[38;2;255;0;255m"
lime= "\033[0;92m"
gray = "\u001b[38;2;128;128;128m"
#styles
bold= "\033[1m"
underline= "\033[4m"
reset= "\033[0m"

bg_none= '\x1b[0m'
bg_black= '\x1b[40m'
bg_red= '\x1b[41m'
bg_green= '\x1b[42m'
bg_yellow= '\x1b[43m'
bg_blue= '\x1b[44m'
bg_magenta= '\x1b[45m'
bg_cyan= '\x1b[46m'
bg_white= '\x1b[47m'
bg_grey= '\x1b[100m'
bg_bright_red= '\x1b[101m'
bg_bright_green= '\x1b[102m'
bg_bright_yellow= '\x1b[103m'
bg_bright_blue= '\x1b[104m'
bg_bright_magenta= '\x1b[105m'
bg_bright_cyan= '\x1b[106m'

#\u001b[48;5; means bg
#\u001b[38;5; means text color

def color(msg, color):
  try:
    print(f"{color}{msg}{reset}")
  except AttributeError:
    quit(f'color not found "{color}"')