# practicing all of the escape sequences
# this was a fun practice!
# ES = escape sequence
#the \\ ES just allows for the backslash to be printed in the string

print('what does this do? \\ \n' )

#the \' ES alllows for the single quote to be printed in the string

print('and this \' \n')

# the \" ES allows for the double quote to be printed in the string

print('and this \" \n')

# the \a ES makes your computer do the classic "bell" sound, like for notifications and stuff!

print('what is ASCII \abell? \n')

# the \b ES engages the "backspace" key for whatever is right before it, in this case it is deleting the space after the \b ES

print('what is ASCII \b backspace??\b \n')

# the /f ES does something about  a page break and then continuing printing on a new piece of paper
#Windows powershell just displays a Venus Symbol, however, I believe this is synonmous with the "ctrl+enter" hotkey with Microsoft Word or Google docs etc

print('wait there is more ASCII stuff?? \f formfeed?! \f \n')

#the \n ES is like using the "enter" key. it continues printing on the following line

print('omg linefeed?? \n oh yeah \n I know what this does \n duh \n')

# the \N ES pulls a symbol from the Unicode database in regards to its actual written name in the unicode database

print('not sure what this unicode thing is yet but lets see what these do \N{BLACK CHESS KNIGHT} whoa! \N{BLACK CHESS PAWN}, \n I\'m learning chess! \N{GRINNING FACE} \n')

# the \r ES will write over the most recent text in the string with whatever is following it
# initally I did not understand what kind of "carriage" it was referencing but now I understand that it is in reference to old typewriter carriages.
# Think about when the carriage returns to the beginning, if you did not go onto the following line you would just be typing on top of the previous line you just typed!
# old school meets new school! wow!

print('carriage return? like baby carriages or something? \r and how about now? \r whoa it just erased the beginning of my other line! \n')

# the \t ES will engage the tab key and create a tab in the position of the \t ES

print('the good ole tab \t wow \t i \t am \t the \t tab \t master \t invisible tab mode \t\t\t\t\t\t\t \n')

# the \uXXXX ES will pull the unicode 16 bit code value from the unicode database and display that symbol

print('16bit hex value huh? whats that all about \u0394, or \u2716, or \0010, how fascinating \n')

# the \UXXXXXXXX ES will pull the unicode 32 bit code value from the unicode database and display that symbol

print('32 BIT HEX VALUE??? lets see what thats all about \U00000045, hmmm \U00000033, and \U00001212 \n')

# the \v ES will be kind of like the \t ES but in vertical orientation, so its like pressing the "enter" or "return" key 4 times or so. good for formatting headers, footers, margins etc

print('A Vertical Tab??? \v whoa \v this is like ultra tab mode \v how fancy \v \n')

# the \000 ES pulls the octal value of the symbol from the unicode or ASCII database and displays that symbol

print('Octal Value? whats that all about \001 \n')

# the \xhh ES pulls symbols using hex values and prints that corresponding symbol

print('hex value huh? this is somewhat connected to those 16 and 32 bit escape sequences I bet... lets see \x01 , \x12 , \x15 \v wow escape sequences are so cool! \n')

#Nice! that was some good ES practice! 
