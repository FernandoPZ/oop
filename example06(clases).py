class Operations:
 def __init__(self):
  pass

#Areas

#Cuadrado
 def area_cuadrado (self,lado):
  return lado*lado

#Circulo
 def area_circulo (self,radio):
  return 3.1415926535897932384626433832795028841971694*(radio*radio)

#Triangulo
 def area_triangulo (self,base,altura):
  return (base*altura)/2

#Trapecio
 def area_trapecio (self,lado,base_menor,base_mayor,altura):
  return ((base_menor+base_mayor)*altura)/2

#Perimetros

#Cuadrados
 def perimetro_cuadrado (self,lado):
  return lado*4

#Circulo
 def perimetro_circulo (self,radio):
  return 2*3.1415926535897932384626433832795028841971694*radio

#Triangulo
 def perimetro_triangulo (self,lado1,lado2,lado3):
  return lado1+lado2+lado3

#Trapecio
 def perimetro_trapecio (self,lado1,lado2,lado3,lado4):
  return lado1+lado2+lado3+lado4

object = Operations()
print("Bienvenido al menu de de areas y perimetros")
print("Escoja una opcion: ")
print("[1] Area de un cuadrado")
print("[2] Area de un circulo")
print("[3] Area de un triangulo")
print("[4] Area de un trapecio")
print("[5] Perimetro de un cuadrado")
print("[6] Perimetro de un circulo")
print("[7] Perimetro de un triangulo")
print("[8] Perimetro de un trapecio")
eleccion=int(input("Escoja una opcion valida: \n"))

#opcion1
if eleccion == 1:
 lado=float(input("ingrese el lado del cuadrado: \n"))
 print("Area del cuadrado", object.area_cuadrado (lado))

#opcion2
elif eleccion == 2:
 radio=float(input("ingrese el radio del circulo: \n"))
 print("Area del circulo", object.area_circulo (radio))

#opcion3
elif eleccion == 3:
 base=float(input("ingrese la base del triangulo: \n"))
 altura=float(input("ingrese la altura del triangulo: \n"))
 print("Area del triangulo", object.area_triangulo (base,altura))

#opcion4
elif eleccion == 4:
 base_mayor=float(input("ingrese la base mayor del trapecio: \n"))
 base_menor=float(input("ingrese la base menor del trapecio: \n"))
 altura=float(input("ingrese la altura: \n"))
 print("Area del trapecio", object.area_trapecio (base_mayor,base_menor,altura))

#opcion5
elif eleccion == 5:
 lado=float(input("ingrese el lado del cuadrado: \n"))
 print("Perimetro del cuadrado", object.perimetro_cuadrado (lado))

#opcion6
elif eleccion == 6:
 radio=float(input("ingrese el radio del circulo: \n"))
 print("Perimetro del circulo", object.perimetro_circulo (radio))

#opcion7
elif eleccion == 7:
 lado1=float(input("ingrese un lado del triangulo: \n"))
 lado2=float(input("ingrese otro lado del triangulo: \n"))
 lado3=float(input("ingrese otro lado del triangulo: \n"))
 print("Perimetro del triangulo", object.perimetro_triangulo (lado1,lado2,lado3))

#opcion8
elif eleccion == 8:
 lado1=float(input("ingrese un lado del trapecio: "))
 lado2=float(input("ingrese otro lado del trapecio: "))
 lado3=float(input("ingrese otro lado del trapecio: "))
 lado4=float(input("ingrese otro lado del trapecio: "))
 print("Perimetro del trapecio", object.perimetro_trapecio (lado1,lado2,lado3,lado4))

else:
 print("No es una de las opciones validas")
print("Fin del programa")
