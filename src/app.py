from .additional_functions import validate_positive_number
from datetime import datetime as dt


DATETIME_STRING_FORMAT = "%Y-%m-%d %H:%M:%S"
current_date = dt.now


class Purchase:
    def __init__(self, purchase_name: str, price: float, category: str,
                 purchase_date=current_date(), quantity=1):
        self.__purchase_name = purchase_name
        self.__price = price
        self.__category = category
        self.__purchase_date = purchase_date.strftime(DATETIME_STRING_FORMAT)
        self.__quantity = quantity

    def get_purchase_name(self):
        return self.__purchase_name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def get_purchase_date(self):
        return self.__purchase_date

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self):
        print(f"Current quantity is {self.__quantity}.")
        message = "Enter new quantity: "
        self.__quantity = validate_positive_number(message)
        print(f"New quantity is {self.__quantity}")

    def set_purchase_name(self):
        print(f"Current purchase name is {self.__purchase_name}.")
        new_purchase_name = input("Enter new purchase_name: ").strip()
        if new_purchase_name.lower() == 'exit':
            pass
        else:
            self.__purchase_name = new_purchase_name
            print(f"The purchase name was changed to {self.__purchase_name}")

    def set_price(self):
        print(f"Current price is {self.__price}.")
        message = "Enter new price: "
        self.__price = validate_positive_number(message)
        print(f"New price is {self.__price}")

    def set_category(self):
        print(f"Current category: {self.__category}")
        flag = True
        while flag:
            new_category = input("Please enter new category: ").strip().capitalize()
            if new_category == "Exit":
                flag = False
            elif len(new_category) != 0:
                self.__category = new_category
                flag = False
            else:
                print("You entered nothing, please try again.")

    def increase_quantity(self):
        print(f"Current quantity is {self.__quantity}.")
        message = "How much do you want to increase the quantity?: "
        self.__quantity += validate_positive_number(message)
        print(f"New quantity is {self.__quantity}")

    def decrease_quantity(self):
        print(f"Current quantity is {self.__quantity}.")
        message = "How much do you want to decrease the quantity?: "
        value = validate_positive_number(message)
        if value >= self.__quantity:
            print("Quantity could not be less than 1")
            self.__quantity = 1
        else:
            self.__quantity -= value
        print(f"New quantity is {self.__quantity}")

    def display_purchase(self):
        details = f"\n{self.__purchase_name} - {self.__price}£, {self.__category},"
        details += f" quatity: {self.__quantity}, time: {self.__purchase_date}.\n"
        details += '-' * len(details)
        return details

    def __str__(self):
        return (f"name= {self.__purchase_name}, price= {self.__price}£,"
                f" category={self.__category}, purchase_date= {self.__purchase_date},"
                f" quantity= {self.__quantity}")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(purchase_name='{self.__purchase_name}', "
                f"price='{self.__price}', "
                f"category='{self.__category}', "
                f"purchase_date='{self.__purchase_date}', "
                f"quantity='{self.__quantity}')")
 