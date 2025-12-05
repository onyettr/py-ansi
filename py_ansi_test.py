
from py_ansi import *
import math

# Box drawing characters (Unicode)
BOX_CHARS = {
    'simple': {
        'top_left': '+', 'top_right': '+', 
        'bottom_left': '+', 'bottom_right': '+',
        'horizontal': '-', 'vertical': '|'
    },
    'single': {
        'top_left': '┌', 'top_right': '┐', 
        'bottom_left': '└', 'bottom_right': '┘',
        'horizontal': '─', 'vertical': '│'
    },
    'double': {
        'top_left': '╔', 'top_right': '╗', 
        'bottom_left': '╚', 'bottom_right': '╝',
        'horizontal': '═', 'vertical': '║'
    },
    'rounded': {
        'top_left': '╭', 'top_right': '╮', 
        'bottom_left': '╰', 'bottom_right': '╯',
        'horizontal': '─', 'vertical': '│'
    }
}

def test_rainbow(message_string):
    """
    Print text with rainbow colors (cycles through colors)
    
    Args:
        message_string: Text to print with rainbow effect
    """
    colors = [91, 93, 92, 96, 94, 95]  # Bright colors for rainbow effect
    for i, char in enumerate(message_string):
        color_code = colors[i % len(colors)]
        print(f"\033[{color_code}m{char}", end='')
    print(ansi_fg_colour["reset"])

def draw_circle(center_x, center_y, radius, color="green", character="●"):
    """
    Draw a circle on the terminal using print_at_xy function
    
    Args:
        center_x: X coordinate of the circle center
        center_y: Y coordinate of the circle center
        radius: Radius of the circle in characters
        color: Color name for the circle
        character: Character to use for drawing the circle
    """
    # Account for terminal characters being roughly twice as tall as wide
    aspect_ratio = 2.0

    # Draw the circle by sampling points around the circumference
    for angle in range(0, 360, 2):  # Step by 2 degrees for smoother circles
        # Convert angle to radians
        rad = math.radians(angle)

        # Calculate position
        x = int(center_x + (radius * math.cos(rad) * aspect_ratio))
        y = int(center_y + (radius * math.sin(rad)))

        # Draw the point
        print_at_xy(color, character, x, y)

def draw_filled_circle(center_x, center_y, radius, color="green", character="●"):
    """
    Draw a filled circle on the terminal using print_at_xy function

    Args:
        center_x: X coordinate of the circle center
        center_y: Y coordinate of the circle center
        radius: Radius of the circle in characters
        color: Color name for the circle
        character: Character to use for drawing the circle
    """
    # Account for terminal characters being roughly twice as tall as wide
    aspect_ratio = 2.0

    # Draw concentric circles from radius down to 1
    for r in range(radius, 0, -1):
        for angle in range(0, 360, 5):  # Larger step for inner circles
            # Convert angle to radians
            rad = math.radians(angle)

            # Calculate position
            x = int(center_x + (r * math.cos(rad) * aspect_ratio))
            y = int(center_y + (r * math.sin(rad)))

            # Draw the point
            print_at_xy(color, character, x, y)

def draw_concentric_circles(center_x, center_y, max_radius, colors=None, character="●"):
    """
    Draw concentric circles with different colors

    Args:
        center_x: X coordinate of the circles center
        center_y: Y coordinate of the circles center
        max_radius: Maximum radius for the outermost circle
        colors: List of colors to use (cycles if fewer colors than needed)
        character: Character to use for drawing the circles
    """
    if colors is None:
        # Default color sequence if none provided
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    # Draw circles from outside in
    for r in range(max_radius, 0, -2):
        color_idx = (max_radius - r) % len(colors)
        draw_circle(center_x, center_y, r, colors[color_idx], character)

def draw_box(x, y, width, height, color="green", style="simple", fill=False, fill_char=" "):
    """
    Draw a rectangular box on the terminal
    
    Args:
        x: X coordinate of the top-left corner
        y: Y coordinate of the top-left corner
        width: Width of the box in characters
        height: Height of the box in characters
        color: Color name for the box
        style: Box style ('simple', 'single', 'double', or 'rounded')
        fill: Whether to fill the box (default: False)
        fill_char: Character to use for filling (default: space)
    """
    # Get the correct box characters for the selected style
    if style not in BOX_CHARS:
        style = "simple"  # Default to simple if style not found
    chars = BOX_CHARS[style]

    # Fill the box if requested
    if fill:
        for row in range(y + 1, y + height):
            fill_line = fill_char * (width - 2)
            print_at_xy(color, fill_line, x + 1, row)

    # Draw the horizontal lines (top and bottom)
    top_line = chars['top_left'] + (chars['horizontal'] * (width - 2)) + chars['top_right']
    bottom_line = chars['bottom_left'] + (chars['horizontal'] * (width - 2)) + chars['bottom_right']

    print_at_xy(color, top_line, x, y)
    print_at_xy(color, bottom_line, x, y + height)

    # Draw the vertical lines (left and right)
    for row in range(y + 1, y + height):
        print_at_xy(color, chars['vertical'], x, row)
        print_at_xy(color, chars['vertical'], x + width - 1, row)

