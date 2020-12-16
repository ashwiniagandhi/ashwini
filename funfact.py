def fact():
 n=int(input('enter the given number to find fact'))
 fact=1
 for i in range(1,n+1): 
    fact=fact*i
    print(fact,end="")
fact()

def get(*a):
 print(a)
get(10,20,30)

def get(**a):
 print(a)
get(ashwini='10',raj='10',ash='12')

n = 2
fact = 1
for i in range(1,n+1): 
    fact = fact * i 
    print(fact,end="")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "sakshi")
