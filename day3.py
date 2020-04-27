v=input()
n=int(v)
if n==1 or n/2!=0:
    print('Weird')
elif n/2==0 or 2<=n<5:
    print('Not Weird')
elif n/2==0 or 6<=n<20:
    print('Weird')
elif n/2==0 or n>20:
    print('Not Weird')
