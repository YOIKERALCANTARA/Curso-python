mystr = "Hello World"

#Concatenar

print("Bienveido a " + mystr)
print(f"Bienvenido a {mystr}")
print("Bienvenido a {0}".format(mystr))

# Muestra lo que se puede hacer con las variables (Metodos, etc)...
#print(dir(mystr))

#Metodos

#Todo mayusculas
print(mystr.upper())

#Todo Minusculas
print(mystr.lower())

#Invierte lan minusculas a mayusculas y viceversa
print(mystr.swapcase())

#Solo la inicial es mayuscula
print(mystr.capitalize())

#Reemplaza una parte del texto
print(mystr.replace("Hello" , "Bye"))

#Unir Metodos
#Reemplaza y coloca todo en mayusculas
print(mystr.replace("Hello" , "Bye").upper)

#Cuenta el numero de apariciones de ese caracter
print(mystr.count("l"))

#Muestra si una variable comienza por: (busca por caracter)
print(mystr.startswith("Hello"))

#Muestra si una variable termina con: (busca por caracter)
print(mystr.endswith("World"))

#Divide un string a partir del caracter asignado
print(mystr.split()) #Apartir de una espacio
print(mystr.split("o")) #Apartir de una letra

#Busca el indice (posicion) de un caracter
print(mystr.find("o"))

#Arroja la cantidad de caracteres de un string
print(len(mystr))

#Dice si el string es numerico
print(mystr.isnumeric())

#Dice si es alphanumerico
print(mystr.isalpha())

#Imprime un caracter seleccionando por su indice (posicion)
print(mystr[5])
print(mystr[0])
print(mystr[-1])
print(mystr[-6])