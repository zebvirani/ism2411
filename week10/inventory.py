#Q1
# the most suprising things about list in python is that they are easy to add to and alter in different ways
#Q2
#It would have saved me time tracking a to do list  and sorting them, adding to them, or removing items.
#exercise 1 

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

#exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

#exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannont be changed after creation")
    print("tuples keep fixed values so they are good for coordinates")

print(coords)

#exercise 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("count:", count)
print("Average:", average)
print("best:", max(sales))
print("Worst:", min(sales))

#exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)

#exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))

