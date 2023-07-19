items = []
new_item = ""
item_prices = []
new_price = ""
total = 0

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime
current_date_and_time = datetime.now()

def main():
    

    print ("Welcome to Shopping Calculator")
    print ()
    print ("This program will help you visualize the items you want to buy in an online store.")
    print ("You will need to add the item and its price. When you finish it, this program can compute")
    print ("the total amount of money for those products. Also, you have the option the remove an item")
    print ("if you change your mind about a product or if you enter the wrong price or name.")
    print ()
    print ("YOU CAN USE THIS PROGRAM IN ANY SITUATION. NOT ONLY FOR AN ONLINE STORE.")
    print ()
    menu_option =""
    while menu_option != "5":

        print ("Please select one of the following: ")
        print ("1. Add item")
        print ("2. View cart")
        print ("3. Remove item")
        print ("4. Compute total")
        print ("5. Quit")
        menu_option = input ("Please enter an action: ")

        if menu_option == "1":
            
            new_item = str(input ("What item would you like to add? "))
            
            try:
                new_price = float (input(f"What is the price of {new_item.capitalize()}? "))
                print (f"{new_item.capitalize()} has been added to the chart.")
                append_item_and_price(new_item, new_price)
            
            except ValueError as val_err:
                print(val_err)
            print()

        elif menu_option == "2":

            print ("The contents of the shopping cart are:")
            show_item_and_price(items, item_prices)

        elif menu_option == "3":
            try:
                item_removed = int(input ("Which item would you like to remove? "))
                remove_item_and_price(item_removed)

            except ValueError as val_err:
                print("Error: you entered text that is not an integer.")
            print()

        elif menu_option == "4":

            compute_total(item_prices)
            
          
        elif menu_option == "5":

            print ("Thank you for using the Shopping Calculator. Goodbye.")
            print (f"{current_date_and_time:%x}")
            print ()

        else:
            print ("You need to select one of the numbers in the list. Try it again ¡")
            print ()


def append_item_and_price(new_item, new_price):
    """This function appends the user item to the items list
    and appends the user item price to the item_prices list.
    Parameters:
        new_item is the name of the item enter by the user.
        new_price is the price for that item enter by the user.
    Return new_item and new_price"""
    items.append(new_item)
    item_prices.append(new_price)
    print ()
    return new_item and new_price


def show_item_and_price(items, item_prices):
    """This function shows the item enter by the user next to its price.
    Parameters:
        items list with the items enter by the user.
        item_prices list with the values enter by the user.
    Return new_price and new_item """
    try:
        for i in range(len(items)):

            new_item = items[i]
            new_price = item_prices[i]
            print(f"{i+1}. {new_item.capitalize()} - ${new_price:.2f}")
        print ()
        return new_price and new_item

    except UnboundLocalError as unbound_err:
        print("Error: You need to add an item and its price first.")
        print("Please select option 1. Add item")
    print()


def remove_item_and_price(item_removed):
    """This functions removes any item and its price enter by the user.
    Parameters:
        item_removed is the index in which the item and its price are placed.
    Return the item_removed enter by the user."""
    try:
        item_removed = items.pop(item_removed-1) and item_prices.pop(item_removed-1)
        print ("Item removed.")
        print ()
        return item_removed

    except IndexError as index_err:
        print(index_err)
    

def compute_total(item_prices):
    """This function sum the total elements in the item_prices list which
    contains all the prices enter bt the user.
    Parameters:
        The item_prices list that contains the numbers to do this calculation.
    Return the total amount of money that each item has."""
    total = 0

    for price in item_prices:

        total += price
    
    print (f"The total price of the items in the Shopping Calculator is ${total:.2f}")
    print ()
    return total 
    

if __name__ == "__main__":
    main()