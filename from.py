fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    x=line.split()
    if len(x)<3 or x[0]!=("From"):
        continue

    print(x[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")
