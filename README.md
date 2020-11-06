# Lists - Restaurant Waiter Helper program

## Task

Complete the ```User stories``` below. 

### User Stories
Task: 1
* As a user, I want to be able to see the menu in a formatted way, so that I can order my meal.
```python
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
        # Iterating over dictionary which prints out the items and their price.
        for key, val in self.menu_items.items(): # selecting both key and value pair when looping.
            print(key + ':', val)
```

Task: 2
* As a user, I want to be able to order 3 items, and have my responses added to a list so they aren't forgotten.
```python
    def choose_items(self):
        # empty list which will fill up when the user choose items of the menu.
        client_choice = []

        # while loops looks at the amount of items in the dictionary and while the condition isn't meant.
        # It will keep asking for the user to choose an item.

        while len(client_choice) < 3:
            # variable created for the user's choice
            choice = input("choose an item... > ")

            # if function checks to see that what has been typed/selected is in the list. if is it will append it to the client choice list.
            if choice in self.menu_items.keys():
                client_choice.append(choice)
        return client_choice
```

Task: 3
* As a user, I want to have my order read back to me in formatted way so I know what I ordered.

```python
 # Iterating over the Clients choices
        for i in client_choice:
            print("\n- The client has chosen: " + i)

        # List of the items the waiter will need to provide
        print("\nThese are the orders you will need to get for the client:")
        return client_choice
```
