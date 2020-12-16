n=int(input("enter the number"))
for i in range (1,n):
    for j in range(2,i):
       if(i%j)==0:
           break
       else:
           print ("the given number are prime",i)
           break
