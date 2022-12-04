#practicing input functions
# the "end=' '" tells the code to continue printing the input onto the same line as the the string it printed.

print("How old are you?", end =' ')
age = input()
print("How tall are you?", end =' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

#the print(f"X") allows the string to be formatted with the appropriate variables referenced with the curly brackets

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
