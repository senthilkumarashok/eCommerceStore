import itertools

class CartItem:
    def __init__(self, item_name, qty, price):
        self.item_name = item_name
        self.qty = qty
        self.price = price
          
class ShoppingCart:

    def __init__(self):
        self.items = []
        self.cost = 0;

    def add_item(self, item_name, qty, price):
        self.items.append(CartItem(item_name, qty, price))
        self.cost += qty * price
        print("Added item to cart successfully !!") 
    
    def list_items(self):
        if (len(self.items) == 0): 
            print("cart is empty !!!")
        else:    
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
                print(format_row.format( header1, item.item_name, item.qty ))    

            print(format_summary)
            print(f"Total cost: {self.cost}")
            print(format_summary)
            print()

    def remove_item(self, item_name):
        for item in self.items:
            if item.item_name == item_name:
                self.items.remove(item)                
                break
        # print(f"Removed item named '{item_name}' successfully !!!")    
            
    def is_empty(self):
        return len(self.items) > 0        
            
    def checkout(self):
        self.list_items()
        print("Your order is successfully placed")
        print(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs. {self.cost}")

        
# # We can test the module separately    
# cart = ShoppingCart()
# cart.add_item("shoes", 2, 2)
# cart.add_item("shirt", 3, 3)
# # cart.add_item("shoes", 5, 5)

# cart.list_items()
# cart.checkout()

# cart.remove_item("shirt")
# cart.remove_item("shoes")

# cart.list_items()

