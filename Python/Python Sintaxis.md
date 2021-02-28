





## **¿Qué es Python?**

Python es un lenguaje de programación creado en los años 90 por Guido Van Rossum. el nombre esta inspirado en los cómicos "Monty Python". en cuanto al lenguaje podemos decir lo siguiente:

- **Python es un lenguaje de propósito general**. es decir que puede ser usado en aplicaciones de cualquier tipo.
- **Python es un lenguaje de alto nivel**. es decir que proporciona sintaxis muy simple, para que una persona pueda escribir programas en el. abstrayendo toda la complejidad de código maquina
- **Python es un lenguaje interpretado o de scripting**. esto quiere decir que el código de python necesita un programa que interpreta el código para que un computador pueda entenderlo.
- **Tipado dinámico**
- **Fuertemente tipado**
- **Multiplataforma**. puede ser ejecutado en distintos sistemas operativos.
- **Multiparadigma**. python soporta la programación Orientado a Objetos, aunque también permite programación imperativa, funcional, y orientada a aspectos
- **Comunidad Grande.** Gran cantidad de bibliotecas.


### ¿Porque aprender Python?

Existen muchas razones para aprender Python entre las que podemos encontrar:

- **Simple**. sintaxis simple, sencilla y clara, es tan sencilla que un programa puede parecer un pseudocódigo. Posee una curva de aprendizaje Amigable

- **Usado en múltiples entornos**.

- - Ciencia de datos
  - Aplicaciones científicas
  - Hacking
  - Desarrollo web backend. a través de frameworks web como Django que es usado en Instagram, Pinterest, Mozilla y muchas otros sitios
  - Aplicaciones de Escritorio, de consola o aplicaciones web
  - Juegos, a través de bibliotecas como pygame
  - Hardware o sistemas embebidos, utilizando open hardware Raspberry Pi


### ¿Cuando no usar Python?

Aunque Python es muy útil, si necesitas crear aplicaciones como estas:

- Aplicaciones de bajo nivel
- Aplicaciones de rendimiento crítico 

probablemente python no sea la mejor opción, pero considera que este tipo de aplicaciones no son creadas por la mayoría de personas y tan solo en campos muy enfocados. así que para el resto de aplicaciones comunes que usamos a diario puede ser perfectamente usado. de hecho algunas empresas que usan python puedes encontrar a: Google, Quora, Instagram, Pinterest, Bitbucket Yahoo, NASA, Ademas esta disponible en todas las distribuciones Linux, dropbox.

Implementaciones de Python

Entre las muchas destacan: Cpython, Jython, IronPython, PyPy, etc. siendo la más popular CPython.

-------

## **Sintaxis**

**Python  --version:** Nos indica la versión de python instalada (debe ejecutarse en cmd)

```python
python --version
Python 3.8.5
```

**Python:** inicia python en la consola de windows (CMD)

```python
python

>>>
```

**Print:**  Imprime caracteres en pantalla

````python
print("Hello world")
````

**Input:** Solicita al usuario que ingrese un dato.

`````python 
input("Insert your age: ")
`````

**Type:** Retorna el tipo de dato ingresado en la función.

```python
type("Hello")
type(10)
```

**Concatenar:** Se pueden sumar dos o mas strings usando el +.

`````python
print("Bye" + "World")
print("Bienveido a " + mystr)
print(f"Bienvenido a {mystr}")
print("Bienvenido a {0}".format(mystr))
`````

------

### **Tipos de datos**

#### **Strings** 

Cadena de caracteres

```python
print("Hello world")

print('Hello World')

print('''Hello World''')

print("""Hello World""")

print("Bye" + "World")
```

##### **Dir:** 

Muestra lo que se puede hacer con las variables (Métodos, etc)...

````python
dir(Variable)
print(dir(Variable))
````

Mediante **Dir** se pueden saber los métodos de los strings algunos de ellos son:

**Upper:** Todo mayusculas

````python
print(mystr.upper())
````

**Lower:** Todo Minusculas

````python
print(mystr.lower())
````

**Swapcase:** Invierte lan minusculas a mayusculas y viceversa

````python
print(mystr.swapcase())
````

**Capitalize:** Solo la inicial es mayuscula:

````python
print(mystr.capitalize())
````

**Replace: ** Reemplaza una parte del texto

````python
print(mystr.replace("Hello" , "Bye"))
````

