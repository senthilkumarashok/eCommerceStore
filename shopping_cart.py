import itertools

class ShoppingCart:

    def __init__(self):
        self.items = []
        self.cost = 0;

    def add_item(self, item_name, qty, price):
        self.items.append((item_name, qty, price))
        self.cost += qty * price
        # print("Added to cart successfully")

    def list_items(self):
        headers = ["ItemNo", "ItemName", "Qty"]
        format_row = "{:<8}  {:<10}  {:<10}"
        headerFormat = format_row.format(headers[0], headers[1], headers[2])

        format_summary = "".join(itertools.repeat("-",len(headerFormat)))

        print(format_summary)
        print("Cart Summary")
        print(format_summary)
        
        print(headerFormat)
        print(format_row.format( "=======", "==========", "======"))
        for idx, item in enumerate(self.items):
            header1 = "{}.".format(idx+1)
            print(format_row.format( header1, item[0], item[1] ))    

        print(format_summary)
        print(f"Total cost: {self.cost}")
        print(format_summary)
        print()

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)                
                break
        # print(f"Removed item named '{item_name}' successfully !!!")    
        
    
cart = ShoppingCart()
cart.add_item("shoes", 2, 2)
cart.add_item("shirt", 3, 3)
cart.add_item("shoes", 4, 4)
cart.add_item("shoes", 5, 5)

cart.remove_item("shirt")

cart.list_items()
