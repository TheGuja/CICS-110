# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def read_string(fname):

    try:
        with open(fname, "r") as file:
            contents = file.read()
            return contents
    except:
        print(f"Error occurred when opening {fname} to read")
        return None

def read_lines(fname):

    contents = read_string(fname)

    if contents is not None:
        contents = contents.split("\n")
        if contents[-1] == "":
            contents.pop(-1)

    return contents

def write_string(fname, text):

    try:
        with open(fname, "w") as file:
            file.write(text)
    except:
        print(f"Error occurred when opening {fname} to write")
        return None
    
def write_lines(fname, text):
    write_string(fname, "\n".join(text))

def append_string(fname, text):

    try:
        with open(fname, "a") as file:
            file.write(text)
    except:
        print(f"Error occurred when opening {fname} to append")
        return None

def append_lines(fname, lines):
    append_string(fname, "\n".join(lines))