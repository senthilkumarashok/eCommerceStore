from core_module import Store
from shopping_cart import ShoppingCart
from login_service import LoginService

isAppRunning=True

print("Welcome to the Demo Marketplace")

role = 0
is_authenticated = False

# Initializing a store 
demoStore = Store()

# Initialize a cart for customer
shoppingCart = ShoppingCart()

def login():
	global role
	print()
	role = int(input("Select your role: [Admin = 1, Customer = 2]"))
	if(role == 1):
		adminLogin()
	elif(role == 2):
		customerLogin()	
	else:
		print("Invalid selection !!")	

def is_admin():
	return role == 1

def is_customer():
	return role == 2
	
#Admin login
def adminLogin():
	user_name = input("Enter admin username: ")
	password = input("Enter admin password: ")
	global is_authenticated
	is_authenticated = LoginService.adminLogin(user_name, password)	

#Customer login
def customerLogin():
	user_name = input("Enter username: ")
	password = input("Enter password: ")
	global is_authenticated
	is_authenticated = LoginService.userLogin(user_name, password)
	
def printInstructions():
	print()
	global role
	print("Type 'A' to view categories")	
	print("Type 'B' to view products")
	if is_admin():		
		print("Type 'C' to add categories")
		print("Type 'D' to delete a category")		
		print("Type 'E' to add products")
		print("Type 'F' to delete product")
	elif is_customer():
		print("Type 'G' to add items to your cart")
		print("Type 'H' to view items in your cart")
		print("Type 'I' to remove items in your cart")
		if shoppingCart.is_empty():
			print("Type 'J' to checkout")
	else:
		print("Invalid role: ", role)	
	print("Type 'X' to exit")
	print()
	
# def loginPrompt(is_admin_user):
# 	username = input("Enter username: ")
# 	password = input("Enter password: ")
	# if(is_admin_user):
    #     LoginService.adminLogin(username, password)
	# else:
	# 	LoginService.userLogin(username, password)

def remove_item_from_cart():
	item_idx = input("Type a cart object ID to remove")
	shoppingCart.remove_item(item_idx)

def add_item_to_cart():
	item_id = int(input("Enter itemNo to add: "))
	qty = int(input("Enter the qty to buy: "))
	product = demoStore.get_product_by_id(item_id)
	if(product is None):
		print("Product does not exist")
	else:
		print(f"{product.product_name}, {qty}, {product.price}")
		shoppingCart.add_item(product.product_name, qty, product.price)		

def add_category():  
    category_name = input("Enter category name: ")
    demoStore.add_category(category_name)

def remove_category():  
    category_id = int(input("Enter category id to remove: "))
    demoStore.del_category(category_id)

def add_product():
	product_name = input("Enter product name: ")
	category_id = int(input("Enter category id: "))
	category_name = demoStore.get_category_name(category_id)
	if(category_name is None):
		print("category does not exist. please create category before adding the product")
	else:	
		price = float(input("Enter price : "))
		demoStore.add_product(product_name, category_id, price)

def remove_product():
	product_id = int(input("Enter product id to remove: "))
	demoStore.del_product(product_id)
	
def handleInput(in_var):
	char_inputs = ["A","B","C","D","E","F","G","H","I","J"]
	print()
	if(in_var == "A"):
		demoStore.listCategories()
	if(in_var == "B"):
		demoStore.listProducts()		
	if(in_var == "C"):
		add_category()			
	if(in_var == "D"):
		remove_category()
	if(in_var == "E"):
		add_product()		
	if(in_var == "F"):
		remove_product()			
	if(in_var == "G"):
		add_item_to_cart()	
	if(in_var == "H"):
		shoppingCart.list_items_in_cart()	
	if(in_var == "I"):
		shoppingCart.remove_item_from_cart()
	if(in_var == "J"):
		shoppingCart.checkout()
	if(in_var == "X"):
		global isAppRunning
		print("Thanks for visiting the Demo Marketplace")
		isAppRunning = False
	# if in_var not in char_inputs:
	# 	try:
	# 		add_to_cart(cart)
	# 	except:
	# 		print("you have entered an illegal character!")


# Adding categories
demoStore.add_categories(["footwear", "clothing", "electronics"])

# Adding products
demoStore.add_product("shoes", 1, 19)
demoStore.add_product("shirt", 2, 12)
demoStore.add_product("camera", 3, 11)


while(isAppRunning):	
	if is_authenticated:
		printInstructions()
		input_var = input("choose one of the option :")
		
		handleInput(input_var)
	else: 
		login()	