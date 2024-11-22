from datetime import datetime as dt
current_date = dt.now


class Purchase:
    def __init__(self, purchase_name: str, price: float, category: str,
                 purchase_date=str(current_date()), quantity=1):
        self.__purchase_name = purchase_name
        self.__price = price
        self.__category = category
        self.__purchase_date = purchase_date
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


    def set_quantity(self, new_quantity):
        if new_quantity > 0:
            self.__quantity = new_quantity


    def __str__(self):
        return (f"name= {self.__purchase_name}, price= {self.__price},"
                f" category={self.__category}, purchase_date= {self.__purchase_date},"
                f" quantity= {self.__quantity}")
