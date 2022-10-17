# shop.py


# Input file
file = input("Enter the filename of the file in question: ")
file = open(file, 'r')


# Setup
buy = {}
sell = {}
money = 0
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