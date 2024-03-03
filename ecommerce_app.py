from core_module import Store,ShoppingCart
from login_service import LoginService

isAppRunning=True

print("Welcome to the Demo Marketplace")

def printInstructions():
	print()
	print("Type S to view your cart items")
	print("Type R to item from your cart")
	print("Type an item number to buy it")
	# print("Type P to get the total cart price")
	print("Type X to exit")
	
def loginPrompt(is_admin_user):
	username = input("Enter username: ")
	password = input("Enter password: ")
	# if(is_admin_user):
    #     LoginService.adminLogin(username, password)
	# else:
	# 	LoginService.userLogin(username, password)

def handleInput(in_var, cart, store):
	char_inputs = ["C","R","P","X","L"]
	print()
	if(in_var == "C"):
		store.listCategories()
	if(in_var == "L"):
		store.listProducts()
	if(in_var == "S"):
		cart.list_items()	
	if(in_var == "R"):
		cart.list_items()
	if(in_var == "X"):
		global isAppRunning
		isAppRunning = False
	if in_var not in char_inputs:
		try:
			cart.addToCart(store[int(in_var)])
		except:
			print("you have entered an illegal character!")

# Initializing a store 
store = Store()

# Adding categories
store.add_categories(["footwear", "clothing", "electronics"])

# # Adding products
store.add_product("shoes", "footwear", 19)
store.add_product("shirt", "clothing", 12)
store.add_product("camera", "electronics", 11)

while(isAppRunning):	
	printInstructions()
	input_var = input("choose an item to buy(type the id)")
	shoppingCart = ShoppingCart()
	handleInput(input_var, shoppingCart, store)
