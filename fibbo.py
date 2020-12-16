a=10
b=20
n=int(input("enter to print fibbo series"))
for i in range(1,n):
  c=a+b
  a=b
  b=c
  print(c)
