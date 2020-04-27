def computepay(h,r):
    if h<=40:
      result = print(h*r)
    elif h>40:
      nh = h-40
      nr = r*1.5
      result = (nh*nr)+(40*r)

      return result

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print(p)
