#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

cadena_texto = 'La cadena de prueba'

def frecuencia_letras(cadena_texto):
    texto_sin_espacios = cadena_texto.replace(' ','').lower() #La cadena de texto elimina espacios y convierte a minusculas todo.
    diccionario_frecuencias = {}
    for letra in texto_sin_espacios:
        if letra in diccionario_frecuencias:
            diccionario_frecuencias[letra] += 1
        else:
            diccionario_frecuencias[letra] = 1
    return diccionario_frecuencias
    
conteo_letras = frecuencia_letras(cadena_texto)
print(conteo_letras)
        


#2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

lista_numerica = [2, 4, 6, 23, 66, 75, 755]

def doble_valor(valor):
    return valor * 2

valores_doblados = list(map(doble_valor, lista_numerica))
print(valores_doblados)



#3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original 
# que contengan la palabra objetivo.

lista_palabras = ['pastel', 'azucar', 'mesa', 'arcoiris', 'libro']

def palabra_buscada(palabra_objetivo, lista_palabras):
    lista_nueva = []
    for palabras in lista_palabras:
        if palabra_objetivo in palabras:
            lista_nueva.append(palabra_objetivo)
    return lista_nueva

listado_nuevo = palabra_buscada('mesa', lista_palabras)
print(listado_nuevo)




#4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

lista_num1 = [4, 6, 7, 3, 8]
lista_num2 = [7, 4, 2, 7, 3]

def diferencia_listados(n1, n2):
    return n1 - n2 #funcion por defector para restar dos parametros
    
lista_resultado = list(map(diferencia_listados, lista_num1, lista_num2))
print(lista_resultado)   




"""5 Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado."""

listado_notas = [3, 6, 7, 9, 9, 5, 3]

def media_notas(notas, nota_aprobado = 5):
    media = sum(notas) / len(notas) #obtiene la media del listado de notas entre la cantidad de las notas.
    estado = 'aprobado'
    if media >= nota_aprobado:
        estado = 'Aprobado'
    else:
        estado = 'Suspenso'

    return media, estado

resultado_media = media_notas(listado_notas)
print(resultado_media)



#6 Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial_resultado = factorial(3)
print(factorial_resultado)



#7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

lista_tuplas = [(4, 5, 7), ('botas', 'azucar', 'atun'), (5, 6, 'patatas')]

def conversion_string(tupla):
    return str(tupla) #convierte la tupla en string.

string_tupla = list(map(conversion_string, lista_tuplas))
print(string_tupla) 



"""8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no"""

def division():
    try:
        numerador = float(input('Por favor ingrese el numerador:'))
        denominador = float(input('Por favor ingrese el denominador:'))
        resultado_division = numerador / denominador
        print(f'El resultado de la division es: {resultado_division}')
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    
    except ValueError:
        print('No se puede introducir un valor no numerico')
division()