**Replace().upper:** Reemplaza y coloca todo en mayúsculas

````python
print(mystr.replace("Hello" , "Bye").upper)
````

**Count:**  Cuenta el numero de apariciones de ese caracter

````python
print(mystr.count("l"))
````

**Startswith:** Muestra si una variable comienza por...

````python
print(mystr.startswith("Hello"))
````

**Endswith:**  Muestra si una variable termina con  (busca por caracter)

````python
print(mystr.endswith("World"))
````

**Split:** Divide un string a partir del caracter asignado

````python
print(mystr.split()) #Apartir de una espacio
print(mystr.split("o")) #Apartir de una letra
````

**Find:** Busca el indice (posicion) de un caracter

````python
print(mystr.find("o"))
````

**Len:** Arroja la cantidad de caracteres de un string

````python
print(len(mystr))
````

**Isnumeric:** Dice si el string es numerico

````python
print(mystr.isnumeric())
````

**Isalpha:** Dice si es alphanumerico

````python
print(mystr.isalpha())
````

**Imprime un caracter seleccionando por su indice (posicion):**

````python
print(mystr[5])
print(mystr[0])
print(mystr[-1])
print(mystr[-6])
````

------

#### **Numbers**

**Integer:**  Números Enteros

````python
print(30)
````

**Float:** Decimales

````python
print(30.5)
````

#####  **Operadores Aritméticos**

**Suma:**

`````python 
3 + 2

1 + 1.0 # Devuelve float
`````

**Resta:**

`````python 
3 - 2
`````

**Multiplicacion:**

`````python
3 * 2
`````

**Division:**  (Puede devolver floats)

`````python 
3 / 2
`````

**Cubo:**  (Elevar al cubo)

`````python
2 ** 3 
`````

**Modulo:**  Modulo (Devuelve el residuo de la operacion)

`````python
3 % 2
`````

**Ejemplo:**

````python
total = 3+5*20/100
````

`````python
age = input("Insert your age: ")
print(age)
new_Age = int(age) + 5
print(new_Age)
`````

------

#### **Boolean**

````python
True 
False
````

------

#### **Lists** 

Tipos de lista:

````python
[10, 20, 30, 40, 50] # Numbers
["Hello", "Bye", "Adios"] # Strings
[10, "Hello", True, 40.5] # Mixed
[]# Vacia

demo_Lists = [1, "hello", 1,34, True, [1, 2, 3]] # Variable Mixed
colors = ["red", "green", "blue"] # Variable String
````

Se define con List(( ));

````python
numbers_list = list((1, 2, 3, 4))
print(numbers_list)
````

como obtener el indice de una lista:

````python
print(colors[1])
print(demo_Lists[2])
print(colors[-1])
print(demo_Lists[-2])
````

Modificar elementos de una lista:

````python
variable[elemento] = nuevo elemento
colors[1] = "yellow"
print(colors)
````

Se pueden saber sus metodos a través de:

`````python
print(dir(variable))
`````

**Range:** crea una lista con el rango de valores asignado.

````python
variable = list(range(inicio, fin))

r = list(range(1, 100))
print(r)
````

Nota: siempre colocar un numero por encima del necesitado ya que resta un numero al valor final.

**In:** saber si un valor esta dentro de una lista 

`````python
print("valor" in variable)

print("green" in colors)
print("violet" in colors)
`````

**Append:** Agrega un elemento a la lista

`````python
variable.append("Elemento nuevo")

colors.append("White")
print(colors)
`````

**Extend:** Agrega uno o mas elementos a una lista utilizando las tuplas.

````python
Variable.extend(("elemento N" , "Elemento N"))

colors.extend(("violet" , "black"))
````

**Insert:** Agrega un elemento en una posicion o indice determinado

````python
Variable.insert(posicion , elemento)

colors.insert(-1, "grey")

colors.insert(len(colors), "cian") #Inserta en la ultima posicion
````

**Pop:** Elimina el ultimo valor de la lista o el valor indicado

`````python
variable.pop()
variable.pop(1) #Elimina el indice 1

colors.pop()
colors.pop(1)
`````

**Remove:**  Elimina un valor especifico de la lista

`````python
variable.remove( Elemento )

colors.remove("Green")
`````

**Clear:**  Limpia todos los elementos de la lista .

`````python
variable.clear()

colors.clear()
`````

**Sort:**  Ordena los elementos de forma ascendente (No mezclar tipos de datos)

