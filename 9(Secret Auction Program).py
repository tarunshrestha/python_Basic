#from replit import clear
#from art import logo 
from os import system
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
canplay = True
bidder = {}

print(logo)


    #Another method to add bidder name and price
def Add_bidder(bidder_name , bidder_bid):
    new = {}
    new["name"] = bidder_name
    new["bid"] = bidder_bid
    bidder.append(new)
    
def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidders in bidding_records:
        bid_amount = bidding_records[bidders]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner = bidders
    print(f"The winner is {winner} with the higgest bid of ${highest_bid}.")

while canplay is True:
    name =input("What is your name?\n")
    price = int(input("What is the bidding price?\n$")) 
    bidder[name] = price
    should_continue =input("Are there any other Bidders? Type 'yes' or 'no'.\n ")
    if should_continue != "yes":
        canplay = False
        highest_bidder(bidder)
    else:
        system('cls') #clear terminal window
        