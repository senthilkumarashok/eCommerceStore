from itertools import count

class Category:
    
    category_id_counter = count() # counter to generate sequential Ids for categoryId
    
    def __init__(self, category_name):
        self.category_id = next(self.category_id_counter);
        self.category_name = category_name;

class Product:
    
    product_id_counter = count() # counter to generate sequential Ids for productId
    
    def __init__(self, product_name, category_id):        
        self.product_id = next(self.product_id_counter);
        self.product_name = product_name
        self.category_id  = category_id

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            print(f"{item[0]} - {item[1]}")

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

class Store:
    
    categories = [] # Datasource for storing categories    
    products = [] # Datasource for storing products        
    
    def add_category(self, category_name):
        self.categories.append(Category(category_name))
        print(f"Category name '{category_name}' successfully added")

    def add_product(self, product_name, category_name):        
        for category in self.categories:
            if category_name == category.category_name:
                category_id = category.category_id
            
        self.products.append(Product(product_name, category_id))
        print(f"Product name '{product_name}' successfully added")


    def displayCategories(self):
        print("\nCategories")
        print("=================") 
        for category in self.categories:
            print(f"{category.category_id}. {category.category_name}")

    def displayProducts(self):
        print("\nProducts")
        print("=================") 
        for product in self.products:
            print(f"{product.product_id}. {product.product_name}") 
