# cli_utils/separators.py

def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_char_separator(char):
    print(char * 30)

def print_custom_separator(char, length):
    print(char * length)

def print_labeled_separator(label, char="*", width=30):
    print(label.center(width, char))

def print_box(message, char="*"):
    print(char * (len(message) + 4))
    print(f"* {message} *")
    print(char * (len(message) + 4))