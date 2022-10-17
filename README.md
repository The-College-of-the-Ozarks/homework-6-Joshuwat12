# Prog1-HW6

Write a program to tackle the following problem. All programming should use good function and variable names and sufficient comments for improved readability.

> *Note: this project is more in-depth than previous assignments, bringing together many pieces that we've talked about so far. Start early, and work on one piece at a time. Don't expect to sit down and do the entire project in one sitting. Put your file through rigorous testing; feel free to change or create new input files, add output where helpful to make sure code is doing what you expect it to, etc. Don't be afraid to ask questions early and often. If you put this off until the day or two before it is due, I will not have time to help you with every piece of your code.*



In this project, you are running a pawn shop (or any other sort of shop that buys and sells any type of goods). Your shop maintains a list of all items it currently has to sell and all items it is currently willing to buy conveniently stored in a data file.

- Your program should start by prompting the user for the name of the input file. Do not move on until you have successfully opened the file specified.

  The input file will be formatted as follows:

      Buy/Sell\tName\t$Price\n

  Where Buy/Sell will say either "Buy" or "Sell", "\t" denotes a tab character, $Price will be a number with two decimal places preceded by a dollar sign, and \n represents a new line (there will be only one item per line). (I encourage you to inspect good_list.dat to familiarize yourself with the input file format). You may assume the data is formatted correctly (see bonus below for validation). ***Only use bad_list.dat for the bonus!***

- After opening the file, your program should loop through the file and construct two dictionaries: a buy list and a sell list. Each dictionary should have Name:Price pairs. Put each item in the appropriate dictionary as indicated by the Buy or Sell column; remove the $ from Price and cast it to a float. Also create a variable initialized to 0 which will hold how much money the shop spends or makes in this shopping session.

- Next, your program should enter into a menu with the following options, and continue looping back to this menu until the quit command is given. Menu items should follow the instructions given.

1. Print Buy list
    > Buy list should be printed with the Name (you may assume at most 20 characters) and Price aligned into columns, one item per row. Price should be preceded by a dollar sign.
2. Print Sell list
    > Sell list should be printed with the same format as the buy list. (*Hint: you may wish to define a function that loops through an arbitrary dictionary and outputs in this way*).
3. Buy item
    > The user gives the name of an item on the buy list (you should validate this; if incorrect, return to menu). The shop buys that item. This should change a running counter indicating how much money the shop has spent or made in this shopping session and remove the indicated item from the buy list.
4. Sell item
    > The user gives the name of an item on the sell list (you should validate this; if incorrect, return to menu). The shop sells that item. This should change a running counter indicating how much money the shop has spent or made in this shopping session and remove the indicated item from the sell list.
5. Add item to Buy or Sell list
    > The user gives the name and price of a new item, and state if it should be added to the buy or sell list. Verify the item is not on the specified list, then add it. If it is already on the list, tell the user and return to menu without changing.
6. Change price of item in Buy or Sell list
    > The user states which list the item is on, then gives the name and updated price. Verify the item is on the specified list, then modify it. If it is not already on the list, tell the user and return to menu without adding.
7. Quit
    > Before fully exiting the program, you should output how much the shop spent or made in this session. Then prompt the user for the name of the output file to be created. Do not move on until a valid output file is opened. Finally, output the remaining buy list and sell list to this output file *in the correct format to be read back in to the program if you started over*.

***Bonus***

Add validation to ensure the input file follows the specified format, and skip lines that are not correct (but warn the user the line is incorrect by line number). Validation should ensure the following properties:
- When splitting at tab characters, there should be exactly three pieces of data.
- The first entry should only say either "Buy" or "Sell", anything else is an error.
- The second entry should not match any key already put into the specified dictionary.
- The third entry should have a $ and a *positive* price.

Your validation should catch all of the errors found in bad_list.dat