`````python
varible.sort()
variable.sort(reverse=True)

colors.sort()
colors.sort(reverse=True)
`````

**Count:** Cuenta las vaces que aparece un elemento en la lista.

`````python
variable.count("elemento")
print(variable.count("elemento"))

colors.count("red")
print(colors.count("red"))
`````



#### **Tuples** 

Tipos de tupla

````python
(10, 20, 30, 40, 50) # Numbers
("Hello", "Bye", "Adios") # Strings
(10, "Hello", True, 40.5) # Mixed
()# Vacia

x = (10, 20, 30, 40, 50) # Variable Numbers
x = (10, "Hello", True, 40.5) # Variable Mixed
````

Imprimir un indice en especifico

````python
x = (1, 2, 3, 4, 5)

print(x)
print(x[3])
````

**Eliminar:** Elimina toda la tupla

````python
del variable tupla

del x
````

Se pueden combinar con diccionarios de esta manera:

````python
locations ={
	(39.12123, 35.00000) : "Tokyo"
	(12.94587, 64.39614) : "New York" 
}
````



#### **Set**  

Almacena un cojunto de elementos sin ordenarlos (Sin indice)

Se define con {}

`````python
variable = {elemento, elemento, elemento}

{"Hello", "Bye", "Adios"} # Strings
{10, "Hello", True, 40.5} # Mixed
{}# Vacia

colors = {"Red", "Green", "Blue"}
`````

**In:** saber si un valor esta dentro de una lista 

`````python
print("valor" in variable)

print("green" in colors)
print("violet" in colors)
`````

Sus metodos se pueden ver atraves de:

`````python
print(dir(variable))
`````

**Add:**  Agrega un valor a la lista  (Inicio)

`````python
variable.remove( Elemento )

colors.remove("Green")
`````

**Remove:**  Elimina un valor especifico del set

`````python
variable.remove( Elemento )

colors.remove("Green")
`````

**Eliminar:** Elimina todo el set 

````python
del variable

del x
````



#### **Dictorionies**                                                                                                                                                                                                              

````python
{
    # Clave y Valor
    "name":"Ryan",
    "lastname":"Ray",
    "nickname":"Fazt"
}
````

**None:** Dato no definido (Luego se puede asignar un dato)

````python
None
````

------

### **Variables** 

​	Es un identificador único para un objeto que se aloja en la memoria. 

​	Almacena todo tipo de datos. 

​	No puede iniciar con un numero.

```python
name = "Yoiker"
x = 100
lista = [10, 20, 30, 40, 50]
```

 **Key sensitive:**  (Sensible a mayúsculas y números)

```python
book = "Digital fortress"
Book = "Digital fortress"
```

**Variables en una linea**

```python
x1, book1 = 100, "I robot"
```

**Conventiones:** (mas sencillo de leer)

```python
book_name = "I Robot" #Snake Case
bookName = "Digital Fortress" #Camel Case
BookName = "Python para todos" #Pascal Case
```

**Reasignar Variables**:

```python
book_name1 = "I Robot"
book_name1 = 12121212
```

**Constantes:** (No se puede modificar)

```python
PI = 3.1416
```

-------

### **Condicionales**

Evalua si una declaracion es verdadera o falsa utilizando los operadores  y en base a eso lleva cabo un accion. Nos ayudan a controlar la toma de decisiones utilizando la lógica en nuestros programas. Los tipos de condicionales en python son: if, elif y else.

**Estructura de las condicionales**

- Una prueba que evalúa a verdadero o falso. (If)
- Un bloque de código que se ejecuta si la prueba es verdadero.
- Un bloque opcional de código si la prueba es falsa. (Else)

De esta manera:

````python
if test:
    code
else:
    code
````

Ejemplo:

#### **Condicionales if, else**

````python
x = int(input("Ingrese un numero"))
if x < 20:
	print("X es menor que 20")
else:
	print("X es mayor que 20")
````

#### **Condicionales if, elif y else**

````python
color = input("Ingrese un color")
if color == "Rojo":
    print("El color is Rojo")
elif color == "Azul":
    print("El color es Azul")
else:
    print("Cualquier color")
````

#### **Condicionales anidadas**

Una sentencia condicional es anidada si el bloque de código verdadero (if) o el bloque de código falso (else) contiene otra sentencia condicional. 

````python
name = "Jhon"
lastname = "Carter"

