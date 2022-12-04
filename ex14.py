from sys import argv

script, user_name, to_do = argv
prompt = ">>> "


print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

#the triple quotes used in conjunction with curly brackets to draw from the input variable strings

print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer}. Nice
""")

#adding another argument variable to better comprehend its function

print(f"Also looks like you like to {to_do}")
