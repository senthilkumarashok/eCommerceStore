from core_module import Store,ShoppingCart
from login_service import LoginService

isAppRunning=True

print("Welcome to the Demo Marketplace")

def printInstructions():
	print()
	print("Type C to view categories")	
	print("Type V to view products")	
	print("Type T to add category")
	print("Type S to view your cart items")
	print("Type R to remove an item from your cart")
	print("Type an item number to buy it")
	print("Type P to get the total cart price")
	print("Type X to exit")	
	
# def loginPrompt(is_admin_user):
# 	username = input("Enter username: ")
# 	password = input("Enter password: ")
	# if(is_admin_user):
    #     LoginService.adminLogin(username, password)
	# else:
	# 	LoginService.userLogin(username, password)

def remove_item_from_cart(cart):
	itemIndex = input("Type a cart object ID to remove")
	cart.remove_item(itemIndex)

def add_to_cart(cart):
	itemId = input("Enter productNo to add: ")
	qty = input("Enter the qty to buy: ")
	cart.add_items(itemId, qty)

def add_category(store):  
    categoryName = input("Enter category name: ")
    store.add_category(categoryName)	
	
def handleInput(in_var, cart, store):
	char_inputs = ["C","R","P","X","L"]
	print()
	if(in_var == "C"):
		store.listCategories()
	if(in_var == "T"):
		add_category(store)
	if(in_var == "V"):
		store.listProducts()
	if(in_var == "S"):
		cart.list_items()	
	if(in_var == "R"):
		remove_item_from_cart(cart)
	if(in_var == "P"):
		print("your cart currently cost : ", cart.list_cart_price())		
	if(in_var == "X"):
		global isAppRunning
		isAppRunning = False
	if in_var not in char_inputs:
		try:
			add_to_cart(cart)
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