def draw_titled_box(x, y, width, height, title, color="green", style="simple", fill=False):
    """
    Draw a box with a title at the top

    Args:
        x: X coordinate of the top-left corner
        y: Y coordinate of the top-left corner
        width: Width of the box in characters
        height: Height of the box in characters
        title: Title text to display at the top of the box
        color: Color name for the box
        style: Box style ('simple', 'single', 'double', or 'rounded')
        fill: Whether to fill the box (default: False)
    """
    # Draw the basic box
    draw_box(x, y, width, height, color, style, fill)

    # Calculate title position and ensure it fits in the box
    if len(title) > width - 4:
        title = title[:width - 7] + "..."

    # Center the title
    title_x = x + max(1, (width - len(title)) // 2)

    # Draw the title
    print_at_xy(color, title, title_x, y)

def draw_nested_boxes(x, y, width, height, levels=3, colors=None, styles=None, padding=2):
    """
    Draw nested boxes inside each other

    Args:
        x: X coordinate of the top-left corner of the outermost box
        y: Y coordinate of the top-left corner of the outermost box
        width: Width of the outermost box in characters
        height: Height of the outermost box in characters
        levels: Number of nested boxes to draw
        colors: List of colors to use (cycles if fewer colors than levels)
        styles: List of styles to use (cycles if fewer styles than levels)
        padding: Space between nested boxes
    """
    if colors is None:
        colors = ["green", "yellow", "cyan", "magenta", "red", "blue"]

    if styles is None:
        styles = ["double", "single", "rounded", "simple"]

    current_x = x
    current_y = y
    current_width = width
    current_height = height

    for level in range(levels):
        if level >= min(current_width // 2, current_height // 2):
            break  # Stop if boxes become too small

        color = colors[level % len(colors)]
        style = styles[level % len(styles)]

        draw_box(current_x, current_y, current_width, current_height, color, style)

        # Calculate dimensions for the next inner box
        current_x += padding
        current_y += padding
        current_width -= (padding * 2)
        current_height -= (padding * 2)

def draw_box_demo():
    """
    Demonstrate various box drawing capabilities
    """
    print_clear_screen()

    # Simple box
    draw_box(5, 3, 20, 6, "green", "simple")

    # Single-line box with title
    draw_titled_box(30, 3, 25, 6, "Single-Line Box", "cyan", "single")

    # Double-line filled box
    draw_box(5, 12, 20, 6, "yellow", "double", True, ".")

    # Rounded box with title
    draw_titled_box(30, 12, 25, 6, "Rounded Box", "magenta", "rounded")

    # Nested boxes
    draw_nested_boxes(60, 5, 30, 15, 4)

    # Position cursor at the bottom
    print("\033[25;1H")
    print("Box drawing demonstration complete.")

    print_terminal_reset()

def main():

    print_color("blue", "Hello")
    print_terminal_reset()
    print_clear_screen()
    print_at_xy("red", "hello <10,1>", 10,1)
    print_at_xy("red", "hello <123,1>", 23,1)
    print_at_xy("green", "there <3,4>", 3,4)
    print_at_xy("cyan", "string3 <15,10>", 15,10)
    print_at_xy("yellow", "string2 <20,20>", 20,20)

    input("Press [ENTER] for next tests")
    print_terminal_reset()
    print_clear_screen()

    for rows in range(1,20):
        for i in range(1,80):
            print_at_xy("green", i, i,rows)

    input("Press [ENTER] for next tests")
    for color in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
                  "bright_red", "bright_green", "bright_yellow", "bright_blue", 
                  "bright_magenta", "bright_cyan", "bright_white"]:
        if color in ansi_fg_colour:
            print_color(color, f"  This is {color} text\n")

    print("\nANSI Color Codes (Standard):")
    for code in range(30, 38):
        print_color_code(code, f"  This is color code {code}\n")

    print("\nANSI Color Codes (Bright):")
    for code in range(90, 98):
        print_color_code(code, f"  This is color code {code}\n")

    print("\nText Styles:")
    print_color("bold", "  Bold text\n")
    print_color("underline", "  Underlined text\n")

    print("\nSpecial Effects:")
    test_rainbow("Rainbow\n")

    input("Press [ENTER] for next steps")
    # put things back
    print_clear_screen()
    # Circle demos
    draw_circle(20, 10, 7, "green", "●")

    # Filled circle
    draw_filled_circle(45, 10, 5, "red", "●")

    # Concentric circles with different colors
    draw_concentric_circles(70, 15, 10, ["blue", "cyan", "green", "yellow", "red"], "●")

    input("Press [ENTER] for next step")
    draw_box_demo()

    # put things back
    print_terminal_reset()

if __name__ == "__main__":
    main()
