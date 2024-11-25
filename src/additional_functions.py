def validate_positive_number(message: str) -> int:
    flag = True
    while flag:
        try:
            value = input(message).strip()
            if value.lower() == 'exit':
                flag = False
            else:
                if int(value) > 0:
                    return int(value)
                else:
                    print("Entered number should be positive and greater than zero.")
        except ValueError:
            print("It is not a number. Please write a number.")
    return 0

message = "Please enter a price: "
price = validate_positive_number(message)
print(f"price is >{price}<")
