# -*- coding: utf-8 -*-

"""
NIVEL 3. LECCIÓN 9. RECORRIDO DE DICIONARIOS
Archivo: Enunciado_2.py
Autor: Aurelio Vivas
Fecha: Diciembre 13 de 2021
"""

"""
PUNTO 1.
"""

# NUEVA BASE DE DATOS DE PRODUCTOS
sucursales = {
    "Cali":[ 
         { "nombre": "manzana", "precio":15, "ventas": 2 },
         { "nombre": "pera", "precio":10, "ventas": 4 },
         { "nombre": "fresa", "precio":5, "ventas": 10 },
     ],
    "Bogota": [
         { "nombre": "manzana", "precio":50, "ventas": 6 },
         { "nombre": "pera", "precio":60, "ventas": 2 },
         { "nombre": "fresa", "precio":20, "ventas": 4 },
    ],
    "Medellin": [
         { "nombre": "manzana", "precio":25, "ventas": 12 },
         { "nombre": "pera", "precio":55, "ventas": 8 },
         { "nombre": "fresa", "precio":10, "ventas": 10 },
   ],
}


"""
PUNTO 2.

(Entiendo el problema) 
Entradas: El diccionario de sucursales, el nombre del producto y el nombre de la sucursal.
Salida: El precio del producto.

(Divide y Vencerás) 
- Paso 1 Debo encontrar el nombre de la sucursal en las llaves del diccionario de sucursales.
- Paso 2 Debo obtener la lista de productos de la sucursal.
- Paso 3 Debo buscar el producto que coincide con el nombre del producto (diccionario) ingresado por el usuario
- Paso 4 Una vez encuentre el producto obtengo el precio.

(Código en Python)
"""

# Escriba la función ....
def precio_producto(sucursales: dict, nombre_sucursal: str, nombre_producto: str) -> int:
   
    precio = 0
    # 1. Debo encontrar el nombre de la sucursal 
    for cada_sucursal in sucursales:    
        if cada_sucursal == nombre_sucursal:
            # 2 Debo obtener la lista de productos de la sucursal
            productos_sucursal = sucursales[cada_sucursal]
            # 3. Debo buscar el producto que coincide con el nombre del producto entregado por el usuario.
            for cada_producto in productos_sucursal:
                # 4. Una vez 
                if cada_producto["nombre"] == nombre_producto:
                    precio = cada_producto["precio"]
                
    return precio

# Pruebe la función aquí ...
#print('precio_producto V1',precio_producto(sucursales,'Bogota','manzana'))

# Escriba la función ....
def precio_producto_v2(sucursales: dict, nombre_sucursal: str, nombre_producto: str) -> int:
   
    precio = 0
    # 1. Debo encontrar el nombre de la sucursal
    # 2 Debo obtener la lista de productos de la sucursal
    productos_sucursal = sucursales.get(nombre_sucursal,[])
    if productos_sucursal:   
        # 3. Debo buscar el producto que coincide con el nombre del producto entregado por el usuario.
        for cada_producto in productos_sucursal:
            # 4. Una vez encuentro el producto obtener su precio
            if cada_producto["nombre"] == nombre_producto:
                precio = cada_producto["precio"]
                
    return precio

# Pruebe la función aquí ...
#print('precio_producto V2',precio_producto_v2(sucursales,'Bogota','manzana'))


"""
PUNTO 3.

(Entiendo el problema) 
Entradas: Diccionario de sucursales.
Salida:  Diccionario donde las llaves son los nombres de las sucursales y los valores la cantidad de dinero en ventas por sucursal.

(Divide y Vencerás) 
- Paso 1 Obtener el valor en ventas de una sucursal.
- Paso 2 Replicar este cálculo para todas las sucursales

(Código en Python)
"""

# Escriba la función ....
def ventas_sucursal(productos_sucursal: list) -> int:
    acumulador = 0
    for producto in productos_sucursal:
        acumulador += producto["precio"] * producto["ventas"]

    return acumulador


def ganancias(sucursales: dict) -> dict:
    ganancias_por_sucursal = {}
    for nombre_sucursal in sucursales:
        productos_sucursal = sucursales[nombre_sucursal]
        ganancias_por_sucursal[nombre_sucursal] = ventas_sucursal(productos_sucursal)        

    return ganancias_por_sucursal  

# Pruebe la función aquí ...
#print('ganancias',ganancias(sucursales))

#________________________________________ INTERFAZ ___________________________________________________

def mostrar_menu() -> str:
    print("Seleccionar una opción")
    print("1. Precio de un producto")
    print("2. Ganancias por sucursal")
    print("3. Salir")
    opcion = input("Opción seleccionada =>")
    return opcion

def solicitar_nombre_sucursal() -> str:
    nombre_sucursal = input("Ingrese nombre de la sucursal #>")
    return nombre_sucursal

def solicitar_nombre_producto() -> str:
    nombre_producto = input("Ingrese nombre del producto #>")
    return nombre_producto

def iniciar_aplicacion() -> None:
    print("BIENVENIDO AL SISTEMA DE VENTAS DE PABLO")
    continuar = True
    while continuar:
        opcion = mostrar_menu()
        if opcion == "1":
            nombre_sucursal = solicitar_nombre_sucursal()
            nombre_producto = solicitar_nombre_producto()
            precio = precio_producto(
                sucursales,
                nombre_sucursal, 
                nombre_producto
            )

            # Validar si se encontro el precio del producto
            if precio == 0:
                print("Sucursal o producto no encontrado")
            else:
                print("El precio del producto es:", precio)

        elif opcion == "2":
            ganancias_por_sucursal = ganancias(sucursales)
            print("Gancias por sucursal:", ganancias_por_sucursal)
        elif opcion == "3":
            continuar = False
        else:
            print("La opción seleccionada no es valida")

iniciar_aplicacion()
