def drawingEdge(n):
    # Write your code here

    if n > 2:
        result=pow(2,n*(n-1)/2)

    else:
        result=pow(n,1)
    return result
z=input()
n=int(z)
x=drawingEdge(n)
print(x)