if name == "Jhon":
    if lastname == "Carter":
        print ("You are Jhon Carter.")
    else:
        print ("You are not Jhon Carter.")
else:
    print ("You are not Jhon.")
````

Nota: la indentacion debe estar colocada de forma correcta, ya que python se basa en ello para diferenciar los bloques de codigo.

------------

### **Operadores**

#### **Comparacion**

````python
> mayor que
< menor que
== igual que
= asignar
````

Logicos

And: Se deben cumplir ambas declaraciones para que un  se lleve a cabo una accion.

````python
and 

#Ejemplo

if x > 2 and x < 10:
    print ("x is greater than two and less than or equal to ten")
````

Or: Se cumple solo una de las declaraciones para llevar a cabo una accion.

````python
Or

#Ejemplo

if x > 2 or x <= 20:
    print ("x is greater than two or less than or equal to twenty")
````

Not: invierte el "resultado" arrojado en una comparacion, pasa de true a false y viceversa.

````python
not

#Ejemplo

if (not( x == y)):
    print("X is not equal y")
````



### **Bucles (For & while)**

#### **For**

Se utiliza para recorrer los elementos de un objeto *iterable* (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.

````python
for variable in elemento iterable (lista, cadena, range, etc):
    cuerpo del bucle
````

Ejemplo:

````python
foods = ["Apples", "Bread", "Cheese", "Milk", "Bananas", "Graves"]

for food in foods:
    if food == "Cheese":
        continue
        # break
        # print("Buy this")
    print(food)
````

**For - Range**

````python
for number in range(1, 8):
	print(number)
    
for letter in ("hellow"):
    print(letter)
````

##### **For en diccionarios**

Un caso es especial de bucle for se da al recorrer los elementos de un diccionario. Dado que un diccionario está compuesto por pares clave/valor, hay distintas formas de iterar sobre ellas.

1 – Recorrer las claves del diccionario.

````python
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}

for k in valores:
    print(k)

>>> A
>>> E
>>> I
>>> O
````

2 – Iterar sobre los valores del diccionario

````python
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}

for v in valores.values():
    print(v)

>>> 4
>>> 3
>>> 1
>>> 0
````

3 – Iterar a la vez sobre la clave y el valor de cada uno de los elementos del diccionario.

````python
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}

for k, v in valores.items():
    print('k=', k, ', v=', v)

>>> k=A, v=4
>>> k=E, v=3
>>> k=I, v=1
>>> k=O, v=0
````

Iterable

Es un objeto que se puede iterar sobre él, es decir, que permite recorrer sus elementos uno a uno. Para ser más técnico, un objeto iterable es aquél que puede pasarse como parámetro de la función `iter()`. Ejemplo:

````python
>>> nums = [4, 78, 9, 84]
>>> it = iter(nums)
>>> next(it)
4
>>> next(it)
78
>>> next(it)
9
>>> next(it)
84
>>> next(it)
Traceback (most recent call last):
File "<input>", line 1, in <module>
StopIteration
````

##### **for … else**

En relación al apartado anterior, Python ofrece una estructura adicional de bucle `for` cuya estructura es la siguiente:

````python
for e in iterable:
	# Tu código aquí
**else**:
	# Este código siempre se ejecuta si no se ejecutó la sentencia break en el bloque for
````

Es decir, el código del bloque `else` se ejecutará siempre y cuando no se haya ejecutado la sentencia `break` dentro del bloque del `for`.
Veamos un ejemplo:

````python
numeros = [1, 2, 4, 3, 5, 8, 6]

for n in numeros:
    if n == 3:
        break
else:
    print('No se encontró el número 3')
````

Como en el ejemplo anterior la secuencia `numeros` contiene al número `3`, la instrucción `print` nunca se ejecutará.



#### **While**

Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición. Si el resultado es True se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.

````python
while condicion:
    bloque de codigo
````

​	Ejemplo:

````python
count = 4

while count <= 20:
    print(count)
    count = count + 1
````



SENTENCIAS

break:  se utiliza para finalizar y salir el bucle, por ejemplo, si se cumple alguna condición.

````python
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)
````

Continue: salta al siguiente paso de la iteración, ignorando todas las sentencias que le siguen y que forman parte del bucle

````python
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)
````

----------

### **Funciones**

Las funciones se pueden crear en cualquier punto de un programa, escribiendo su definición.

