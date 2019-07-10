class Person:
 eyes_color=""
 height=0.0
 weight=0.0
 name=""
 planet=""
 def __init__(self):
  pass
 def run(self):
  print("Run")
 def sleep(self):
  print("Sleep")

dejha = Person()
dejha.eyes_color="blue"
dejha.name="Dejha Thoris"

jhon = Person()
jhon.eyes_color="brown"
jhon.name="Jhon Carter"

print(dejha.eyes_color)
print(jhon.eyes_color)
