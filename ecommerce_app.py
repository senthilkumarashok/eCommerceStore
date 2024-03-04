from core_module import Store
import shopping_cart
from login_service import LoginService

isAppRunning=True

print("Welcome to the Demo Marketplace")

role=0

def login():
	role = int(input("Select your role: [Admin = 1, Customer = 2]"))
	if(role == 1):
		adminLogin()
	elif(role == 2):
		customerLogin()	
	else:
		print("Invalid selection !!")	
	
#Admin login
def adminLogin():
	user_name = input("Enter admin username: ")
	password = input("Enter admin password: ")
	is_authenticated = LoginService.adminLogin(user_name, password)
	if is_authenticated:
		printInstructions()	

#Customer login
def customerLogin():
	user_name = input("Enter username: ")
	password = input("Enter password: ")
	is_authenticated = LoginService.userLogin(user_name, password)
	if is_authenticated:
		printInstructions()	

def printInstructions():
	print()
	global role
	if role == 1:
		print("Type 'A' to view categories")	
		print("Type 'B' to add categories")
		print("Type 'C' to delete a category")
		print("Type 'D' to view products")	
		print("Type 'E' to add products")
		print("Type 'F' to delete product")
	elif role == 2:
		print("Type 'G' to add Items to your cart")
		print("Type 'H' to view items in your cart")
		print("Type 'I' to remove items in your cart")	
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

def add_item_to_cart(cart, store):
	item_id = int(input("Enter itemNo to add: "))
	qty = int(input("Enter the qty to buy: "))
	product = store.get_product_by_id(item_id)
	if(product is None):
		print("Product does not exist")
	else: 	
		cart.add_item(product.product_name, qty, product.price)

def add_category(store):  
    category_name = input("Enter category name: ")
    store.add_category(category_name)

def remove_category(store):  
    category_id = int(input("Enter category id to remove: "))
    store.del_category(category_id)

def add_product(store):
	product_name = input("Enter product id: ")
	category_id = int(input("Enter category id: "))
	category_name = store.get_category_name(category_id)
	if(category_name is None):
		print("category does not exist. please create category before adding the product")
	else:	
		price = float(input("Enter price : "))
		store.add_product(product_name, category_id, price)

def remove_product(store):
	product_id = int(input("Enter product id to remove: "))
	store.del_product(product_id)
	
def handleInput(in_var, cart, store):
	char_inputs = ["A","B","C","D","E","F","G","H","I"]
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
	if(in_var == "G"):
		add_item_to_cart(cart, store)	
	if(in_var == "H"):
		cart.list_items()	
	if(in_var == "I"):
		remove_item_from_cart(cart)
	if(in_var == "X"):
		global isAppRunning
		print("Thanks for visiting the Demo Marketplace")
		isAppRunning = False
	# if in_var not in char_inputs:
	# 	try:
	# 		add_to_cart(cart)
	# 	except:
	# 		print("you have entered an illegal character!")

# Initializing a store 
demoStore = Store()

# Adding categories
demoStore.add_categories(["footwear", "clothing", "electronics"])

# Adding products
demoStore.add_product("shoes", 1, 19)
demoStore.add_product("shirt", 2, 12)
demoStore.add_product("camera", 3, 11)

login()

while(isAppRunning):		
	# printInstructions()
	input_var = input("choose one of the option :")
	shoppingCart = shopping_cart.ShoppingCart()
	handleInput(input_var, shoppingCart, demoStore)
