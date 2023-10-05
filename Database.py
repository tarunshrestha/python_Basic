name = ["tarun" , "arun", "muskan"]
city = ["ktm" , "Pokhara" , "Chitwan"]

def gender():
    represent = input("Male or Female??").lower()
    if represent == "male":
        represent = "Mr."
    elif represent == "female":
        represent ="Ms."
    else:
        represent = "They"

        
def count(num):
    for i in num:
        print (i)
