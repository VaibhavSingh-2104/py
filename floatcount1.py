fname = input("Enter file name: ")
fh = open(fname)
a=list()
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        x,y=line.split()
        a.append(float(y))

for value in a:
    count=count+1
    total=total+value
print('Average spam confidence:',total/count)
