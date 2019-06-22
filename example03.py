def add(number1,number2):
 result = number1+number2
 print ("Add", result)
n1 = 5
n2 = 10
add(n1,n2)
print("Add",add(n1,n2))
r = add(n1,n2)
print("Add",r)

print("-------------")
print("segundo")
print("-------------")

def add(number1,number2):
 result = number1+number2
 return result
n1 = 5
n2 = 10
r = add(n1,n2)
print("Add",r)
print("Add",add(n1,n2))