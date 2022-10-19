# shop.py


# Functions
def PrintMenu():
  print("-" * 50)
  print("Please enter the number corresponding to the desired transaction.")
  print("1: Print Buy List")
  print("2: Print Sell List")
  print("3: Buy Item")
  print("4: Sell Item")
  print("5: Add Item to Buy or Sell List")
  print("6: Change Price of Item in Buy or Sell List")
  print("7: Quit")

def PrintList(l):
  print("Name".ljust(20), "|", "Price".ljust(20) + "\n")
  for item in l:
    price = "$" + str(l[item])
    print(item.ljust(20), "|", price.ljust(20))


# Input file
file = input("Enter the filename of the file in question: ")
file = open(file, 'r')


# Setup
buy = {}
sell = {}
for tran in file.readlines():
  tran = tran[:-1].split("\t")
  if len(tran) > 3:
    tran[1:-1] = " ".join(tran[1:-1]) # Joins the name into one element if necessary
  
  tran[2] = float(tran[2][1:])
  if tran[0] == "Buy":
    buy[tran[1]] = tran[2]
  else:
    sell[tran[1]] = tran[2]

file.close()


# Menu
money = 0
option = "0"

print("Welcome to the best pawn shop in the world.")
while option != "7":
  PrintMenu()
  option = input()
  if option == "1":
    PrintList(buy)
  elif option == "2":
    PrintList(sell)
  
  elif option == "3":
    item = input("Enter the name of the item being bought: ")
    if item in buy:
      money -= buy[item]
      buy.pop(item) # https://www.w3schools.com/python/ref_dictionary_pop.asp
    else:
      print("Item not found")
  
  elif option == "4":
    item = input("Enter the name of the item being sold: ")
    if item in sell:
      money += sell[item]
      sell.pop(item)
    else:
      print("Item not found")
  
  elif option == "5":
    name = input("Enter the name of the item: ")
    price = input("Enter the price for the item: ")
    try:
      price = float(price)
      l = input("Enter 'buy' or 'sell' to add it to that list, or anything else to cancel: ")
      if l == "buy":
        if name in buy:
          print(name, "is already in the buy list.")
        else:
          buy[name] = price
      elif l == "sell":
        if name in sell:
          print(name, "is already in the sell list.")
        else:
          sell[name] = price
    except:
      print("Invalid price")

  elif option == "6":
    l = input("Enter 'buy' or 'sell' to change that list, or anything else to cancel: ")
    if l in ["buy", "sell"]:
      name = input("Enter the name of the item: ")
      price = input("Enter the price for the item: ")
      try:
        price = float(price)
        if l == "buy":
          if name in buy:
            buy[name] = price
          else:
            print(name, "is not in the buy list.")
        elif l == "sell":
          if name in sell:
            sell[name] = price
          else:
            print(name, "is not in the sell list.")
      except:
        print("Invalid price")
  
  elif option != "7":
    print("Option not recognized")


# Output
net = "$" + str(money)
print("The net gain from this session is", net)

file = input("Enter the filename of the file to store the new data: ")
file = open(file, 'w')
for item in buy:
  lines = ["Buy"]
  lines.append(item)
  price = "$" + str(buy[item])
  lines.append(price)
  file.write("\t".join(lines) + "\n")
for item in sell:
  lines = ["Sell"]
  lines.append(item)
  price = "$" + str(sell[item])
  lines.append(price)
  file.write("\t".join(lines) + "\n")

file.close()