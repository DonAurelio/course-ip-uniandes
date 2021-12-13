# NIVEL 3. LECCIÓN 9. RECORRIDO DE DICIONARIOS

**¿Por qué necesitamos recorrer la información de un diccionario?** En el momento en que se requiere procesar la información que se encuentra almacenada en un diccionario se hace necesario recorrerlo.

**¿Cómo podemos recorrer la información de un diccionario?** Hay dos formas de recorrer un diccionario: **recorriendo las llaves** o **recorriendo los valores**. Dependiendo de la naturaleza del problema es posible determinar cuál de las formas de recorrido usar.

Considere el siguiente directorio de teléfonos representado por un diccionario.

```python
directorio = {
    "Juan": "300 235 87 45",
    "Luis": "311 986 47 00",
    "Ana": “320 700 62 15",
    "María": “312 958 88 50",
}
```
El **recorrido por las llaves**, es llevado a cabo por la instrucción `for-in`, recorre únicamente las llaves del diccionario como se muestra en el siguiente ejemplo

**Ejemplo 1**
```python 
for cada_elemento in directorio:
    print(cada_elemento)
```

*Salida*
```python 
Juan
Luis
Ana
Maria
```

**Ejemplo 2**
```python 
for cada_elemento in directorio.keys():
    print(cada_elemento, ”->”, directorio[cada_elemento])
```

*Salida*
```python 
Juan -> 300 235 87 45
Luis -> 311 986 47 00
Ana -> 320 700 62 15
Maria -> 312 958 88 50
```

**¿Qué dudas o preguntas tengo sobre lo que leí en la introducción?**

## ENUNCIADO 1 (Tienda) - Diccionario como Estructura de Datos Simple

Pablo tiene una tienda de frutas y vende tres tipos de frutas; manzanas, peras y fresas. Una manzana tiene un valor de $50, cada pera tiene un valor de $60 y cada fresa tiene un valor de $20. Pablo hace el registro de sus ventas en una base de datos llamada ventas representada por un diccionario en Python. De la misma manera, Pablo mantiene el precio de cada producto en otra base de datos llamada precios, como se muestra a continuación.

**Base de datos**
```python
ventas = {
    "manzana": 55,
    "pera": 85,
    "fresa": 130,
}

precios = {
    "manzana": 500,
    "pera": 600,
    "fresa": 200,
}
```
**Actividades**

1. ¿Liste los productos que Pablo tiene disponible en su base de datos de ventas? No es necesario usar código Python.
2. ¿Qué tipo de recorrido en diccionarios nos permitirá imprimir los nombres de los productos que Pablo tiene disponible en su base de datos? ¿Por qué?.
3. ¿Qué tipo de recorrido en diccionarios me permitiría imprimir la cantidad de unidades que Pablo ha vendido de cada producto según su base de datos?  ¿Por qué?
4. Escriba una función que reciba como parámetro el diccionario de ventas e imprima los nombres de los productos que Pablo tiene disponible en su base de datos. Incluya en el código el llamado a la función y muestre la salida.
5. Escriba una función que reciba como parámetro el diccionario de ventas e imprima el nombre del producto y la cantidad de unidades que Pablo ha vendido de cada producto. Incluya en el código el llamado a la función y muestre la salida.
6.  Escriba la función “balance” que reciba como parámetros el diccionario de ventas y el diccionario de precios e imprima el valor en pesos en ventas de cada producto. Indique la salida del código. Incluya en el código el llamado a la función y muestre la salida.


## ENUNCIADO 2 (Sucursales) - Diccionario como Estructura de Datos Compleja

Pablo ha tenido mucho éxito con su tienda y ahora tienes 3 tiendas en total, una en cada ciudad; Bogotá, Medellín y Cali. Dado que cada sucursal tiene diferentes precios para cada producto (manzana, pera y fresa), Pablo ha tenido que hacer cambios en su base de datos para poder hacer seguimiento de las ventas en cada sucursal. 

Pablo ha solicitado ayuda de un estudiante de Introducción a la Programación para que lo asista en la estructuración de la nueva base de datos usando diccionarios. Para lo anterior Pablo le ha entregado la información de los precios y ventas en cada sucursal. 

| Sucursal  | Nombre  | Precio | Ventas |
|-----------|---------|--------|--------|
| Cali      | manzana | 15     | 2      |
| Cali      | pera    | 10     | 4      |
| Cali      | fresa   | 5      | 10     |
| Bogotá    | manzana | 50     | 6      |
| Bogotá    | pera    | 60     | 2      |
| Bogotá    | fresa   | 20     | 4      |
| Medellín  | manzana | 25     | 12     |
| Medellín  | pera    | 55     | 8      |
| Medellín  | fresa   | 10     | 10     |

**Actividades**

1. Usando la tabla anterior, complete la base de datos usando diccionarios en Python.

```python
sucursales = {
    “Cali”:[ 
         { "nombre": "manzana", "precio":15, "ventas": 2 },

     ],
    “Bogota”: [



    ],
    “Medellin”: [



   ],
}
```

2. Considerando la base de datos en forma de diccionarios. Pablo requiere conocer cuál es el precio de un producto dada la base de datos de sucursales, el nombre de la sucursal y el nombre del producto.

- [ ] **(Entiendo el problema)** ¿Qué información debo entregar a Pablo? ¿Cuáles son las entradas y cuál es la salida?

* Entradas:
* Salida:

- [ ] **(Divide y Vencerás)** ¿Cuál es la lista de pasos lógicos que debo seguir para solucionar el problema?

* Paso 1 ...
* Paso 2 ...
* Paso 3 ...
* Paso N ...

- [ ] **(Código en Python)** Escriba la función `precio_producto` que le permitirá a Pablo conocer el precio de un producto para una sucursal. Realice una versión usando el recorrido de diccionarios y otra versión usando el método get. Considere los pasos lógicos que describió anteriormente, es libre de usar funciones auxiliares si considera que es necesario.


3. Considerando la base de datos en forma de diccionarios. Pablo requiere conocer cuánto fueron las ganancias en ventas para cada sucursal, data la base de datos de sucursales. Para lo anterior a Pablo le gustaría ver un diccionario con el nombre de la sucursal como llave y el valor total en ventas como valor.

- [ ] **(Entiendo el problema)** ¿Qué información debo entregar a Pablo? ¿Cuáles son las entradas y cuál es la salida?

* Entradas:
* Salida:

- [ ] **(Divide y Vencerás)** ¿Cuál es la lista de pasos lógicos que debo seguir para solucionar el problema?

* Paso 1 ...
* Paso 2 ...
* Paso 3 ...
* Paso N ...

- [ ] **(Código en Python)** Escriba la función `ganancias` que le permitirá a Pablo conocer las ganancias obtenidas por sucursal. Considere los pasos lógicos que describió anteriormente, es libre de usar funciones auxiliares si considera que es necesario.


