#!/usr/bin/python3
"""
  ANSI Terminal priniting
   __author__ onyettr
"""
# pylint: disable=unused-argument, invalid-name
#from isp_protocol import ISP_PACKET_DATA_FIELD

# Basic ANSI color codes
FG_BLACK = 30
FG_RED = 31
FG_GREEN = 32
FG_YELLOW = 33
FG_BLUE = 34
FG_MAGENTA = 35
FG_CYAN = 36
FG_WHITE = 37

# Bright ANSI color codes (90-97)
FG_BRIGHT_BLACK = 90  # Gray
FG_BRIGHT_RED = 91
FG_BRIGHT_GREEN = 92
FG_BRIGHT_YELLOW = 93
FG_BRIGHT_BLUE = 94
FG_BRIGHT_MAGENTA = 95
FG_BRIGHT_CYAN = 96
FG_BRIGHT_WHITE = 97

# Text styles
STYLE_NORMAL = 0
STYLE_BOLD = 1
STYLE_UNDERLINE = 4

# Colour table for ANSI terminal printing
ansi_fg_colour = {
    "white"  : "\033[97m",
    "cyan"   : "\033[96m",
    "header" : "\033[95m]",
    "blue"   : "\033[94m",
    "yellow" : "\033[93m",
    "green"  : "\033[92m",
    "red"    : "\033[91m",
    "black"  : "\033[90m",
    "reset"  : "\033[0m",
    # Added additional named colors
    "magenta": "\033[95m",
    "gray"   : "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    # Standard (non-bright) colors
    "std_black": "\033[30m",
    "std_red": "\033[31m",
    "std_green": "\033[32m",
    "std_yellow": "\033[33m",
    "std_blue": "\033[34m",
    "std_magenta": "\033[35m",
    "std_cyan": "\033[36m",
    "std_white": "\033[37m",
    # Text styles
    "bold": "\033[1m",
    "underline": "\033[4m"
}

def print_at_xy(fg,message_string, column, row):
    """ 
    Print message at specific coordinates with color

    Args:
        fg: Color name from ansi_fg_colour dictionary
        message_string: Text to print
        column: X coordinate (column)
        row: Y coordinate (row)
    """
    print(f"\033[{row};{column}H{ansi_fg_colour[fg]}{message_string}")

def print_color(fg, message_string):
    """ print a message """
    print(ansi_fg_colour[fg],end='')
    print(message_string, end='')
    print(ansi_fg_colour["reset"],end='')

def print_message(fg, message):
    """
        print a PRINT_DATA message
        This is a NULL terminated string
    """
    print_message = bytes(message[ISP_PACKET_DATA_FIELD:len(message)-1])
    eoln = print_message.find(0)
    print_message = print_message[:eoln]
    print(ansi_fg_colour[fg], print_message.decode('utf-8'), \
          ansi_fg_colour["reset"])

def print_color_code(color_code, message_string, style=STYLE_NORMAL):
    """
    Print a message with specified ANSI color code
    
    Args:
        color_code: ANSI color code (30-37 or 90-97)
        message_string: Text to print
        style: Text style (default: STYLE_NORMAL)
    """
    print(f"\033[{style};{color_code}m{message_string}\033[0m", end='')

def print_terminal_reset():
    """
        print_terminal_reset
            reset the ANSI graphics Terminal
    """
    print("\033[0m")

def print_clear_screen():
    """ isp_print_clear_screen """
    print("\033[2J")

def print_cursor_disable():
    """
        print_cursor_disable
            Stop Cursor Blinking
    """
    print("\033[?25l") # Cursor off

def print_cursor_enable():
    """
        print_cursor_enable
            reset the Cursor to Blinking
    """
    print("\033[?25h")  # Flicker enables Cusror hide DECTCEM, this reenables
