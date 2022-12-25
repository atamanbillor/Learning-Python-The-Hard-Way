# pulling the function "import" from the sys python package

from sys import argv

#defining the argument variables

script, input_file = argv

#defining our first function
# this function prints the file that is being read
#the "f" denotes that you are calling the functions from a file

def print_all(f):
    print(f.read())

# defining the second function
# the seek function basically just moves the header to the byte that you specify it to

def rewind(f):
    f.seek(0)

# defining the third function
# the "readline" function reads one line at a time for the given file

def print_a_line(line_count, f):
    print(line_count, f.readline())

#opening the input file and defining it as a new variable

current_file = open(input_file)

print("First let's print the whole file:\n")

#calling the first defined function that will print out all of the file

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#calling the second defined function

rewind(current_file)

print("Let's print three lines:")

# printing one line at a time
# This format is repetitive and a lot of work
# best to use a loop in the future ;)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
