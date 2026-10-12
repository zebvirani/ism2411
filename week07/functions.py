#AI-Discolsure
# i used chatgpt to help explain Python functions
#and variable scope.
# AI helped me understand how the code works
# I reviewed the examples and tested the code myself

#self assessment
#the first bug i noticed was the missing colon because it stuck out eaisly especially since there was a previous example
# i found it by just looking at the code and noticed missing syntax. THis tells me that i can mostlikely spot obvious mistakes
# but i need help spotting more complicated mistakes
#2. apply discount takes a price and a tier level and returns the price multiplied by the discount asscoiated with the given tier.
# a colleague could eaisly use it without reading the body.
#3. I used AI for parts of each exercise when I got stuck and did not know how to proceed. Ai did build my understanding since I read the output and 
#typed it in myself to understand what the code was doing


#--exercise 1
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

#---exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    
    return price * (1 - discount)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

#---exercise 3
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax :${total:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

#--exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#---exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #add + sign so all values add up and doesnt take the lasst value assigned which is 90
print(f"Total: ${total}")

count = 0
for sale in sales:# needed to add colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):#list index out of range. rmove = to to make sure it stays in range of 0-4
    print(sales[i])
    i += 1

#--exercise 6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?
# scope is how a variable can be used?
# x is a global variable so print x will equal 100
#double it is a local variable so so it is a seperate entity that has a seperate value.