# Printing red text for errors
def print_red(text):
    print("\033[91m {}\033[00m".format(text))


# Printing green text for messeages
def print_green(text):
    print("\003[21m {}\033[00m".format(text))


# Printing yellow text for messeages
def print_yellow(text):
    print("\003[93m {}\033[00m".format(text))
