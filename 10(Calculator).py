from os import system 

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations={
    "+": add,
    "-":sub ,
    "*": multiply,
    "/": divide
}

def symbols():
    for i in operations:
        print(i)
        

total = 0
num1 = float(input("What is the first number?\n"))
symbols()
symbol = input("Pick the operation.\n")
num2 = float(input("What is the second number?\n"))
calculate =operations[symbol] #choosing operation
first_total = calculate(num1,num2) #using operation key and calling function to run the both value 

print(f"{num1} {symbol} {num2} = {first_total}")
total = first_total
canplay = True
while canplay is True:
    choose= input("Do u wanna continue calculating or end it?\n Type 'y' to continue and 'n' to end.\n")
    if choose != "y" :
        canplay = False
        print("Goodbye Thank you for using the calculator.")
    else:
        system('cls')
        print(f"The previous value is {total}")
        symbols()
        symbol_2 = input("Choose and operation symbol.\n")
        # if symbol != "+" or symbol != "-" or symbol != "*" or symbol != "/" :
        #     print ("You picked", symbol,"which isn't supported.")
        #     break
        num3 = float(input("What is the next number?\n"))
        calculate_2 = operations[symbol_2]
        second_total = calculate_2 (total,num3)  #calling second total with first total as an argument.
        total =second_total
        print(f"{first_total} {symbol_2} {num3} = {second_total}")
        
        