"""9 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""

mis_mascotas = ['Mapache', 'Leon', 'Oso hormiguero', 'Oso', 'Golden Retriever', 'Pajarito', 'Gato', 'Tiburon', 'Avestruz']
mascotas_prohibidas = ['Mapache', 'Serpiente Piton', 'Cocodrilo', 'Oso']

def mis_mascotas_aceptadas(mascotas):
    return mascotas not in mascotas_prohibidas

mascotas_aceptadas = list(filter(mis_mascotas_aceptadas, mis_mascotas))
print(mascotas_aceptadas)






 #10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

lista_num = [23, 76, 35, 53]

class ListaVaciaError(Exception):

    def __init__(self, mensaje='La lista está vacia, no se puede calcular el promedio'):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def promedio(lista):
    if not lista:  # Verifica si la lista está vacía
        raise ListaVaciaError()
    
    return sum(lista) / len(lista)

try:
    resultado = promedio(lista_num)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"Error: {e}")




"""11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente"""

def edad():
    try:
        edad_usuario = int(input(f'Por favor indique su edad:'))
        if 0 <= edad_usuario <= 120:
            print(f'El usuario tiene {edad_usuario} años')
        else:
            print('La edad del usuario no se encuentra en el rango [0-120 años]')
    except ValueError:
        print('El valor introducido no es valido como edad')

edad()




#12 Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

frase = "Me encanta el chocolate" 

def longitud_palabras(palabra):
    return len(palabra)
   
listado_longitudes = list(map(longitud_palabras, frase.split()))
print(listado_longitudes)





#13 Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la funcion map()

caracteres = 'Nueces'

def conversion_mayusc_minusc(palabra):
    for letra in palabra:
        return letra.upper(), letra.lower() 

letras = list(map(conversion_mayusc_minusc, set(caracteres)))
print(letras)






#14 Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

palabras = ['pez', 'mono', 'perro', 'gato', 'pantera']
letra = 'p'

def primera_letra(palabra):
    return palabra[0].lower() == letra.lower()

palabras_filtradas = list(filter(primera_letra,palabras))
print(palabras_filtradas)






#15 Crea una función lambda que  sume 3 a cada número de una lista dada.

lista_numeros = [4, 6, 2, 6]

suma_lambda = lambda x: x + 3
print(list(map(suma_lambda, lista_numeros)))





#16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

texto = 'Hoy hace mucho frio'
n = 3

def palabras_longitud_min(texto):
    return len(texto) > n

lista_palabras_filtradas = list(filter(palabras_longitud_min,texto.split()))
print(lista_palabras_filtradas)





#17 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, (5,7,2) corresponde al número quinientos setenta y dos (572). Usa la función reduce()

lista = [5, 7, 2]

from functools import reduce

concatenado = int(reduce(lambda x, y: str(x) + str(y), lista))
print(concatenado)




"""18 Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter 
para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()"""

estudiantes = [
    {'nombre': 'Pablo', 'edad': 25, 'calificacion': 78},
    {'nombre': 'Mariana', 'edad': 23, 'calificacion': 80},
    {'nombre': 'Anastasia', 'edad': 21, 'calificacion': 89},
    {'nombre': 'Pedro', 'edad': 25, 'calificacion': 94},
    {'nombre': 'Olga', 'edad': 25, 'calificacion': 67},
    {'nombre': 'Maria', 'edad': 26, 'calificacion': 45},
    {'nombre': 'Sergio', 'edad': 23, 'calificacion': 99}
]

calificacion_sobresaliente = list(filter(lambda x: x['calificacion'] >= 90,estudiantes))
for estudiante in calificacion_sobresaliente:
    print(f'El estudiante {estudiante['nombre']} ha obtenido una una de {estudiante['calificacion']}') 




#19 Crea una función lambda que filtre los números impares de una lista dada.

numeros = [2, 4, 3, 3, 7, 9, 6, 2, 4, 4, 4]

filtrar_impares = list(filter(lambda x: x % 2 != 0, numeros))
print(filtrar_impares)





#20 Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista = [54, 'patata', 'chocolate', 64, 73, 'hola']

lista_valores_int = list(filter(lambda x: isinstance(x, int),lista)) #añado isinstance para que solo cuente valores integer
print(lista_valores_int)





#21 Crea una función que calcule el cubo de un número dado mediante una función lambda

num_al_cubo = lambda x: x ** 3
print(num_al_cubo(2))





#22 Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce

lista_num = [3, 2, 6, 2, 5]
producto_total = reduce(lambda x, y: x * y, lista_num)
print(producto_total)





#23 Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce

listado_palabras = ['me','quiero', 'comer', 'un', 'pulpo']
concatenado = reduce(lambda x, y: x + ' ' + y, listado_palabras)
print(concatenado)





#24 Calcula la diferencia total en los valores de una lista. Usa la función reduce().
from functools import reduce

listado_num = [4, 2, 2, 1]
diferencia_valores = reduce(lambda x, y: x - y, listado_num)
print(diferencia_valores)





#25 Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena_texto = 'como me gusta el buen cafe'

def conteo_caracteres(texto):
    return len(texto.replace(' ', '')) #se añade replace para no contar los espacios de la cadena de texto.

cantidad_caracteres = conteo_caracteres(cadena_texto)
print(cantidad_caracteres)





#26 Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y: x % y

print(resto_division(4,3))





#27 Crea una función que calcule el promedio de una lista de números.

lista_numerica = [500, 234, 142, 288, 232, 124, 42]

def promedio(valores):
    promedio_lista = sum(valores) / len(valores)
    return promedio_lista

resultado_promedio = promedio(lista_numerica)
print(resultado_promedio)




#28 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

listado = [4, 55, 'azucar', 'pan', 54, 'pan']

def elemento_repetido(lista):
    lista_repetido = []
    for palabra in listado:
        if palabra in lista_repetido:
            return palabra
        else:
            lista_repetido.append(palabra)

palabra_repetida = elemento_repetido(listado)
print(palabra_repetida)





#29 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

contraseña = '45337687'

def enmascarar(contraseña):
    longitud_contraseña = len(contraseña)
    for caracter in contraseña:
        ultimos_digitos = contraseña[-4:] 
        mascara = '#' * (longitud_contraseña - 4)
        return  mascara + ultimos_digitos
    
contraseña_enmascarada = enmascarar(contraseña)
print(contraseña_enmascarada)




#30 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

palabra1 = 'botines'
palabra2 = 'bisonte'

def palabras_anagramas(p1, p2):
    palabra_ordenada1 = sorted(palabra1.lower())
    palabra_ordenada2 = sorted(palabra2.lower()) 

    if palabra_ordenada1 == palabra_ordenada2:
        print('Son anagramas')
    else:
        print('No son anagramas')

comprobacion = palabras_anagramas(palabra1, palabra2)
 



"""31 Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción."""


def buscar_nombre():
    try:
        entrada_nombres = input('Introduce los nombres para el listado')
        listado_nombres = [nombre.strip() for nombre in entrada_nombres.split(',')]

        if not listado_nombres or listado_nombres == [""]:
            raise ValueError('El listado no puede estar vacio')

        nombre_buscado = input('Introduce el nombre que desear buscar de la lista introducida: ').strip()


        if nombre_buscado in listado_nombres:
            print(f'El nombre {nombre_buscado} se ha encontrado en el listado introducido')
        else:
            raise ValueError(f'El nombre {nombre_buscado} no se enuentra en el listado introducido')
    
    except ValueError as e:
        print(f'Error:{e}')

buscar_nombre()




"""32 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí"""

empleados = [
    {'nombre': 'Jesus', 'Puesto': 'Becario'},
    {'nombre': 'Marian', 'Puesto': 'Manager'},
    {'nombre': 'Ana', 'Puesto': 'Informatico'},
    {'nombre': 'Pepe', 'Puesto': 'Recruiter'}   
]

def puesto_empleado(empleado, listado):
    for nombre in listado:
        if nombre['nombre'] == empleado:
            return nombre['Puesto']
    return 'Este empleado no forma parte de la empresa'

print(puesto_empleado('Pepe', empleados)) 




#33 Crea una función lambda que sume elementos correspondientes de dos listas dadas.

listado1 = [1, 32, 31, 64, 5, 2]
listado2 = [4, 22, 23, 25, 7, 9]

sumatorio = lambda x, y: [x + y for x, y in zip(x, y)]
print(sumatorio(listado1, listado2))





"""34 Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. 
Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
El objetivo es implementar estos métodos para manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas
Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol.
"""

class Arbol():
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self): #funcion para crecer la longitud de tu tronco
        self.tronco += 1
    
    def nueva_rama(self): #funcion incremento de ramas en tu arbol
        self.ramas.append(1)

    def crecer_ramas(self): #funcion crecimiento de las ramas de tu arbol
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_ramas(self, indice): #funcion para eliminar ramas de tu arbol
        if 0 <= indice < len(self.ramas):
            del self.ramas[indice]
        else:
            return 'El índice no es válido'

    def info_arbol(self): #funcion para ver la informacion de tu arbol con todas sus caracteristicas
        return {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitud_ramas': self.ramas
        }
    
manzano = Arbol()
print('arbol creado:',manzano.info_arbol())

manzano.crecer_tronco()
print('El tronco del arbol ha crecido',manzano.info_arbol())

manzano.nueva_rama()
print('Ha crecido una nueva rama en tu arbol:', manzano.info_arbol())

manzano.crecer_ramas()
print('Las ramas de tu arbol han crecido :', manzano.info_arbol())

manzano.nueva_rama()
manzano.nueva_rama()
print('Ha crecido 2 ramas nuevas en tu arbol:', manzano.info_arbol())

manzano.quitar_ramas(1)
print('Ha caido una rama de tu arbol:', manzano.info_arbol())


print('Tu arbol tiene las siguientes caracteristicas:',manzano.info_arbol())





"""36 Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
 Código a seguir:
