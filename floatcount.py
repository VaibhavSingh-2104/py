import statistics
fname = input("Enter file name: ")
fh = open(fname)
a=list()
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        x,y=line.split()
        a.append(float(y))
print('Average spam confidence:',statistics.mean(a))
