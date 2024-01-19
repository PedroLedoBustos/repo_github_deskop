import random
import time
import os
# Ejercicio 1 #
    # Escribir una secuencia de instruciones en python que permita declarar 3 variables a,b y c asignandoles respectivamente 
    # los valores 1, Francia, 36.2 y luego mostrar los valores de estas variables en la consola.

a,b,c = 1, "Francia", 36.2
print(a,b,c)

# Ejecicio 2 #
    # Escribir una secuencia de instruciones en python que permita declarar una variable ch inicializandola con el valor "hola" y 
    # luego modificar esa misma variable para que contenga "esta bien". El programa debe mostrar el contenido de la variable en la consola después de la modificación.
ch = "hola"
ch = "esta bien"
print(ch)

# Ejercicio 3 #
    # Escribe una serie de instruciones en python que permita declarar 2 variables x e y asignandoles respectivamente los valores 3 y 8.5, luego convertir el typo de
    # estas variables a una cadena de caracteres. Al final, el programa debe mostrar el typo de estas variables despues de la conversión.
x,y= 3 , 8.5
x = str(x) 
y = str(y)
print(f"El tipo de x es: {type(x)} y el tipo de y es: {type(y)}")

# Ejercicio 4 #
    # Escribe un programa que pregunte al usuario su peso en Kg y lo almacene en una variable. El programa debe mostrar al final el peso introducido por el usuario.
peso= int(input("¿Cuántos Kg pesas?"))
print(f"El sujeto pesa: {peso}Kg")

# Ejercicio 5 #
    # Crear una serie de instruciones en python que permitan declarar una variable var y asignarle el valor "Hola". Luego, el programa debe verificar si la variable var 
    # es un entero o una cadena de caracteres. Si es un entero, el programa debe imprimir en la consola "Entero", y si es una cadena de caracteres, el programa imprimirá 
    # "Cadena de caracteres" en consola.
var = "Hola"
if type(var) == int:
    print("Entero")
elif type(var) == str:
    print("Cadena de caracteres")
else:
    print("No es ni entero ni cadena de caracteres.")

# Ejercicio 6 #
    # Escribir un programa que declare la variable "d" y le asigne el valor 5, y verifique si esta varaible es mayor o menor que 0. Si la variable es mayor que 0, el 
    # programa debe imprimir "Positiva", de lo contrario debe imprimir "Negativa".
    
d = 5
if d > 0:
    print("Positiva")
elif d < 0:
    print("Negativa")
else:
    print("la variable 'd' es 0")

# Ejercicio 7 #
    # Escribir un programa que solicite al usuario su edad y la almacene en una varaible. El programa debe verificar si el usuario tiene una edad mayor o menor a 18 años.
    # Si la edad del usuario es mayor o igual a 18, entonces el programa debe imprimir "El usuario es mayor de edad", de lo contrario debe imprimir "El usuario es menor de edad".

edad = int(input ("Introduce tu edad: "))
if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")

# Ejercicio 8 #
    # Escribir un programa en python que permita imprimir en la consola los números del 1 al 20. (es necesario crear dos versiones, una con for y otra con while)

lista = range(1,21)
for n in lista:
    print(n)
print("Ahora con el while")
x = 0
while x <= 20:
    print(x)
    x += 1

# Ejercicio 9 #
    # Escribir un programa en python que permita imprimir solo los numeros impares entre 10 y 20. (Es necesario crear dos versiones, una con for y otra con while)
print("Numeros impares del 10 al 20 con for: ")
numeros = range (10,21)
for n in numeros:
    if n%2 != 0:
        print(n)
print("Numeros impares del 10 al 20 con while: ")
n=10
while n in numeros:
    if n%2 !=0:
        print(n)
    n += 1

# Ejercicio 10 #
    # Escribir la instrución que permite crear una lista de numeros del 1 al 10 utilizando la comprension de lista.