La primera línea de la definición de una función contiene:

- la palabra reservada def
- el nombre de la función (la guía de estilo de Python recomienda escribir todos los caracteres en minúsculas separando las palabras por guiones bajos)
- paréntesis (que pueden incluir los argumentos de la función, como se explica más adelante)

Las instrucciones que forman la función se escriben con sangría con respecto a la primera línea.

Por comodidad, se puede indicar el final de la función con la palabra reservada return (más adelante se explica el uso de esta palabra reservada), aunque no es obligatorio.

Para poder utilizar una función en un programa se tiene que haber definido antes. Por ello, normalmente las definiciones de las funciones se suelen escribir al principio de los programas.

````python
def mi_funcion (parametros):
    bloque de instrucciones
    return #Reservada para devolver un valor
````

Ejemplo:

````python
def hello (name):
    print("Hello" + name)

hello(" yoiker")
hello(" yoisberth")
hello(" yois")
hello(" miguel")
````

````python
def add (numbeOne, numberTwo):
    return (numbeOne + numberTwo)

print(add(30, 10))
print(add(70, 30))
print(add(830, 44))
````

funcion lambda

````python
add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10, 30))
````

----------------------------------

### **Modulos**

Un módulo es un fichero conteniendo definiciones y declaraciones de Python. El nombre de archivo es el nombre del módulo con el sufijo `.py` agregado. Dentro de un módulo, el nombre del mismo módulo (como cadena) está disponible en el valor de la variable global `__name__`.

#### **Creacion de modulos**

¿Quieres crear tu primer módulo?

Crea un archivo con la extension .py (`mis_funciones.py`)

`````python
def saludo(nombre):
    print("Hola " + nombre)
`````

Importa y ejecuta el modulo en el archivo principal de esta manera:

````python
import mis_funciones
mis_funciones.saludo("j2logo")

>>> Hola j2logo
````

Sin embargo, ¿que está sucediendo aquí, detrás de bambalinas? Cuando importamos un módulo, Python compila ese módulo y genera un archivo .pyc, y el programa sólo se vuelve a compilar si el .py es más reciente que el archivo .pyc.

Ejemplo:

Nombre de archivo para el modulo: myname.py

````python
def print_name(n):
    print("Hola", n)
````

Archivo principal:

````python
import myname
name.print_name("Jorge")

>>> Hola Jorge
````



#### Cómo importar módulos en Python

Como has visto al final del apartado anterior, para usar las definiciones de un módulo en el intérprete o en otro módulo, primero hay que importarlo. Para ello, se usa la palabra reservada `import`. Una vez que un módulo ha sido importado, se puede acceder a sus definiciones a través del operador punto `.`.

````python
import Nombre_Modulo
Nombre_modulo.nombre_definicion(parametro)
````

##### from … import …

Podemos importar uno o varios nombres de un módulo del siguiente modo:

`````python
from mis_funciones import saludo, otra_funcion

saludo('j2logo')
`````

Esto nos permite acceder directamente a los nombres definidos en el módulo sin tener que utilizar el operador `.`.

##### from … import 

```python
from mis_funciones import *

saludo('j2logo')
```

Es similar al caso anterior, solo que importa todas las definiciones del módulo a excepción de los nombres que comienzan por guión bajo `_`.

##### **from … import as**

Por último, podemos redefinir el nombre con el que una definición será usada dentro de un módulo utilizando la palabra reservada `as`:

```python
from mis_funciones import saludo as hola
hola('j2logo')

>>>Hola j2logo
```

##### Ejecutar módulos como scripts

Un módulo puede ser ejecutado como un script o como punto de entrada de un programa cuando se pasa directamente como parámetro al intérprete de Python:

````python
python mis_funciones.py
````

Cuando esto ocurre, el código del módulo se ejecuta como si se hubiera importado, con la particularidad de que el nombre del módulo, `__name__`, es `__main__`.

Esto hace realmente interesante añadir al final del módulo las siguientes líneas de código, que solo se ejecutarán en caso de que dicho módulo se haya ejecutado como el *principal*:

````python
if __name__ == '__main__':
hola('j2logo')
````

No se ejecutarán en caso de que el módulo se importe en otro módulo.



#### **Instalar modulos de internet**

Se debe ejecutar en consola en comando `pip` junto a la descripcion correspondiente al modulo deseado. Ejemplo:

````python
# CMD
pip install colorama
````

