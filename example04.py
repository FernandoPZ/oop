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
#Areas
if eleccion == 1:
    #Cuadrado
    lado=float(input("ingrese el lado del cuadrado: \n"))
    def area_cuadrado(lado):
        area_cuadrado=lado*lado
        print("El area del cuadrado es: ",area_cuadrado)
    area_cuadrado(lado)
elif eleccion == 2:
    #Circulo
    radio=float(input("ingrese el radio del circulo: \n"))
    def area_circulo(radio):
        area_circulo=3.1416*(radio*radio)
        print("El area del circulo es: ",area_circulo)
    area_circulo(radio)
elif eleccion == 3:
    #Triangulo
    base=float(input("ingrese la base del triangulo: \n"))
    altura=float(input("ingrese la altura del triangulo: \n"))
    def area_triangulo(base,altura):
        area_triangulo=(base*altura)/2
        print("El area del triangulo es: ",area_triangulo)
    area_triangulo(base,altura)
elif eleccion == 4:
    #Trapecio
    base_mayor=float(input("ingrese la base mayor del trapecio: \n"))
    base_menor=float(input("ingrese la base menor del trapecio: \n"))
    altura=float(input("ingrese la altura: \n"))
    def area_trapecio(base_menor,base_mayor,altura):
        area_trapecio=((base_menor+base_mayor)*altura)/2
        print("El area del trapecio es: ",area_trapecio)
    area_trapecio(base_menor,base_mayor,altura)
#Perimetro
if eleccion == 5:
    #Cuadrado
    lado=float(input("ingrese el lado del cuadrado: \n"))
    def perimetro_cuadrado(lado):
        perimetro_cuadrado=lado*4
        print("El perimetro del cuadrado es: ",perimetro_cuadrado)
    perimetro_cuadrado(lado)
elif eleccion == 6:
    #Circulo
    radio=float(input("ingrese el radio del circulo: \n"))
    def perimetro_circulo(radio):
        perimetro_circulo=2*3.1416*radio
        print("El perimetro del circulo es: ",perimetro_circulo)
    perimetro_circulo(radio)
elif eleccion == 7:
    #Triangulo
    lado1=float(input("ingrese un lado del triangulo: \n"))
    lado2=float(input("ingrese otro lado del triangulo: \n"))
    lado3=float(input("ingrese otro lado del triangulo: \n"))
    def perimetro_triangulo(lado1,lado2,lado3):
        perimetro_triangulo=lado1+lado2+lado3
        print("El perimetro del triangulo es: ",perimetro_triangulo)
    perimetro_triangulo(lado1,lado2,lado3)
elif eleccion == 8:
    #Trapecio
    lado1=float(input("ingrese un lado del trapecio: "))
    lado2=float(input("ingrese otro lado del trapecio: "))
    lado3=float(input("ingrese otro lado del trapecio: "))
    lado4=float(input("ingrese otro lado del trapecio: "))
    def perimetro_trapecio(lado1,lado2,lado3,lado4):
        perimetro_trapecio=lado1+lado2+lado3+lado4
        print("El perimetro del trapecio es: ",perimetro_trapecio)
    perimetro_trapecio(lado1,lado2,lado3,lado4)
else:
    print("No es una de las opciones validas")
print("Fin del programa")
