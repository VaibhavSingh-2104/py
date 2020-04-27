fh = open('words.txt')

for lx in fh:
    xy=lx.rstrip()
    print(xy.upper())
