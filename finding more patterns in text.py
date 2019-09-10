#import library

import re

sentence="1995 is the year I was born"

re.match(r"[a-zA-Z]+",sentence)  #will give no output because match() does local search

re.search(r"[a-zA-Z]+",sentence) #will give output because search() does global search

#finding starting pattern

if re.match(r"^[0-9]+",sentence):  #"^" sign represents the starting
    print("Starts with digit ")
else:
    print("Starts with character")

#finding the ending of pattern
    
if re.search(r"[0-9]$",sentence):   #"$" sign represents the ending
    print("Ends with digits ")
else:
    print("Ends with character")