n1 = 20
n2 = 10

def addition():
  sum = n1 + n2
  print(sum)

def substraction():  
   sub = n1 - n2
   print(sub)

def multipl():
   mul = n1 * n2
   print(mul)

def division():
   div = n1/n2
   print(div)

addition()
substraction()
multipl()
division()

print("**********************************")


def addition(num1, num2):
  sum = num1 + num2
  print(sum)
  return sum

def substraction(num1, num2):  
   sub = num1 - num2
   print(sub)
   return sub

def multipl(num1, num2):
   mul = num1 * num2
   print(mul)
   return mul

def division(num1, num2):
   div = num1/num2
   print(div)
   return div

print(addition(10, 5))
print(substraction(10, 5))
print(multipl(10, 5))
print(division(10, 5))