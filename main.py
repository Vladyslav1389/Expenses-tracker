from src.app import Purchase

first_purchase = Purchase("beer", 6, "alcohol")
print(first_purchase)
print(first_purchase.get_purchase_name())
print(first_purchase.get_price())
print(first_purchase.get_purchase_date())
print(first_purchase.get_category())
print(first_purchase.get_quantity())
first_purchase.set_quantity(2)
print(first_purchase.get_quantity())

