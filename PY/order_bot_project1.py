#### note -- currently, choosing to add_order overwrites the original total_order instead of adding to it.




# function menu: collects from dictionarys and prints the information in menu format
def menu():
    print("---------------------------------------------\nMENU--")
    for item, price in consumables.items():
        print(f"{item}: $"+"{:.2f}".format(price))
    print("Note: please add to your consideration that the child is farm-raised and gluten-free")
    print("---------------------------------------------\n")
# function take_order: creates a new order from customer and adds it into a list called total		
def take_order():
    global total_order
    global new_order
    print("\nWelcome to Economical Eats!\nHere is the menu:\n")
    menu() 
    new_order = input(str(f"\nPlease enter what you would like to order in the following format(no additional spaces!):\n'item1+item2+item3...'\n\n"))
    new_order = new_order.strip(" ").lower()
    total_order =  list(new_order.split('+'))
#function add_tip to ask user whether or not they wish to tip
def add_tip():
    global tip
    points = 0
    print("---------------------------------------------\n")
    print("\nAlso........\n...Leave a tip?")
    choice = input(str("Pick from the following presets.\n10%\n15%\n20%\nNo tip :(\n\n"))
    if choice == "10%":
        tip = 1.1
    elif choice == "15%":
        tip = 1.15
    elif choice == "20%":
        tip = 1.2
    elif choice in ["no tip :(", "No tip :(","no tip","No tip","no", "No", ":("]:
        tip = 1.0
    else:
        print("Please make a choice.")
        add_tip()
        points += 1
        if points == 5:
            print("An error occurred. Please try again?")
            try_again = input(str("(Y/N)\n"))
            if try_again in ["Y","y"]:
                take_order()
            elif try_again in ["N","n"]:
                print("Goodbye.")
    
# function tally_receipt: counts up cost behind the scenes and then creates the receipt.
def tally_receipt():
    print("---------------------------------------------\nRECEIPT--")
    total_cost = 0.00
    for x in range (0, len(total_order)):
        tally = consumables.get(total_order[x])
        print(f"\n{total_order[x]} == {tally}")
        total_cost += tally
    print(f"\n\nYour total cost (plus tax) is: $" + "{:.2f}".format(total_cost*1.08875*tip)) 
    print("Thank you for dining with us :)")
    print("---------------------------------------------\n")

# function add_order: allows to add more to original order.

def add_order():
    more = input(str("\nWould you like to order more?(y/n)\n"))	
    if more.lower() == "y":
        take_order()


# Call the functions
# dictionaries; holding the information that will be displayed on the menu; the information is also used to create customer's order and total.
consumables = {
    "water": 0.00,
    "butterbeer": 2.49,
    "honey and milk": 1.50,
    "raspberry and mint lemonade": 2.25,
    "saiko soda pop": 1.50,
    "dubious food": 0.99,
    "rock-hard food": 1.10,
    "tomato and basil soup": 3.75,
    "meat skewers": 4.50,
    "spicy curry on rice": 4.25,
    "sad meal": 2.49,
    "a small child": 9.90
}


take_order()
add_order()
add_tip()
tally_receipt()
