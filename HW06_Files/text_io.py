# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import basic_io

def echo_to_file(fname, append):

    list_to_append = []

    while True:
        text = input('Enter line of text or "quit": ')

        if text.lower() == "quit":
            if append == True:
                basic_io.append_lines(fname, list_to_append)
                break
            else:
                basic_io.write_lines(fname, list_to_append)
                break

        list_to_append.append(text)

def print_file(fname):

    try:
        with open(fname, "r") as file:
            contents = file.read()
            print(contents)
    except:
        print(f"Error occurred when opening {fname} to read")
        return None

def copy_file(from_name, to_fname):
    
    contents = basic_io.read_lines(from_name)

    if contents is not None:
        basic_io.write_lines(to_fname, contents)
    
def erase_file(fname):

    try:
        basic_io.write_string(fname, "")
    except:
        open(fname, "x")