print("Lista")
lista= [i for i in range(1,11)]
print(lista)

# Ejercicio 11 #
    # Escribir la instrucción que permite crear una lista de números pares del 1 al 10 con una comprensión de lista.
lista_pares= [n for n in range(1,11) if n%2==0]
print(lista_pares)

# Ejercicio 12 #
    # Escribir las instrucciones que permiten crear la lista L asignandole los valores [6,8,3,4,1,12,2,9.2], y luego 
    # ordenar los números de la lista en orden creciente. El programa debe mostrar la lista L despues de ordenar los números.

L= [6,8,3,4,1,12,2,9.2]
L.sort()
print(L)

# Ejercicio 13 #
    # Escribir las instrocciones que permiten crear la lista L asignandole los valores [3,2,2,1,9,1,2,3,7], luego calcular 
    # el número de apariciones del número 1 en la lista L.
L= [3,2,2,1,9,1,2,3,7]
print(L.count(1))

# Ejercicio 14 #
    # Escribir las instrucciones que permiten crear una lista vacia L y agregarle los enteros 10,25,30,45,90 y las cadenas de caracteres "ab", "cd","ef".
L= []
numeros= [10,25,30,45,90, "ab", "cd", "ef"]
for n in numeros:
    L.append(n)
print(L)
    # Otro método.
N= []
N += [10,25,30,45,90,"ab", "cd", "ef"]
print(N)

# Ejercicio 15 #
    # Escribir el programa que cree una lista L asignandole el valor [1,2,3,4,5,6,7,8,9,10] y luego crear una nueva lista L1 que recupera un elemento 
    # de cada tres en la lista L. En este caso, debemos obtener al final la siguiente lista: [1,4,7,10]
L= [1,2,3,4,5,6,7,8,9,10]
L1= []
for i in range(len(L)):
    if i%3 == 0:
        L1.append(L[i])
print(L1)

# Ejercicio 16 #
    # Escribe las instruciones que permitan ordenar una cadena de caracteres en orden alfabeticamente ascendente. Para probar, vamos a tomar la 
    # cadena c= "Francia". El programa debe devolver "aacfinr".
c= "francia"
c= sorted(c)
c= "".join(c)
print(c)

# Ejercicio 17 #
    # Escriba un programa que, dadas dos listas L1 y L2, devuelva una lista L3 que contenga los elementos en común entre L1 y L2.
    # Para probar, vamos a tomar las listas: L1= [9,8,7,14,3,2,"a","p","hola","b"] y L2= ["b",1,9.2,6,3,9,"p"]
L1= [9,8,7,14,3,2,"a","p","hola","b"]
L2= ["b",1,9.2,6,3,9,"p"]
L3= set(L1).intersection(set(L2))
L3= list(L3)
print(L3)

# Ejercicio 18 #
    # Escriba un programa que permita ordenar una lista de tuplas L en orden ascendente, basandose en el segundo elemento de la tupla.
    # La lista que consideramos en este ejercicio es: L=[("Manzana",15),("Banana",8),("Fresa",12),("Kiwi",9),("Melocoton",2)]
L=[("Manzana",15),("Banana",8),("Fresa",12),("Kiwi",9),("Melocoton",2)]
L.sort(key= lambda x:x[1])
print(L)

# Ejercicio 19 #
    # Escriba un programa que permita invertir una cadena de caracteres. El programa debe invertir la variable "ch" que contiene la frase "Hola a todos".
ch= "Hola a todos"
ch= ch[::-1]
print(ch)

# Ejercicio 20 #
    # Escribir un programa que muestre en la consola el valor de las claves "Manzana" y "Banana" del diccionario {"Manzana":3, "Banana":7, "Kiwi":1}
dic= {"Manzana":3, "Banana":7, "Kiwi":1}
print(dic["Manzana"])
print(dic["Banana"])

