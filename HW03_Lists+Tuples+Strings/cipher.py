# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def l337_encrypt(s):
    
    s = s.replace("O", "0")
    s = s.replace("I", "1")
    s = s.replace("E", "3")
    s = s.replace("A", "4")
    s = s.replace("S", "5")
    s = s.replace("T", "7")
    s = s.replace("B", "8")

    return s

def l337_decrypt(s):
    
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    s = s.replace("3", "E")
    s = s.replace("4", "A")
    s = s.replace("5", "S")
    s = s.replace("7", "T")
    s = s.replace("8", "B")

    return s

def odd_even_encrypt(s):

    odd_index_string = ""
    even_index_string = ""

    current_index = 0

    for element in s:
        if current_index % 2 == 0:
            even_index_string += element
        else:
            odd_index_string += element
        
        current_index += 1

    final_string = odd_index_string + even_index_string
    
    return final_string

def odd_even_decrypt(s):

    s = list(s)

    first_half = s[:len(s) // 2]
    second_half = s[len(s) // 2:]

    index_first_half = 1
    index_second_half = 0

    for element in first_half:
        s[index_first_half] = element
        index_first_half += 2

    for element in second_half:
        s[index_second_half] = element
        index_second_half += 2

    s = "".join(s)

    return s

def cipher_encrypt(s):
    s = l337_encrypt(s)
    s = odd_even_encrypt(s)
    s = odd_even_encrypt(s)

    return s

def cipher_decrypt(s):
    s = odd_even_decrypt(s)
    s = odd_even_decrypt(s)
    s = l337_decrypt(s)

    return s