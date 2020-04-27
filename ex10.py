name = input("Enter file:")
fhand = open(name)
counts=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    x=words[5]
    y=x.split(':')
    counts[y[0]]=counts.get(y[0],0)+1

tmp=list()
def ky(a):
    return a[0]

for k,v in counts.items():
    newtup=[k,v]
    tmp.append(newtup)

tmp=sorted(tmp,key=ky)
for k,v in tmp[:]:
	print(k,v)
