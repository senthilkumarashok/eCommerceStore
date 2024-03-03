import core_module
from login_service import LoginService

print("\nWelcome to the Demo Marketplace\n")

# Initializing a store 
store = core_module.Store()

# Adding categories
store.add_category("footwear")
store.add_category("clothing")
store.add_category("electronics")
store.displayCategories()

print()
# # Adding products
store.add_product("shoes", "footwear")
store.add_product("shirt", "clothing")
store.add_product("camera", "electronics")

store.displayProducts()

LoginService.userLogin('senkumar', 'password2')
LoginService.userLogin('user1', 'password2')
LoginService.adminLogin('senkumar', 'password')
LoginService.adminLogin('admin1', 'password1')
