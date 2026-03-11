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
    
def print_ascii_art():
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # This resets the color back to default
    
    top_of_arc = """
   ___ _______________________
  |===|=======================|
  |||||_|_|_|_|_|_|_|_|_|_|_|_|
 [___[_________________________]"""
    middle_of_arc = """  |---|-------|--_-_--|-------|
  |[ ]| [:.:] |,'`. `.| [:.:] |
  ====|========    ||:|========"""
    
    bottom_of_arc = """  ||^||  {$}  |    ||:|  {$}  |
  ||:|| (:..) |    ||:| (:.:) |
  ||:||=======|    ||:|=======|
  ||:||_______|    ||:|_______|"""
  
    print(f"{RED}{top_of_arc}")
    print(f"{RESET}{middle_of_arc}")
    print(f"{BLUE}{bottom_of_arc}")
    