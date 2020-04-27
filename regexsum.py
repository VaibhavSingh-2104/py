import re
fhand=input("Enter File name: ")
hand=open(fhand)
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for n in stuff:
        numlist.append(int(n))
print('Total Sum:',sum(numlist))
