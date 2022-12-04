# a new form of "function" that pulls from the python function database
#import is the function and then argv is the argument variable

from sys import argv

# read the WYSS section for how to run this
# so the script is asking for 4 argument variables.
# when you run this in Terminal, the name of the script is the first argv
# then "first" is the second argument variable and so forth
# NOTE: these argumen variables will be input as strings, if we want actual number values to be represented, then use int() in conjunction with the input varianble

script, first, second, third = argv

print("The script is called:", script)
print("your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
