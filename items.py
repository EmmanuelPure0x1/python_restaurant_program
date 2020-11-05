class Menu_Items:
    def __init__(self):
        # items dictionary created along with numerical values which represent the proce of the items.
        self.menu_items = {
            "Spaghetti Bolognese": 12,
            "Mac n Cheese": 7,
            "Stir Fry": 6,
            "Caviar": 30,
            "Jerk Chicken": 11,
            "Sea-bass": 10,
            "Fillet Mignon": 25,
            "Chicken & Chips": 7
        }

    def loopy(self):
        # looping function that prints out the available items and their price.
        for key, val in self.menu_items.items(): # selecting both key and value pair when looping.
            print(key + ':', val)