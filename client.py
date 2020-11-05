from items import Menu_Items

class Client_Order(Menu_Items):
    def __init__(self):
        super().__init__()

    # The function below will gather user input and save in a variable which can be used later.
    def see_menu(self):

        # View_menu variable asks the user if they want to see the menu.
        view_menu = input("Do you want to see the menu? Y/N > ")

        # Input is evaluated against the expected response and flow is controlled.
        if view_menu[0].lower() == "y":
            self.loopy()

        elif view_menu[0].lower() == "n":
            print("Well get out then....")


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

if __name__ == "__main__":
    eman = Client_Order()
    eman.see_menu()
    print(eman.choose_items())