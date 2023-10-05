#the x must be up so that it can be runned for dictionary.
x = 1111
programing_dictionary = {
    "Id":"It is a number given to a user to know their details.",
    "Username":"The name of the user written to be used as profile name.",
    "Password":"The set of charecters used as a key to get logged into account.",
    123: f"This is a checking of the number in this code {x}"
    }


a =input("What key should be added to dictionary?\n")
b =input("What is its description??\n") 

def Add(key = a,text= b):
    programing_dictionary[a] = b
    print(programing_dictionary)

Add()


#############################################_NOTES_#############################################################

#Print individual
#print(programing_dictionary["Username"])

#Add 
#programing_dictionary["Admin"] = "Admin is the boss no one can defy him."

#Edit
#programing_dictionary["id"] = "I can say whatever i like."

#Print all
#print(programing_dictionary)

#Create empty
#hi_dictionary = {}

#delete existing dictionary
#del hi_dictionary

#wipe existing dictionary
#programing_dictionary ={}

#Loop keys and text(for key only print(key))
#for key in programing_dictionary:
#    print (f"{key} :{programing_dictionary [key]} ")