
from py_ansi import *

def main():

    isp_print_color("blue", "Hello")
    isp_print_terminal_reset()
    isp_print_clear_screen()
    isp_print_at_xy("red", "hello <10,1>", 10,1)
    isp_print_at_xy("red", "hello <123,1>", 23,1)
    isp_print_at_xy("green", "there <3,4>", 3,4)
    isp_print_at_xy("cyan", "string3 <15,10>", 15,10)
    isp_print_at_xy("yellow", "string2 <20,20>", 20,20)

    input("Next tests")
    isp_print_terminal_reset()
    isp_print_clear_screen()

    for rows in range(1,20):
        for i in range(1,80):
            isp_print_at_xy("green", i, i,rows)

if __name__ == "__main__":
    main()