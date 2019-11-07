n=int(input("enter the number:"))
factorial=1
if n<0:
  print("Negative numbers are not allowed for a factorial")
if n==0:
  print("1")
else:
  for i in range(1,n+1):
     factorial=factorial*i
print(factorial)  
