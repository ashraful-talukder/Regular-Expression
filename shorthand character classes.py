import re

sentence1 = "Welcome to the year 2019"
sentence2 = "I love @$%@&^ Bangladesh's weather.   #it's cool"
sentence3 = "I        love           Justice         league" 
sentence1_modified = re.sub(r"\d","",sentence1) # 'd' stands for digit and '\' is an escaping character

sentence2_modified = re.sub(r"[$@%&^\'\.#]"," ",sentence2) # '.' means all character and here '\.' means escaping the original meaning of '.'

sentence2_modified = re.sub(r"\w","",sentence2) # removing all [a-zA-Z0-9]
sentence2_modified = re.sub(r"\W"," ",sentence2) # removing all characters except [a-zA-Z0-9]
                               
sentence2_modified = re.sub(r"\s+"," ",sentence2_modified) # removing the extra space with a single space

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+"," ",sentence2_modified) # removing single letter

sentence3_modified = re.sub(r"\s+love\s+"," hate ",sentence3)
sentence3_modified = re.sub(r"\s+"," ",sentence3_modified)

# open variable explorer to see the change
# you can also use print() to show the change