
try:
    import string

    alphabet = string.ascii_uppercase
except ImportError:
    pass


class FoodMenu:
    """UI for Pizza Menu"""

    def restaurant_menu(self, menu_type):
        print(f"""
        +-------------------------------------------+
        |              Pizza Shed |
        +---------------------------------+---------+""")
        for (index, (food, price)) in enumerate(menu_type):
            print("""\
        | {letter}\t {food} | £{price} |
        +---------------------------------+---------+
        """.format(letter=alphabet[index], food=food, price=price))


class Program(FoodMenu):

    def __init__(self, table):
        self.table = table
        self.total = 0.00
        self.vat = 0.05
        self.sides_req = 'N/A'
        self.comment = 'N/A'

        self.pizza = [
            ("Cheese and Tuna Melt", 6.99),
            ("Tandoori Chicken Supreme", 7.99),
            ("Vegetarian Supreme", 5.99),
            ("Beef Sizzler", 9.99),
            ("Seafood Special", 8.99)
        ]
        self.crust_base = [
            ("Thin", 0.00),
            ("Thick", 0.00)
        ]
        self.drinks = [
            ("Tap Water", 0.00),
            ("Bottled Water", 0.70),
            ("Pepsi", 1.50),
            ("Tango", 1.00)
        ]

        self.sides = [
            ("Garlic Bread", 0.50),
            ("Colesaw", 0.50),
            ("3 Dips", 0.50),
        ]

        self.item_list = []
        self.item_qty = []
        self.item_price_list = []
        self.item_index_pizza = []
        self.item_index_sides = []
        self.item_index_drinks = []

    def get_table(self):
        return self.table

    def order(self):
        self.restaurant_menu(self.pizza)

        is_ok = True
        while is_ok:
            __display = ''

            if self.total == 0.00:
                pass
            else:
                __display = f'Total bill: £{format(self.total, ",.2f")}'

            print(__display)
            pizza_chosen = input("Select a letter or 'a' to proceed: ")

            if pizza_chosen in self.item_index_pizza:
                print('You have already selected this item.')
                print('Please select another item')
                continue

            elif pizza_chosen in alphabet[:len(self.pizza)]:
                index = pizza_chosen
                self.item_index_pizza.extend(index)
                print(f'Pizza Chosen: {self.pizza[alphabet.index(pizza_chosen)][0]}')  # get food item
                print(f'Price: {self.pizza[alphabet.index(pizza_chosen)][1]}')  # get cost item

                get_pizza = [self.pizza[alphabet.index(pizza_chosen)][0]]  # Stores pizza into lists
                self.item_list.extend(get_pizza)  # Appending to list

                pizza_qty = float(input("Enter Quantity: "))
                get_pizza_cost = [self.pizza[alphabet.index(pizza_chosen)][1]]  # Stores pizza price into lists
                self.item_price_list.extend(get_pizza_cost)

                while pizza_qty > 10:
                    print("You may only order up to 10 items for this product")
                    break
                else:
                    get_pizza_qty = str(pizza_qty)
                    self.item_qty.append(get_pizza_qty)

                    self.total += self.pizza[alphabet.index(pizza_chosen)][1] * pizza_qty

                    # multiply food with qty

            elif pizza_chosen == 'a' and self.total != 0.00:

                # self.crust_base(crust_base)
                self.pizza_type()

                break
            # Some kind of message if the input is invalid
            # is good practice
            else:
                print("Invalid Input. Please choose at least one item from the menu")

    def pizza_type(self):
        valid = True
        while valid:
            self.restaurant_menu(self.crust_base)
            crust_chosen = input("Select a crust base: ")
            if crust_chosen in alphabet[:len(self.crust_base)]:

                print(f'Crust Chosen: {self.crust_base[alphabet.index(crust_chosen)][0]}')  # get food item
                get_crust = [self.crust_base[alphabet.index(crust_chosen)][0]]  # Stores pizza into lists

                self.item_list.extend(get_crust)  # Appending to list
                get_crust_qty = str(1)
                self.item_qty.append(get_crust_qty)
                self.choose_sides()  # Navigate to sides
                valid = False
            else:
                print("Invalid Input. Please choose at least one item from the menu")

    def choose_sides(self):

        answer = input("Would you like extra sides?")
        if answer == "Y" or answer == "y":
            self.restaurant_menu(self.sides)

            is_ok = True
            while is_ok:

                print(f'Total bill: £{format(self.total, ",.2f")}')
                sides_chosen = input("Select a letter or 'a' to proceed: ")

                if sides_chosen in self.item_index_sides:
                    print('You have already selected this item.')
                    print('Please select another item')
                    continue

                elif sides_chosen in alphabet[:len(self.sides)]:
                    index_2 = sides_chosen
                    self.item_index_sides.extend(index_2)
                    print(self.item_index_sides)
                    print(f'Sides Chosen: {self.sides[alphabet.index(sides_chosen)][0]}')  # get food item
                    print(f'Price: {self.sides[alphabet.index(sides_chosen)][1]}')  # get cost item

                    get_sides = [self.sides[alphabet.index(sides_chosen)][0]]  # Stores pizza into lists
                    self.item_list.extend(get_sides)  # Appending to list

                    sides_qty = float(input("Enter Quantity: "))
                    get_sides_cost = [self.sides[alphabet.index(sides_chosen)][1]]  # Stores pizza price into lists
                    self.item_price_list.extend(get_sides_cost)

                    while sides_qty > 10:
                        print("You may only order up to 10 items for this product")
                        sides_qty = float(input("Enter Quantity: "))
                        break
                    else:
                        get_sides_qty = str(sides_qty)
                        self.item_qty.append(get_sides_qty)

                        self.total += self.sides[alphabet.index(sides_chosen)][1] * sides_qty

                        # multiply food with qty

                elif sides_chosen == 'a' and self.item_index_sides != []:

                    self.choose_drinks()
                    #                    self.choose_drinks()

                    break
                # Some kind of message if the input is invalid
                # is good practice
                else:
                    print("Invalid Input. Please choose at least one item from the menu")
        else:
            self.choose_drinks()

    def choose_drinks(self):
        self.restaurant_menu(self.drinks)

        is_ok = True
        while is_ok:

            print(f'Total bill: £{format(self.total, ",.2f")}')
            drink_chosen = input("Select a letter or 'a' to proceed: ")

            if drink_chosen in self.item_index_drinks:
                print('You have already selected this item.')
                print('Please select another item')
                continue

            elif drink_chosen in alphabet[:len(self.drinks)]:
                index3 = drink_chosen
                self.item_index_drinks.extend(index3)
                print(self.item_index_drinks)
                print(f'Drink Chosen: {self.drinks[alphabet.index(drink_chosen)][0]}')  # get food item
                print(f'Price: {self.drinks[alphabet.index(drink_chosen)][1]}')  # get cost item

                get_pizza = [self.drinks[alphabet.index(drink_chosen)][0]]  # Stores pizza into lists
                self.item_list.extend(get_pizza)  # Appending to list

                drink_qty = float(input("Enter Quantity: "))
                get_drink_cost = [self.drinks[alphabet.index(drink_chosen)][1]]  # Stores pizza price into lists
                self.item_price_list.extend(get_drink_cost)

                while drink_qty > 11:
                    print("You may only order up to 10 items for this product")
                    break
                else:
                    get_drink_qty = str(drink_qty)
                    self.item_qty.append(get_drink_qty)

                    self.total += self.drinks[alphabet.index(drink_chosen)][1] * drink_qty

                    # multiply food with qty

            elif drink_chosen == 'a' and self.item_index_drinks != []:

                # self.crust_base(crust_base)
                self.request()

                break
            # Some kind of message if the input is invalid
            # is good practice
            else:
                print("Invalid Input. Please choose at least one item from the menu")

    def request(self):
        ans = input("Do you have any additional request? Y/N")
        if ans == "Y":
            req = input("Enter your request here: ")
            self.comment = req
            self.invoice()
        else:
            self.invoice()

    def invoice(self):

        self.subtotal = self.total
        self.VAT = self.subtotal * self.vat
        self.TOTAL = self.subtotal + self.VAT
        print(f"Table Number: {self.get_table()}")
        fmt = '{:<8}{:<27}{:<20}{}'

        print(fmt.format('', 'Item', 'Price', 'Qty'))
        for row, (item, price, qty) in enumerate(zip(self.item_list, self.item_price_list, self.item_qty)):
            print(fmt.format(row, item, price, qty))
        print(f'Sides: {self.sides_req}')
        print(f'additional Request: {self.comment}')

        print("---------------")
        print(f'Subtotal: £{format(self.subtotal, ",.2f")}')
        print(f'VAT 5%: £{format(self.VAT, ",.2f")}')
        print(f'Total Due: £{format(self.TOTAL, ",.2f")}')


def main():
    is_valid = True
    while is_valid:
        try:
            table_number = int(input("Enter your table Number: "))
            if table_number > 25:
                print("Please enter a table number between 1-25")
            else:
                info = Program(table_number)
                info.order()
                is_valid = False
        except ValueError:
            print("Enter a valid number between 1-25")


if __name__ == '__main__':
    main()
