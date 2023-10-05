#from pip._internal import locations
name = input(str(print("What is your name?\n")))
age = input(print ("What is your age ?\n"))
id_number = input(print("What is your id_number ? \n"))
address =  input(print("Where do you live??\n"))
points = input(print("What are your grades?\n"))
can_go = "yes";

if points > 4:
    can_go = "Congrats You have been accepted with full scholarship."
elif points >= 2.5:
    can_go = "You nearly got Accepted."
else:
    can_go ="Sorry, You cannot go."

print(f"Hi {name} aged {age} .\n Your Id Number is {id_number} \n You live in {address} \n {can_go}")
