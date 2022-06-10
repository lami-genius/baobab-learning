NUM_DECIMAL_PLACES = 2
# Exercise 1
print(
    "",
    "Excercise 1",
    "",
    sep="*" * 5,
)
EURO_TO_USD = 1.06
amount_in_euro = 200
amount_in_usd = round(amount_in_euro * EURO_TO_USD, NUM_DECIMAL_PLACES)

print(f"Amount in Euro: {amount_in_euro:2}")
print(f"Exchange rate: {EURO_TO_USD:5}")
print(f"Amount in USD: {amount_in_usd:7f}")

print("-" * 75)

# Exercise 2
print(
    "",
    "Excercise 2",
    "",
    sep="*" * 5,
)
bill_amount = 400
tip_percentage = 0.6
total_amount_due = round(bill_amount * (1 + tip_percentage), NUM_DECIMAL_PLACES)

print(f"Initial bill amount: {bill_amount}")
print(f"Tip percentage: {tip_percentage * 100}%")
print(f"Total amount due: {total_amount_due}")

print("-" * 75)

# Exercise 3
print(
    "",
    "Excercise 3",
    "",
    sep="*" * 5,
)
import math

radius = 20
circumference = round(2 * math.pi * radius, NUM_DECIMAL_PLACES)
area = round(pow(radius, 2) * math.pi, NUM_DECIMAL_PLACES)

print(f"Radius: {radius}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")

print("-" * 75)

# Excercise 4
print(
    "",
    "Excercise 4",
    "",
    sep="*" * 5,
)
num_val = 71
is_even = num_val % 2 == 0

print(f"Number is: {num_val}")
print(f"Is {num_val} even? ", is_even)
print(f"Is {num_val} odd? ", not is_even)

print("-" * 75)

# Exercise 5
print(
    "",
    "Excercise 5",
    "",
    sep="*" * 5,
)
amount_in_dollars = 256

# 20s
num_20s = amount_in_dollars // 20
amount_remaining = amount_in_dollars % 20

# 10s
num_10s = amount_remaining // 10
amount_remaining = amount_remaining % 10

# 5s
num_5s = amount_remaining // 5
amount_remaining = amount_remaining % 5

# 1s
num_1s = amount_remaining

print(f"Amount in USD: {amount_in_dollars}")
print(f"Number of 20s: {num_20s}")
print(f"Number of 10s: {num_10s}")
print(f"Number of 5s: {num_5s}")
print(f"Number of 1s: {num_1s}")

print("-" * 75)
