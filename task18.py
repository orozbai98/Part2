i = 0
c = 1
a = int(input("vash vozrast"))
b = a%2
if b==0:
    while i <= a:
        print(i)
        i = i + 2
elif b==1:
    while c <= a:
        print(c)
        c = c + 2
    