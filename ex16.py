# retreiving the argv variable function from python sys package

from sys import argv

# defining the argument variables

script, filename = argv

#some print functions with "filename" being called for in the curly brackets

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTR:-C (^C).")
print("If you do want that, hit RETURN.")

# if you press RETURN, the script will continue, if you press ctrl c then it will terminate the script via "keyboard interrupt"

input("?")

print("Opening the file...")

# assigning the variable, 'target' to the filename called for in the argv, in this case, text.txt
# the 'w' is giving a mode to the file we are opening
# the w mode is allowing us to write into the chosen file

target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
