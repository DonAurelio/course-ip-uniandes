# -*- coding: utf-8 -*-

"""
NIVEL 3. LECCIÓN 9. RECORRIDO DE DICIONARIOS 
Archivo: Enunciado_1.py
Autor: Aurelio Vivas
Fecha: Diciembre 13 de 2021
"""

"""
PUNTO 1.

R/
- Manzana
- Pera
- Fresa
"""

"""
PUNTO 2.

R/ Recorrido por llaves, porque los nombres de los productos hacen parte de la llave del diccionario.
"""

"""
PUNTO 3.

R/ Recorrido por valores, porque la cantidad de unidades vendidas de cada producto hace parte de los valores del diccionario.
"""

# BASE DE DATOS DE PRODUCTOS
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

"""
PUNTO 4.
"""

# Escriba la función ....
def nombres_productos(ventas: dict) -> None:
    for cada_llave in ventas:
        print(cada_llave)

# Pruebe la función aquí ...
#nombres_productos(ventas)

"""
PUNTO 5.
"""

# Escriba la función ....
def unidades_vendidas_por_producto(ventas: dict) -> None:
    for cada_llave in ventas:
        print(cada_llave,"=>",ventas[cada_llave])

# Pruebe la función aquí ...
#unidades_vendidas_por_producto(ventas)

"""
PUNTO 6.
"""

# Escriba la función ....
def balance(ventas: dict, precios: dict) -> None:
    for cada_llave in ventas:
        print(cada_llave,"=>", ventas[cada_llave] * ventas[cada_llave])

# Pruebe la función aquí ...
#balance(ventas, precios)

#________________________________________ INTERFAZ ___________________________________________________

def mostrar_menu() -> str:
    print("Seleccionar una opción")
    print("1. Productos disponibles")
    print("2. Unidades vendidas por producto")
    print("3. Balance de ventas")
    print("4. Salir")
    opcion = input("Opción seleccionada =>")
    return opcion

def iniciar_aplicacion() -> None:
    print("BIENVENIDO AL SISTEMA DE VENTAS DE PABLO")
    continuar = True
    while continuar:
        opcion = mostrar_menu()
        if opcion == "1":
            nombres_productos(ventas)
        elif opcion == "2":
            unidades_vendidas_por_producto(ventas)
        elif opcion == "3":
            balance(ventas,precios)
        elif opcion == "4":
            continuar = False
        else:
            print("La opción seleccionada no es valida")

iniciar_aplicacion()