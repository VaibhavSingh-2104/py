largest = None
smallest = None
numbers_list =[]
while True:
    num= input("Enter a number: ")
    if num == 'done' :
        break
    try:
        value = numbers_list.append(int(num))
    except:
        print("Invalid input")
        continue

for value in numbers_list:
    if largest is None:
         largest = value
    elif value > largest:
         largest = value

    if smallest is None:
         smallest = value
    elif value < smallest:
         smallest = value

print("Maximum is", largest)
print("Minimum is", smallest)
