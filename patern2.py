n=int(input("Enter n :"))
i=1
j=i
for i in range(n+1):
    for j in range(n-i):
          print(j,end=' ')
    print()
