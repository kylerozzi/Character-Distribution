"""
distribution.py
Author: <your name here>
Credit: Tristan Meyer helped me

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
import string
alphabet = list(string.ascii_lowercase)

sen=str(input('Please enter a string of text (the bigger the better): '))
sen1=''.join(e for e in sen if e.isalnum())
sen1=(sen1.lower())
len1=len(sen1)
g = ""
num= []

for i in alphabet:
    if sen1.count(i) !=0:
        g=(sen1.count(i))*(i)
        num.append(g)



