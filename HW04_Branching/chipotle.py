# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def get_protein(order):

    if order[3].lower() == "chicken":
        return 2.5
    elif order[3].lower() == "steak":
        return 3.5
    elif order[3].lower() == "barbacoa":
        return 3.5
    elif order[3].lower() == "carnitas":
        return 3
    elif order[3].lower() == "veggies":
        return 2.5
    elif order[3].lower() == "no protein":
        return 0
    else:
        return 0
    
def get_rice(order):

    if order[4].lower() == "white":
        return 2.5
    elif order[4].lower() == "brown":
        return 3.5
    elif order[4].lower() == "no rice":
        return 0
    else:
        return 0
    
def get_beans(order):

    if order[5].lower() == "black":
        return 2.5
    elif order[5].lower() == "pinto":
        return 2.5
    elif order[5].lower() == "no beans":
        return 0
    else:
        return 0
    
def is_burrito(order):

    if order[6]:
        return 2
    
    return 0

def get_toppings(order):

    total = 0

    if order[3].lower() == "veggies":
        if "guacamole" in order:
            total += 0
    else:
        if "guacamole" in order:
            total += 2.75
    
    if "tomato salsa" in order:
        total += 2.5

    if "chili corn salsa" in order:
        total += 1.75

    if "tomatillo green chili salsa" in order:
        total += 2

    if "tomatillo red chili salsa" in order:
        total += 2

    if "sour cream" in order:
        total += 2.5

    if order[3].lower() == "veggies":
        if "fajita veggies" in order:
            total += 0
    else:
        if "fajita veggies" in order:
            total += 2.5

    if "cheese" in order:
        total += 2

    if "queso blanco" in order:
        total += 2.75

    if "no toppings" in order:
        total = 0

    return total

def apply_discount(order, total):

    if order[2].upper() == "MAGIC":
        total *= 0.95
    elif order[2].upper() == "SUNDAYFUNDAY":
        total *= 0.9
    elif order[2].upper() == "FLAT3":
        total -= 3

    return total

def approximate_time(order):
 
    if order[1].lower() == "amherst" or order[1].lower() == "north amherst" or order[1].lower() == "south amherst" or order[1].lower() == "hadley":
        return 15
    elif order[1].lower() == "northampton" or order[1].lower() == "south hadley" or order[1].lower() == "belchertown" or order[1].lower() == "sunderland":
        return 30
    elif order[1].lower() == "holyoke" or order[1].lower() == "greenfield" or order[1].lower() == "deerfield" or order[1].lower() == "springfield":
        return 45
    
def generate_invoice(order):
    
    sum_of_all_elements = get_protein(order) +  get_beans(order) + get_rice(order) + is_burrito(order) + get_toppings(order)

    print(f"Welcome to Chipotle Mexican Grill Hadley, {order[0]}.\n"
          "Your invoice is displayed below:\n"
          f"Protein: {order[3]} - ${get_protein(order)}\n"
          f"Rice: {order[4]} rice - ${get_rice(order)}\n"
          f"Beans: {order[5]} beans - ${get_beans(order)}\n"
          f"Burrito: {('Yes') if (order[6] == True) else ('No')} - ${is_burrito(order)}\n"
          f"Toppings: {', '.join(order[7:])} - ${get_toppings(order)}\n"
          f"Subtotal: ${sum_of_all_elements}\n"
          f"Discount Code: {order[2]}\n"
          f"Total: ${apply_discount(order, sum_of_all_elements)}\n"
          f"You Save: ${sum_of_all_elements - apply_discount(order, sum_of_all_elements)}\n"
          f"Your order will be ready for pickup in {approximate_time(order)} minutes.\n"
          "Enjoy your meal and have a good day!")
