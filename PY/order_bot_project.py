import decimal 
# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat with two other friends.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you and your friends have to split the bill. 

	# Wouldn't it be great if we could automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you and your friends eat out, each of you have the option to order one or multiple items.
	# What kind of items are available to order?

	# At the end of the order, the receipt comes and you all have to calculate the cost for each person:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a specific total for each person

# -------------------------------------------- 

food = {
	"ham and cheese(no sandwich included)": 5.50,
	"strawberry lemonade": 2.50,
	"fruit salad": 3.75,
  	"tomato soup": 2.50
  }

# -------------------------------------------- 

# Part 1:
# Let's start by asking taking the order of the group(you and two friends). What did each person order?

# Write a function that will take the group's order:
# - Prompt the user to enter the price of each item they ordered
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# --------------------------------------------

totalOrder = float
def menu():
	global values
	global items
	values = food.values() 
	items = food.items()
	for key, value in items:
		print(f"{key}: $"+"{:.2f}".format(value))

def takeOrder():
	global newOrder
	global totalOrder
	global totalCost
	print("\nWelcome to Economical Eats!\nHere is the menu:\n")
	menu()
	newOrder = input(str(f"\nPlease enter what you would like to order in the following format(no additional spaces!):\n'item1,item2,item3...'\n\n"))
	totalOrder = list(newOrder.split(','))
	
# -------------------------------------------- 

# Part 2:
# Now that you have the costs of everything ordered, let's calculate the cost of each person's order(including tip and tax).

# Write a function that will calculate the cost of each person's order, including:
# - Cost of all of their ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

def tallyOrder():
	global itemNum
	global totalOrder
	global tip
	totalCost = list()
	
	# for totalOrder in food:
	# 	totalOrder.extend({values})
	if "ham and cheese" in totalOrder:
		totalCost.extend({5.50})
	if "strawberry lemonade" in totalOrder:
		totalCost.extend({2.50})
	if "fruit salad" in totalOrder:
		totalCost.extend({3.75})
	if "tomato soup" in totalOrder:
		totalCost.extend({2.50})

	totalCost = sum(totalCost)

	print("Your total cost after tax is:  $" + "{:.2f}".format(totalCost*.08875))

	# tip = input(str(f"Would you like to add a tip?\n\nOptions:\n15%\n20%\nn/a\n"))
	# if tip == "15%"
	# 	print("Your total cost after tax is:  $" + "{:.2f}".format(totalCost*.0887 + totalCost*.15))
	# if tip == "20%"
	# 	print("Your total cost after tax is:  $" + "{:.2f}".format(totalCost*.0887 + totalCost*.20))
	# if tip == "n/a"

	# print("Please come again!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""



takeOrder()
more = input(str("\nWould you like to order more?(Yes/No)\n"))	
if more.lower() == "yes":
	takeOrder()
elif more.lower() == "no":
	tallyOrder()
else:
	print("\nError.\nSorry, please come again later.")











# -------------------------------------------- 

# Part 3:
# Let's print out a receipt for each person.

# Write a function that will take the values of each person's order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Total cost for each person

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 









# -------------------------------------------- 

# Part 4: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering numbers. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Can you adjust your program to account for any shared items ordered for the group?
# - Display the tax and tip values
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
