
l,b,h,m=120,122,2,2
size = ""
if l*b*h >= 1000000 or (l >= 150 or b >= 150 or h >= 150) or m >= 20:
    size = "SPECIAL"
elif l*b*h < 1000000 or m < 20:
    size = "STANDARD"
elif l*b*h >= 1000000 and m >= 20:
    size = "NOT-SHIPPED"


print(size)