1 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2 Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
4 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
 
 Caso de uso:
 1 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 2 Agregar 20 unidades de saldo de "Bob".
 3 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
 4 Retirar 50 unidades de saldo a "Alicia"."""

class UsuarioBanco():
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad_retirada):
        if not self.cuenta_corriente:
            return f'Error: {self.nombre} no tiene cuenta corriente y no puede retirar dinero.'
        
        if cantidad_retirada > self.saldo:
            return 'No hay saldo suficiente para realizar el retiro.'
        
        self.saldo -= cantidad_retirada
        return f'{self.nombre} ha retirado {cantidad_retirada}. Saldo actual: {self.saldo}'

    def transferir_dinero(self, usuario_transferir, cantidad_transferir):
        if not self.cuenta_corriente:
            return f'Error: {self.nombre} no tiene cuenta corriente y no puede transferir dinero.'
        
        if self.saldo < cantidad_transferir:
            return 'No se puede realizar la transferencia por saldo insuficiente.'

        self.saldo -= cantidad_transferir
        usuario_transferir.saldo += cantidad_transferir
        return (f'Se ha realizado una transferencia de {cantidad_transferir} de {self.nombre} a {usuario_transferir.nombre}. '
                f'Saldo actual de {self.nombre}: {self.saldo}. Saldo actual de {usuario_transferir.nombre}: {usuario_transferir.saldo}')

    def agregar_dinero(self, cantidad_ingreso):
        if cantidad_ingreso <= 0:
            return 'La cantidad a ingresar debe ser mayor a 0.'

        self.saldo += cantidad_ingreso
        return f'{self.nombre} ha ingresado {cantidad_ingreso}. Saldo actual: {self.saldo}'

#usuarios
usuario1 = UsuarioBanco('Alicia', 100, True)
usuario2 = UsuarioBanco('Bob', 50, True)


print(usuario2.agregar_dinero(20))       # Bob agrega 20 unidades
print(usuario2.transferir_dinero(usuario1, 80))  # Bob transfiere 80 unidades a Alicia
print(usuario1.retirar_dinero(50))       # Alicia retira 50 unidades





"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , contar_palabras , eliminar_palabra . 
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto. 
Código a seguir:
1 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2 Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
3 Crear una función eliminar_palabra para eliminar una palabra del texto.Tiene que devolver el texto con la palabra eliminada.
4 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto"""

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabras(texto, palabra_eliminar):
    palabras = texto.split()
    texto_modificado = ' '.join([palabra for palabra in palabras if palabra != palabra_eliminar])
    return texto_modificado

