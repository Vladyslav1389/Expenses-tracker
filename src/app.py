from datetime import datetime as dt
current_date = dt.now

class Purchase:
    def __init__(self, purchase_name: str, price: float, category: str,
                 purchase_date=str(current_date()), quantity=1):
        self.purchase_name = purchase_name
        self.price = price
        self.category = category
        self.purchase_date = purchase_date
        self.quantity = quantity

    def __str__(self):
        return (f"{__name__}: name= {self.purchase_name}, price= {self.price},"
                f" category={self.category}, purchase_date= {self.purchase_date},"
                f" quantity= {self.quantity}")

first_purchase = Purchase("beer", 6, "alcohol")
print(first_purchase)