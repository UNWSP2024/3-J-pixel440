Hotdog=3.50
Chilidog=4.50
Cheese=.50
Peppers=.75
Grilled_onions=1.00
Tax_rate=.07


hot_dog_type = input("Enter the type of hot dog (Hotdog or Chili Dog): ")


if hot_dog_type == "Hotdog":
    base_cost = Hotdog
elif hot_dog_type == "Chili Dog":
    base_cost = Chilidog
else:
    print("Please enter either Hotdog or Chili Dog")


total_toppings_cost=0.00


cheese = input("Would you like cheese? (yes/no): ")
if cheese == "yes":
    total_toppings_cost += Cheese

peppers = input("Would you like peppers? (yes/no): ")
if peppers == "yes":
    total_toppings_cost += Peppers

onions = input("Would you like grilled onions? (yes/no): ")
if onions == "yes":
    total_toppings_cost += Grilled_onions


subtotal = base_cost + total_toppings_cost
tax = subtotal * Tax_rate
total_cost = subtotal + tax


print("----------Order Receipt----------")
print(f"         Hot Dog: ${base_cost:.2f}")
print(f"         Toppings: ${total_toppings_cost:.2f}")
print(f"         Tax: ${tax:.2f}")
print(f"         Total Cost: ${total_cost:.2f}")
