

def discount_calculator(discount):

    def apply_discount(price):
        return price - (price * discount)

    return apply_discount


ten_percent = discount_calculator(0.10)

print(ten_percent(500))
print(ten_percent(1000))