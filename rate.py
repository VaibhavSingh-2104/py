hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h<40:
  print(h*r)
elif h>40:
  nh = h-40
  nr = r*1.5
  result = (nh*nr)+(40*r)
print(result)
