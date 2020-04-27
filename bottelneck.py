numbers_list =[]
a=input("enter length:")
while True:
    num= input("Enter a number: ")
    if len(num) == a :
        break
value = numbers_list.append(num)

for i,j in value:
    if a[i]<a[j]:
        new_val=remove(a[i])
        print(len(new_value))
    else:
        continue
