p="@423"
x=float(p.replace(p[0] ," "))
print(type(x),x)
print(x*3)

p="100%"
h=int(p.replace(p[len(p)-1], " "))
print(type(h),h)
print(x*h)