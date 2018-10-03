"""
distribution.py
Author: <your name here>
Credit: https://www.tutorialspoint.com/How-to-remove-all-special-characters-punctuation-and-spaces-from-a-string-in-Python    

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
sen=str(input('Please enter a string of text (the bigger the better): '))
sen1=''.join(e for e in sen if e.isalnum())
sen2=(sen1.lower())
sen3=list(sen2)
num= []
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in sen3:
        num.append(sen3.count(i))


num1,sen4 = list((zip(list(t) for t in zip(*sorted(zip(num, sen3))))
both = list((zip(num1,sen4)))



