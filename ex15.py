#so, "sys" is a package of python functions and stuff
# the "import" function is pulling from this package database the following function that you ask for
# in this case, it is the "argv" , argument variable, function

from sys import argv

#the argument variables are "script" and "filename"

script, filename = argv

#here, the variable "txt" is assigned to the function of "open" for the argument variable of "file_name"
# also, after inserting other .py files into the argv I was outputted with text of that corresponding code. it doesnt have to be a .txt file for the open function to work. In terminal it just outputs text of the code, FANCY


txt = open(filename)

#printing the string and calling the filename string

print(f"Here's your file {filename}")

#printing the txt variable with a .read... hmmm maybe this is what converts the .py files into text in Terminal, We shall find out!
# after running a sample code, it is the .read function that is outputting the files as text into terminal! wow!

print(txt.read())

#same idea down here, except there is a new variable. Which means you can read or open a different file if you wish.

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

#Same stuff, I can use the same file if I want or any other .py or .txt file. I havent attempted other files quite yet

print(txt_again.read())
