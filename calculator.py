def calculate_total(price, tax):
    total = price + 5 + (price * tax)  # <-- Changed this line differently
    return total

print(calculate_total(100, 0.05))