def procesar_texto(opcion, texto, *args):
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar' and len(args) == 2:
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == 'eliminar' and len(args) == 1:
        palabra_eliminar = args[0]
        return eliminar_palabras(texto, palabra_eliminar)
    else:
        return 'Error: No has ingresado los parámetros válidos para la función deseada.'
    
texto = 'Las tortugas van despacio y comen rapido'
print(procesar_texto('contar', texto))
print(procesar_texto('reemplazar', texto, 'tortugas','vacas'))
print(procesar_texto('eliminar', texto, 'rapido'))






#38 Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
import datetime

hora_actual = datetime.datetime.now().strftime('%H:%M')
hora = int(hora_actual[:2])

if 6 <= hora < 12:
    print(f'Es por la mañana, son las {hora_actual}')
elif 12 <= hora < 19:
    print(f'Es por la tarde, son las {hora_actual}')
else:
    print(f'Es por la noche, son las {hora_actual}')






"""39  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
0 - 69 insuficiente
70 - 79 bien
80 - 89 muy bien
90 - 100 excelente"""

try:

    nota_examen = int(input('Por favor introduzca la nota obtenida en el examen: '))

    if 0 <= nota_examen <= 69:
        print(f'La nota obtenida en el examen es de {nota_examen} - Insuficiente')
    elif nota_examen <= 79:
        print(f'La nota obtenida en el examen es de {nota_examen} - Bien')
    elif nota_examen <= 89:
        print(f'La nota obtenida en el examen es de {nota_examen} - Muy bien')
    elif nota_examen <= 100:
        print(f'La nota obtenida en el examen es de {nota_examen} - Excelente')
    else:
        raise ValueError('El valor introducido no es valido como nota de examen')
    
except ValueError:
    print('Error; Instroduzca un valor valido entre 0-100')
 




"""40 Escribe una función que tome dos parámetros: figura una cadena que puede ser "rectangulo" , "circulo" o "triangulo") y datos (una tupla con los datos necesarios para 
calcular el área de la figura)"""
import math

def calculo_area(figura,*args):
    if figura == 'rectangulo':
        if len(args) != 2:
            return 'Para calcular el area de un rectangulo necesitas introducir la base y altura'
        base, altura = args
        return base * altura

    elif figura == 'circulo':
        if len(args) != 1:
            return 'Para calcular el area de un circulo necesitar poner el valor del radio'
        radio = args[0]
        return math.pi * (radio ** 2)
    
    elif figura == 'triangulo':
        if len(args) != 2:
            return 'Es necesario poner el valor de la base y altura para calcular el area de un triangulo'
        base, altura = args
        return (base * altura) / 2
    else:
        return 'La figura que indicas no se puede calcular'

print('El area del rectangulo es', calculo_area('rectangulo', 2, 5))
print('El area del circulo es', calculo_area('circulo', 2))
print('El area del triangulo es', calculo_area('triangulo', 2, 5))    





"""41 En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python"""

precio_articulo = float(input('Por favor ingresa el valor del articulo que desear comprar'))
activar_descuento = input('Si dispones de algun descuento, por favor indicalo').lower()


if activar_descuento == 'si':
    descuento_aplicable = float(input('Ingrese el valor del cupon que desea aplicar a su compra'))
    if 0 < descuento_aplicable <= precio_articulo:
        valor_articulo =  precio_articulo - descuento_aplicable
        print(f'el valor del articulo final es de {valor_articulo}')
elif activar_descuento == 'no':
    print(f'el valor del articulo final es de {precio_articulo}')
else:
    print('El valor indicado no es valido')

