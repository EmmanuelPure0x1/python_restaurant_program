class Menu:
    def menu():
        # a question is posed to the client. and response is store within 'see_menu_request' variable.
        if see_menu_request == 'Y'.lower():
            # depending on response - an action is carried out.
            for item in menu_items:
                # formatted response.
                print("-", item)
            else:
                print("ok, no worries")

