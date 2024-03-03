from itertools import count

class Category:
    
    category_id_counter = count(start=1) # counter to generate sequential Ids for categoryId
    
    def __init__(self, category_name):
        self.category_id = next(self.category_id_counter);
        self.category_name = category_name;

class Product:
    
    product_id_counter = count(start=1) # counter to generate sequential Ids for productId
    
    def __init__(self, product_name, category_id, price):        
        self.product_id = next(self.product_id_counter);
        self.product_name = product_name
        self.category_id  = category_id
        self.price = price

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def list_items(self):
        for item in self.items:
            print(f"{item[0]} - {item[1]}")

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

class Store:
        
    def __init__(self):
        self.categories = [] # Datasource for storing categories
        self.products = [] # Datasource for storing products
    
    def add_category(self, category_name):
        self.categories.append(Category(category_name))
        # print(f"Category name '{category_name}' successfully added")

    def add_categories(self, categories):
        for category_name in categories:
            self.add_category(category_name)            

    def add_product(self, product_name, category_name, price):        
        for category in self.categories:
            if category_name == category.category_name:
                category_id = category.category_id
            
        self.products.append(Product(product_name, category_id, price))
        # print(f"Product name '{product_name}' successfully added")


    def listCategories(self):        
        format_row = "{:<10}  {:<10}"       
        print(format_row.format( "CategoryId", "CategoryName"))
        print(format_row.format( "==========", "============"))
        for category in self.categories:
            header1 = "{}.".format(category.category_id)
            print(format_row.format( header1, category.category_name))

    def listProducts(self):
        format_row = "{:<10}  {:<10}  {:<10}"       
        print(format_row.format( "productNo", "Name", "Price"))
        print(format_row.format( "==========","====", "======"))
        for product in self.products:
            header1 = "{}.".format(product.product_id)
            print(format_row.format(header1,  product.product_name, product.price)) 
