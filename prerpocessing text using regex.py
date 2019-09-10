import re

X = ["I know the #right to chose.",
     "What makes you so sure that the number is 3478325",
     "Remember this @#%*! sign's are effective",
     "      I love         you",
     "Do you know someone - called #s-John Wick    "]
     
for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i]) # removing all unwanted characters
    X[i] = re.sub(r"\d"," ",X[i]) # removing all digits
    X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i]) # removing all single letter
    X[i] = re.sub(r"\s+"," ",X[i]) # removing extra spaces
    X[i] = re.sub(r"^\s","",X[i]) # removing spaces from the starting of a line
    X[i] = re.sub(r"\s$","",X[i]) # removing spaces from the end of a line