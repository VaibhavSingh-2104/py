fname = input("Enter file name: ")
fh = open(fname)
st = list()
for line in fh:
    line.rstrip()
    word_list=line.split()
    for w in word_list:
        if( w not in st):
            st.append(w)


#st = list(set(st))

st.sort()
print(st)
