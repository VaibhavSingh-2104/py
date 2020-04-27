def minMoves(h,w,h1,w1):
    number_of_folds =0
    while(h1<=h/2):
        h=h/2
        number_of_folds = number_of_folds+1

    if(h1!=h):
        number_of_folds = number_of_folds+1

    while(w1<=w/2):
        w=w/2
        number_of_folds = number_of_folds+1

    if(w1!=w):
        number_of_folds = number_of_folds+1
    return number_of_folds

h,w,h1,w1 =[int(x) for x in input().split()]
print(minMoves(h,w,h1,w1))
