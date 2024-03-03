import itertools

class Category:
    
    category_id_counter = itertools.count(start=1) # counter to generate sequential Ids for categoryId
    
    def __init__(self, category_name):
        self.category_id = next(self.category_id_counter);
        self.category_name = category_name;

class Product:
    
    product_id_counter = itertools.count(start=1) # counter to generate sequential Ids for productId
    
    def __init__(self, product_name, category_id, price):        
        self.product_id = next(self.product_id_counter);
        self.product_name = product_name
        self.category_id  = category_id
        self.price = float(price)

class Store:
        
    def __init__(self):
        self.categories = [] # Datasource for storing categories
        self.products = [] # Datasource for storing products
    
    def add_category(self, category_name):    
        self.categories.append(Category(category_name))
        # print(f"Category name '{category_name}' successfully added")

    def del_category(self, category_id):
        category_exist = False
        for category in self.categories:
            if(category_id == category.category_id):
                self.categories.remove(category)
                category_exist = True
                break
        if(category_exist is False):
            print("Category not found !!!")        
        else:            
            # print(f"Category found: {category_to_remove}")
            for product in self.products:
                if(category_id == product.category_id):
                    self.products.remove(product)

    def add_categories(self, categories):
        for category_name in categories:
            self.add_category(category_name)            

    def add_product(self, product_name, category_id, price):
        category_name = self.get_category_name(category_id)
        if category_name is None:
            print("Category not found !!!")
        else:    
            self.products.append(Product(product_name, category_id, price))
        # print(f"Product name '{product_name}' successfully added")

    def del_product(self, product_id):
        isProductExist = False
        for product in self.products:
            # print(f" product id is {product_id} == {product.product_id}")
            if(product_id == product.product_id):
                self.products.remove(product)
                # print(" Removing product")
                isProductExist = True
                break

        if isProductExist is False:
            print(f"Product with id:{product_id} does not exist")        

    def listCategories(self):
        headers = ["CategoryId", "CategoryName"];
        format_row = "{:<10}  {:<10}"
        headerFormat = format_row.format(headers[0], headers[1])

        format_summary = "".join(itertools.repeat("-",len(headerFormat)))
        print(format_summary)
        print("View Categories")
        print(format_summary)
                
        
        print(headerFormat)        
        print(format_row.format( "__________", "____________"))        
        for category in self.categories:
            header1 = "{}.".format(category.category_id)
            print(format_row.format( header1, category.category_name))

        print(format_summary)
        print()    

    def listProducts(self):
        headers = ["productNo", "Name", "Category", "Price"];
        format_row = "{:<10}   {:<10}   {:<10}   {:<10}" 
        headerFormat = format_row.format(headers[0], headers[1], headers[2], headers[3])      

        format_summary = "".join(itertools.repeat("-",len(headerFormat)))
        print(format_summary)
        print("View Products")
        print(format_summary)

        print(headerFormat)
        print(format_row.format( "==========","=======", "============", "======"))
        for product in self.products:
            header1 = "{}.".format(product.product_id)
            header2 = self.get_category_name(product.category_id)
            header3 = "{}$".format(product.price)
            print(format_row.format(header1,  product.product_name, header2, header3)) 

        print(format_summary)
        print() 

    def get_category_name(self, category_id):
        categoryName = ""
        for category in self.categories:
            if category_id == category.category_id:
                categoryName = category.category_name
                break
        return categoryName    
                
# Initializing a store 
store = Store()

# Adding categories
store.add_categories(["footwear", "clothing", "electronics"])

# View categories
store.listCategories()

# Adding products
store.add_product("shoes", 1, 19)
store.add_product("shirt", 2, 12)
store.add_product("camera", 3, 11)

# View products
store.listProducts()

# Delete category
store.del_category(1)
store.del_product(3)

# View Products and Categories after deleting category
store.listCategories()
store.listProducts()
