# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

class VendingMachine:
    def __init__(self):
        self.snacks = {}
        self.balance = 0
        self.total_sale = 0

    def list_items(self):
        if self.snacks == {}:
            print("No items in the vending machine")
        else:
            print("Available items:")
            for snack in sorted(self.snacks):
                print(f"{snack} (${self.snacks[snack]['price']}): {self.snacks[snack]['quantity']} available")

    def add_item(self, snack, price, quantity):
        if snack in self.snacks:
            self.snacks[snack] = {"price": price, "quantity": self.snacks[snack]["quantity"] + quantity}
            print(f"{quantity} {snack}(s) added to inventory")
        else:
            self.snacks[snack] = {"price": price, "quantity": quantity}
            print(f"{quantity} {snack}(s) added to inventory")

    def insert_money(self, money):

        if money in {1, 2, 3}:
            self.balance += money
            print(f"Balance: {self.balance}")
        else:
            print("Invalid amount")

    def purchase(self, snack):
        if snack in self.snacks:
            if self.snacks[snack]["quantity"] == 0:
                print(f"Sorry, {snack} is out of stock")
            elif self.balance < self.snacks[snack]["price"]:
                print(f"Insufficient balance. Price of {snack} is {self.snacks[snack]['price']}")
            else:
                self.snacks[snack]["quantity"] -= 1
                self.balance -= self.snacks[snack]["price"]
                self.total_sale += self.snacks[snack]["price"]
                print(f"Purchased {snack}")
                print(f"Balance: {self.balance:.2f}")
        else:
            print("Invalid item")

    def get_item_price(self, snack):
        if snack in self.snacks:
            return self.snacks[snack]["price"]
        else:
            print("Invalid item")

    def get_total_sales(self):
        return round(self.total_sale, 2)
    
    def remove_item(self, snack):
        if snack in self.snacks:
            del(self.snacks[snack])
            print(f"{snack} removed from inventory")
        else:
            print("Invalid item")

    def get_item_quantity(self, snack):
        if snack in self.snacks:
            return self.snacks[snack]["quantity"]
        else:
            print("Invalid item")

    def empty_inventory(self):
        snack_list = [snack for snack in self.snacks]
        for snack in snack_list:
            self.snacks.pop(snack)
        print("Inventory cleared")

    def display_change(self):
        if self.balance != 0:
            print(f"Change: {self.balance}")
            self.balance = 0
        else:
            print("No change")