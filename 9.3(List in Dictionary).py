capitals = {
    "A": "Apple", #key:value pairs
    "B":"Ball",
    "C":"Cat"
    }
#Nesting Dictionary in a Dictionary
child_alpha ={
    "A":{"all": ["apple" , "aeroplane" , "Asta" , "Ace"] ,"Total": 4 } ,  #list nested in dictanary 
    "B":["ball", "bank", "BYE"]
    }

#Nesting Dictionary in a List
child_alpha_log = [
    {
        "Word":"A", 
        "all": ["apple" , "aeroplane" , "Asta" , "Ace"] ,
        "Total": 4 
    } ,  #dictanary nested in list 
    {
        "Word":"B",
        "all": ["bapple" , "baeroplane" , "bAsta" , "Ace"] ,
        "Total": 5 
    }
    
]
print(f"The first is \n{child_alpha}\n then the second is \n{child_alpha_log}")