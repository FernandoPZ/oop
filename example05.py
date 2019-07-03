class Hello:
 def __init__(self):
  pass
 def add (self,number1, number2):
  return number1+number2
 def div (self,number1, number2):
  return number1/number2
object = Hello()
print("Add", object.add (5,6))
print("Div", object.div (5,6))
