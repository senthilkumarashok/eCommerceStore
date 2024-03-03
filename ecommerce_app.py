from core_module import Store
import shopping_cart
from login_service import LoginService

isAppRunning=True

print("Welcome to the Demo Marketplace")

def printInstructions():
	print()
	print("Type 'A' to view categories")	
	print("Type 'B' to add categories")
	print("Type 'C' to delete a category")
	print("Type 'D' to view products")	
	print("Type 'E' to add products")
	print("Type 'F' to delete product")
	
	print("Type 'S' to view your cart items")
	print("Type 'R' to remove an item from your cart")
	print("Type an item number to buy it")	
	print("Type X to exit")	
	
# def loginPrompt(is_admin_user):
# 	username = input("Enter username: ")
# 	password = input("Enter password: ")
	# if(is_admin_user):
    #     LoginService.adminLogin(username, password)
	# else:
	# 	LoginService.userLogin(username, password)

def remove_item_from_cart(cart):
	item_idx = input("Type a cart object ID to remove")
	cart.remove_item(item_idx)

def add_to_cart(cart):
	item_id = input("Enter productNo to add: ")
	qty = input("Enter the qty to buy: ")
	cart.add_items(item_id, qty)

def add_category(store):  
    category_name = input("Enter category name: ")
    store.add_category(category_name)

def remove_category(store):  
    category_id = int(input("Enter category id to remove: "))
    store.del_category(category_id)

def add_product(store):
	product_name = input("Enter product name: ")
	category_id = int(input("Enter category id: "))
	price = float(input("Enter price : "))
	store.add_product(product_name, category_id, price)

def remove_product(store):
	product_id = input("Enter product id to remove: ")
	store.del_product(product_id)
	
def handleInput(in_var, cart, store):
	char_inputs = ["A","B","C","D","E","F"]
	print()
	if(in_var == "A"):
		store.listCategories()
	if(in_var == "B"):
		add_category(store)		
	if(in_var == "C"):
		remove_category(store)
	if(in_var == "D"):
		store.listProducts()		
	if(in_var == "E"):
		add_product(store)		
	if(in_var == "F"):
		remove_product(store)			
	if(in_var == "T"):
		add_category(store)	
	if(in_var == "S"):
		cart.list_items()	
	if(in_var == "R"):
		remove_item_from_cart(cart)
	if(in_var == "X"):
		global isAppRunning
		isAppRunning = False
	# if in_var not in char_inputs:
	# 	try:
	# 		add_to_cart(cart)
	# 	except:
	# 		print("you have entered an illegal character!")

# Initializing a store 
store = Store()

# Adding categories
store.add_categories(["footwear", "clothing", "electronics"])

# Adding products
store.add_product("shoes", 1, 19)
store.add_product("shirt", 2, 12)
store.add_product("camera", 3, 11)

while(isAppRunning):	
	printInstructions()
	input_var = input("choose an item to buy(type the id)")
	shoppingCart = shopping_cart.ShoppingCart()
	handleInput(input_var, shoppingCart, store)
