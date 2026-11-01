# ISM2411 — Module 10 Lab: Inventory List Manager
# Name: Toghrul Guliyev
#
# Reflection
# 1. The most surprising thing about lists was how much you can do with
#    slicing. I expected to need a loop to get the first three items or every
#    other item, but one line like inventory[::2] does it. Negative indexes
#    also surprised me, because inventory[-1] always gives the last item
#    without knowing how long the list is.
#
# 2. # 2. In my microeconomics class (ECO2023) I worked on a case study about the
#    rental housing market. Comparing rent prices meant typing numbers into
#    Excel and writing formulas for the average, the highest, and the lowest
#    rent. With a Python list I could store all the rents once and use sum(),
#    max(), min(), and a loop to filter rents above a certain price in a few
#    lines, then rerun it instantly if I added new data.

# Exercise 1 — Build the list
print("=== Exercise 1: Build the list ===")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2 — Index practice
print("\n=== Exercise 2: Index practice ===")
print(inventory[0])                    # first item
print(inventory[-1])                   # last item
middle = len(inventory) // 2           # computed, not hard-coded
print(inventory[middle])               # middle item

# Exercise 3 — Slicing
print("\n=== Exercise 3: Slicing ===")
print(inventory[:3])                   # first three
print(inventory[-2:])                  # last two
print(inventory[::2])                  # every other item

# Exercise 4 — Modify
print("\n=== Exercise 4: Modify ===")
inventory.append("envelope")
print("After append:", inventory)
inventory.remove("tape")
print("After remove:", inventory)
inventory.sort()
print("After sort:  ", inventory)

# Exercise 5 — Tuple comparison
print("\n=== Exercise 5: Tuple comparison ===")
coords = (40.7128, -74.0060)           # NYC latitude, longitude
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples cannot be changed after they are created. That is useful for")
    print("coordinates, because a location should never be edited by accident.")
print(coords)

# Exercise 6 — Average of a list of sales
print("\n=== Exercise 6: Sales summary ===")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7 — Accumulator pattern
print("\n=== Exercise 7: Accumulator pattern ===")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print("Original:  ", prices)
print("Discounted:", discounted)

# Exercise 8 — Filter above threshold
print("\n=== Exercise 8: Filter above threshold ===")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))