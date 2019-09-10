import re

sentence="I love Iron man"
print(re.sub(r"Iron man","Captain America",sentence))

print(re.sub(r"love","hate",sentence))

print(re.sub(r"[a-z]","0",sentence,4,flags=re.I)) #flag "re.I" removes case sensitivity

print(re.sub(r"[a-z]","0",sentence,4)) # fist I won't be count because of case sensitivity