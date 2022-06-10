# No use of reserved words like print, while, if ...
# Start with letter or underscore followed by letters, numbers or _
# Use meaningful variable names

distance_travelled_mi = 100

time_taken_min = 1200

time_taken_hr = time_taken_min / 60

print("Number of miles travelled", distance_travelled_mi)
print()

print("Number of hours travelled", time_taken_hr)
print()

print("Speed in mph", distance_travelled_mi / time_taken_hr)
print()

fruits = "apples and oranges"
num_apples = 100
num_oranges = 200
print(
    "I have",
    fruits,
    "... I have",
    num_apples,
    "apples and",
    num_oranges,
    "oranges",
    sep=" ",
)
