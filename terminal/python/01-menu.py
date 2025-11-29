import click
import os

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"

def set_cursor_position(row, col):
    """
    Sets the terminal cursor position to the specified row and column.
    Rows and columns are 1-indexed.
    """
    print(f"\033[{row};{col}H", end="")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# create the menu options
options = ['Option 1', 
           'Option 2', 
           'Option 3', 
           'Option 4', 
           'Exit']

# set the initial active option
active = options[0]

# clear the terminal screen
clear_screen() 

while True:

    # move the cursor to the top-left corner
    set_cursor_position(1, 1)
    
    # show the title
    print("MENU")

    # perform the  options
    for op in options:

        # highlight the active option
        if op == active:
            print(f"{GREEN}{BOLD}> {op}{RESET}")
        else:
            # print the normal option
            print(f"  {op}")

    # get user input for navigation
    char = click.getchar()

    if char == '\x1b[A':  # Up arrow
        idx = options.index(active)
        # move the selection up, wrapping around if necessary
        active = options[idx - 1] if idx > 0 else options[-1]
    elif char == '\x1b[B':  # Down arrow
        idx = options.index(active)
        # move the selection down, wrapping around if necessary
        active = options[idx + 1] if idx < len(options) - 1 else options[0]
    elif char == '\r':  # Enter key
        if active == 'Exit':
            print("Exiting menu.")
            break
        else:
            print(f"You selected: {active}")
            click.pause(info="Press any key to return to the menu...")