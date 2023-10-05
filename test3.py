import Database

dname = Database.name 
name =input("What is your name??\n").lower()
age = int(input ("What is your age????\n"))
contact = int(len(input("What is your contact number???\n")))
address = input("Where do you live??\n")
gender = Database.gender()

def bool_to_word(name , age , address):
    if name == "":
        ename =int(input("Type no:\n"))
        name = dname[ename]
        print (f"Hi {name}")
        #return "Error please type your name"
    else:
        print(f"Hi {name}")
        
    if age < 18:
            print("You are not allowed to vote")
    elif age > 60:
            print("You are more then allowed to vote")
    else:
        print(f"Your age is {age}. You can vote.")
    
    gender
    
    if 10 > contact <= 8 :
        print ( f"{name} Your phone number should be at least of length 9 digits ")
    else:
        return "Your Contact Number is" + contact
    
    if address != "ktm":
        print("can you come closer to my home town...")
    else:
        return "We are Close......."
    
nickname = input("What is your nickname???\n")

print(bool_to_word(name , age , address))
print(f"{gender.represent} {name},We are happy to have you on the ride. ")