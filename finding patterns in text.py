#import library
import re

#finding if there is zero or more characters or anything matches

sentence = "I am a student"
re.match(r".*",sentence)

#finding if there is one or more characters or anything matches

sentence = "I am a student"
re.match(r".+",sentence)

sentence2=""
re.match(r".+",sentence2) #it will give no output

#finding the match of letters only

sentence = "I am a student"
re.match(r"[a-zA-Z]*",sentence)

#finding the match of sequence

c="a"
re.match(r"ab?",c)

c1="b"
re.match(r"ab?",c1) #this will show no output

c2="abb"
re.match(r"ab?",c2) #this will show only the expected result 'ab'