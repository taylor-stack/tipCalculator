print("Thanks for checking out the tip calculator!\n")

total = int(input(" What was the total bill?\n"))

people = int(input(" How many people are splitting the bill?\n"))

tip = float(input(" What percentage of a tip would you like to give?\n"))

new_total = (total * tip)

new_amount = ((total + new_total) / 5)

share = str(new_amount)

print("Each person should pay:" + " " + share)