def calculate_total(price, tax):
    total = price - 10 + (price * tax)  # <-- Changed this line
    return total

print(calculate_total(100, 0.05))