# Ejercicio 21 #
    # Escribir un programa que permita sumar los valores del siguiente dicionario: {"Manzana":15, "Banana":8, "Fresa":12, "Kiwi":9, "Melocoton":2}
dic= {"Manzana":15, "Banana":8, "Fresa":12, "Kiwi":9, "Melocoton":2}
sumaValor= sum(dic.values())
print(sumaValor)

# Ejercicio 22 #
    # Escribir un programa que permita truncar el numero decimal a 2 cifras despues de la coma. Por ejemplo, si tomamos el numero decimal 187.632587, el programa debera mostrar 187.63
print(float("{:.2f}".format(187.632587)))

# Ejercicio 23 #
    # Escribir un programa que permita formatear la cadena de caracteres: "Me llamo miNombre y tengo edad años. Estoy aprendiendo el lenguaje Lenguaje". El programa debe permitir 
    # formatear esta cadena asignandole el contenido de las variables: miNombre= "julien", edad= 32, Lenguaje "Python". El programa mostrara en consola: "Me llamo Julien y tengo 
    # 32 años. Estoy aprendiendo el lenguaje Python"
miNombre= "Julien"
edad= 32
lenguaje= "Python"
frase= f"Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo el lenguaje {lenguaje}"
print(frase)

# Ejericio 24 #
    # Escribir un programa qyue muestre la tabla de multiplicación del número 8. El programa debe devolver la siguiente salida: 8x0=0, 8x1=8... 8x10=80.
numero= 8
for n in range(0,11):
    print(f"{numero} x {n}= {numero*n}")

# Ejericio 25 #
    # Escribir un programa que muestre la carpeta en la que se encuentra el script Python actual.
print(os.getcwd())

# Ejercicio 26 #
    # Escribir un programa que permita eliminar un elemento de una lista. Consideramos la lista L= [1,2,3,4,5] y queremos eliminar el número 1.
L= [1,2,3,4,5]
L.remove(1)
print(L)

# Ejericio 27 #
    # Escribir un programa que permita recuperar la extension de un archivo.
ruta_arcivo= r"C:/Users/pedro/OneDrive/Escritorio/Ejercicios Python/Ejercicios principiantes.py"
nombre_archivo= os.path.basename(ruta_arcivo)
extension_archivo= nombre_archivo.split(".")[-1]
print(f"Extensión archivo: {extension_archivo}")

# Ejercicio 28 #
    # Escriba un programa que permita calcular el tiempo de ejecución de un script. Tomemos como ejemplo el script del ejercicio 24 y 
    # calculemos su tiempo de ejecución. El programa debe mostrar al final la tabla de multiplicación del ejercicio 24 junto con el tiempo de ejecición.
inicio= time.time()
numero= 8
for n in range(0,11):
    print(f"{numero} x {n}= {numero*n}")
final= time.time()
print(f"Tiempo de ejecución del código = {final - inicio}")

# Ejercicio 29 #
    # Escdriba un programa que permita mezclar aleatoriamente los elementos de una lista L. Tomemos por ejemplo la lista L [3,6,8,7,2,"s","ch","d"]
L= [3,6,8,7,2,"s","ch","d"]
random.shuffle(L)
print(L)

# Ejericio 30 #
    # Escriba un programa para generar aleatorimente un numero entre 20 y 30.
numeroAleatorio= random.randint(20,30)
print(numeroAleatorio)

# Ejercicio 31 #
    # Escribe un programa que muestre los siguientes numeros en la consola (8 * (5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

contador=1
while contador<=8:
    print("5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20")
    contador += 1

# Ejercicio 32 #
    # Escribir un programa que cree la variable L y le asigne la lista [3,6,9,12,15,18,21,24]. Luego crear una nueva lista L1 
    # mediante una comprension de lista que contenga los numeros de L divididos por 3. El programa debe mostrar la lasta L1 en la consola.
L = [3,6,9,12,15,18,21,24]
L1= [i//3 for i in L]
print(L1)


