from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
auction_bids = {}

def bids():
  name = input("What is your name?   ")
  user_bid = int(input("How much would you like to bid?   $"))
  new_bid = {
    "name": name,
    "bid": user_bid
  }
  auction_bids[name] = user_bid
  
def highest_bid(auction_bids):
  highest_bid = 0
  winner = ""
  for bidder in auction_bids:
    bid_amount = auction_bids[bidder]
    if bid_amount > highest_bid:
      winner = "".join(bidder)
  print(f"The winner of the auction is {winner}!")
    
def more_bids():
  more_people = input("Would anyone else like to bid? Type 'yes' or 'no':  ")
  while more_people == "yes":
    clear()
    bids()
    more_people = input("Would anyone else like to bid? Type 'yes' or 'no':  ")

  highest_bid(auction_bids)

    
bids()
more_bids()
