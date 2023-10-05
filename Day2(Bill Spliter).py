#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")

total = float(input("What was the total bill?\n$"))
tip= int(input("What percentage of tip would you like to give? 10, 15, 12?\n"))
people = int(input("How many people to split the bill?\n"))

tip_percent = tip / 100 * total + total
pay = int(tip_percent / people)
print(f"The Amount per person is ${pay}")