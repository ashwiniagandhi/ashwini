num=int(input("enter the number"))
for i in range (2,num):
   if num%i==0:
     print(num,"the given number is not prime")
     break
   else:
          print (num,"the given number are prime")
          break
