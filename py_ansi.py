#!/usr/bin/python3
"""
    ISP printing
     - Created to avoid circular references as used in more than place

    In System Programming (ISP) protocol implementation
   __author__ onyettr
"""
# pylint: disable=unused-argument, invalid-name
#from isp_protocol import ISP_PACKET_DATA_FIELD
ISP_PACKET_DATA_FIELD=1

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

def isp_print_at_xy(fg,message_string, column, row):
    """ 
    Print message at specific coordinates with color

    Args:
        fg: Color name from ansi_fg_colour dictionary
        message_string: Text to print
        column: X coordinate (column)
        row: Y coordinate (row)
    """
    print("\033[%d;%dH%s%s" %(
        row,column,
        ansi_fg_colour[fg],
        message_string))

def isp_print_color(fg, message_string):
    """ print a message """
    print(ansi_fg_colour[fg],end='')
    print(message_string, end='')
    print(ansi_fg_colour["reset"],end='')

def isp_print_response(fg, message):
    """
        print a data response packet
        This is an unknown response format so we just print each elementc
    """
    print_message = message[ISP_PACKET_DATA_FIELD:len(message)-1]

    print(ansi_fg_colour[fg],end='')
    for x in print_message:
        print(hex(x), end='')
        print(' ', end='')
    print(ansi_fg_colour["reset"])

def isp_print_message(fg, message):
    """
        print a PRINT_DATA message
        This is a NULL terminated string
    """
    print_message = bytes(message[ISP_PACKET_DATA_FIELD:len(message)-1])
    eoln = print_message.find(0)
    print_message = print_message[:eoln]
    print(ansi_fg_colour[fg], print_message.decode('utf-8'), \
          ansi_fg_colour["reset"])

def isp_print_terminal_reset():
    """
        isp_print_terminal_reset
            reset the ANSI graphics Terminal
    """
    print("\033[0m")

def isp_print_clear_screen():
    """ isp_print_clear_screen """
    print("\033[2J")

def isp_print_cursor_disable():
    """
        isp_print_cursor_disable
            Stop Cursor Blinking
    """
    print("\033[?25l") # Cursor off

def isp_print_cursor_enable():
    """
        isp_print_cursor_enable
            reset the Cursor to Blinking
    """
    print("\033[?25h")  # Flicker enables Cusror hide DECTCEM, this reenables
