from sys import argv

script, filename = argv

print("""

So you want to to read this so called "file" thing? """)
print(" We will see about that... ")
print(""" SOooo, if you want to read the file
press enter

OR

press CTRL + C if you dont want to!

just make up your mimd quick!""")

input(" ? ")

target = open(filename, 'w')

print(f"Ok, the {filename} is open and in write mode!")

print(f"lets write something to the {filename}")

newtext = input("ENTER TEXT HERE:  ")

print(f"Now we will rewrite your {filename} with your new text!")
print("very exciting stuff")

target.write(newtext)

target.close()
