def greet(age):
    age_detail = "Your age is " + repr(age)+"."
    if age >= 60:
        return f"{age_detail}Hello, senior!"
    elif age <=18:
        return f"{age_detail}you should not be in here!"
    else:
        return f"{age_detail.upper()} Hello Comrade"

def password(password):
    password_length = len(password)
    if  password_length <= 5 or password_length == None :
        return "Invalid Password"
    
    
x=int(input("What is your age???\n"))
y=input("Enter Password!\n")


print(f"{greet(x)} i am Tarun.\n Your password is {password(y)}")