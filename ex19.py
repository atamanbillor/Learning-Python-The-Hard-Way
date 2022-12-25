# using the def function we define the function and its accompanied variables that are necessary for it to do what we want

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print ("Get a blanket.\n")

#now the function is defined and we can begin to assign values to the variables and begin to call the function

# defining the given variables with integer values and calling the function

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#defining the variables prior to calling the function

print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# exhibiting that operations can be done within the bounds of the function

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 * 6)

# ability to use variables and operations within the bounds of calling the function

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#NICE
