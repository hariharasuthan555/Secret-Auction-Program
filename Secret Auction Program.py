bids={}
bidding_finished=True

def find_highest_bidder(bidding_record):
  highest_amount=0
  winner=""
  for bidder in bidding_record:
    bid_amount=int(bidding_record[bidder])
    if bid_amount>highest_amount:
      highest_amount=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highest_amount}")

while bidding_finished:
  name=input("What is your name?")
  price=input("What is your bid?")
  bids[name]=price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue=="no":
    bidding_finished=False
    find_highest_bidder(bids)
  elif should_continue=="yes":
    print("\n"*20)
    
