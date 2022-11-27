# formatter is a variable given the string of squigglies, which...
# can be formatted or they can be displayed as is

formatter = "{} {} {} {}"

# some print functions here using the formater variable, and
# with the use of the .format function, desired values or strings
# can be input into the squigglies locations in the order they are
# listed, how neat!

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

# I wrote a poem

print(formatter.format(
    "Have you ever",
    "Swallowed oceans",
    "of Dragonflies",
    "With your sweet eyes?"
))
