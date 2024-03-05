"""Module providing a function"""
import itertools
import dataclasses

@dataclasses.dataclass
class CartItem:
    """Class representing a CartItem"""
    def __init__(self, item_name, qty, price):
        self.item_name = item_name
        self.qty = qty
        self.price = price


class ShoppingCart:
    """Class representing a ShoppingCart"""
    def __init__(self):
        self._items = []
        self.cost = 0

    def add_item(self, item_name, qty, price):
        """Function for adding items in the cart."""
        self._items.append(CartItem(item_name, qty, price))
        self.cost += qty * price
        print("Added item to cart successfully !!", len(self._items))

    def list_items_in_cart(self):
        """Function for displaying items in the cart."""
        if len(self._items) == 0:
            print("cart is empty !!!")
        else:
            headers = ["ItemNo", "ItemName", "Qty"]
            format_row = "{:<8}  {:<10}  {:<10}"
            header_format = format_row.format(headers[0], headers[1], headers[2])

            format_summary = "".join(itertools.repeat("-", len(header_format)))

            print(format_summary)
            print("Cart Summary")
            print(format_summary)

            print(header_format)
            print(format_row.format("=======", "==========", "======"))

            for idx, item in enumerate(self._items):
                header1 = f"{idx + 1}."
                print(format_row.format(header1, item.item_name, item.qty))

            print(format_summary)
            print(f"Total cost: {self.cost}")
            print(format_summary)
            print()

    def remove_item(self, item_name):
        """Function for removing items in the cart."""
        for item in self._items:
            if item.item_name == item_name:
                print(f"Removing item {item_name}")
                self._items.remove(item)
                break
        # print(f"Removed item named '{item_name}' successfully !!!")

    def is_empty(self):
        """Function to check whether cart is empty."""
        return len(self._items) > 0

    def checkout(self):
        """Function to checkout once cart is ready."""
        print("Your order is successfully placed")
        print(f"You will be shortly redirected to the portal \
              for Unified Payment Interface to make a \
              payment of Rs. {self.cost}"
        )


# # We can test the module separately
# cart = ShoppingCart()
# cart.add_item("shoes", 2, 2)
# cart.add_item("shirt", 3, 3)
# # cart.add_item("shoes", 5, 5)

# cart.list_items_in_cart()
# cart.checkout()

# cart.remove_item("shirt")
# cart.remove_item("shoes")

# cart.list_items_in_cart()
