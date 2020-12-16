numbers=(23,0,35,1,24,5,9)
d=len(numbers)
if(d%2)==0:
    print('i am even',numbers[:2],numbers[-2:])
else:
    n=(len(numbers)/2) 
    print(numbers[n])
