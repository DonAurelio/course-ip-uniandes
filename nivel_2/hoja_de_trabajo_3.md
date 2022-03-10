# PROBLEMA 1. Uso de diccionarios en problemas reales.

Defina una función llamada crear_estudiante. La función debe recibir como parámetro el nombre del estudiante, y las notas de cada materia: matemáticas, biología, sociales, física, y filosofía. La función debe retornar un diccionario donde se encuentre almacenado el nombre del estudiante y las notas en cada materia. Use la función para crear 3 estudiantes. Imprima en pantalla la información de cada estudiante. 

Defina la función buscar_estudiante, la cual le permitirá buscar un estudiante por nombre. Esta función debe recibir 3 diccionarios (estudiantes), un nombre y debe retornar el diccionario del estudiante que corresponde con el nombre entregado como parámetro. Si ninguno de los estudiantes tiene el nombre integrado como parámetro entonces se debe retornar None.

Define la función mejor_estudiante, la cual le permitirá conocer el estudiante con mejor promedio. Esta función debe recibir 3 diccionarios (estudiantes) y debe retornar el diccionario del estudiante que presenta mayor promedio de notas en todas las materias.

## Solución

```python
def crear_estudiante(nombre: str, mate: float, bio: float, soc: float, fisi: float, filo: float) -> dict:
    """
    Crea un estudiante representado en un diccionario.

    Parámetros
    ----------
    nombre : str
        Nombre del estudiante.
    mate : float
        Promedio del estudiante en matemáticas.
    bio : float
        Promedio del estudiante en biología.
    soc : float
        Promedio del estudiante en sociales.
    fisi : float
        Promedio del estudiante en física.
    filo : float
        Promedio del estudiante en folosofía.

    Retorno
    -------
    dict
        Un estudiante representado en un diccionario.

    """
    estudiante = {
       "nombre": nombre,
       "matematicas": mate,
       "biologia": bio,
       "sociales": soc,
       "fisica": fisi,
       "filosofia": filo
       
    }
    
    return estudiante

estudiante_1 = crear_estudiante('Carolina Ramirez', 5.0, 3.6, 4.7, 3.9, 5.0)
estudiante_2 = crear_estudiante('Marcelo Gonzales', 3.5, 5.0, 4.0, 2.5, 3.0)
estudiante_3 = crear_estudiante('Vladimir Zuleta', 3.0, 4.8, 2.7, 3.5, 4.0)

print('prueba: crear_estudiante')
print(estudiante_1)
print(estudiante_2)
print(estudiante_3)


def buscar_estudiante(nombre: str, est1: dict, est2: dict, est3: dict) -> dict:
    """
    Permite buscar un estudiante dado un nombre.

    Parámetros
    ----------
    nombre : str
        Nombre del estudiante a buscar.
    est1 : dict
        Diccionario que representa al estudiante 1.
    est2 : dict
        Diccionario que representa al estudiante 2.
    est3 : dict
        Diccionario que representa al estudiante 3.

    Retorno
    -------
    dict
        Retorna el estudiante que cuyo nombre es igual al nombre del estudiante buscado,
        si el estudiante con el nombre pasado como parámetro no es encontrado retorna None.

    """
    estudiante = None
    
    if nombre == est1['nombre']:
        estudiante = est1
    elif nombre == est2['nombre']:
        estudiante = est2
    elif nombre == est3['nombre']:
        estudiante = est3
    else:
        estudiante = None
        
    return estudiante

print('prueba: buscar_estudiante')
print(buscar_estudiante('Carolina Ramirez',estudiante_1,estudiante_2,estudiante_3))
print(buscar_estudiante('Sebastian Santos',estudiante_1,estudiante_2,estudiante_3))


def mejor_estudiante(est1: dict, est2: dict, est3: dict) -> dict:
    """
    Permite determinar qué estudiante tiene el mejor promedio acomulado.

    Parámetros
    ----------
    est1 : dict
        Diccionario que representa al estudiante 1.
    est2 : dict
        Diccionario que representa al estudiante 1.
    est3 : dict
        Diccionario que representa al estudiante 1.

    Retorno
    -------
    dict
        Retorna el estudiante cuyo promedio acumulado es el más alto.

    """
    promedio_est1 = ( est1["matematicas"] + est1["biologia"] + est1["sociales"] + est1["fisica"] + est1["filosofia"] ) / 5
    promedio_est2 = ( est2["matematicas"] + est2["biologia"] + est2["sociales"] + est2["fisica"] + est2["filosofia"] ) / 5
    promedio_est3 = ( est3["matematicas"] + est3["biologia"] + est3["sociales"] + est3["fisica"] + est3["filosofia"] ) / 5
    
    estudiante = None
    
    if promedio_est1 >= promedio_est2 and promedio_est1 >= promedio_est3:
        estudiante = est1
    elif promedio_est2 >= promedio_est1 and promedio_est2 >= promedio_est3:
        estudiante = est2
    else:
        estudiante = est3

    return estudiante        
        
print('prueba: mejor_estudiante')
print(mejor_estudiante(estudiante_1,estudiante_2,estudiante_3))

```