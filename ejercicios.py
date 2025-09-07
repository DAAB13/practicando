# Ejercicio 1
""" 
def generar_mensaje (nombre, nota):
  if nota >= 11:
    return f"Felicidades {nombre}, aprobaste el curso con {nota} de nota"
  else:
    return f"Estimado(a) {nombre}, desaporbaste el curso, sigue intentando"

mensaje_diego = generar_mensaje("Diego", 13)
print(mensaje_diego)
"""


# Ejercicio 2
"""
notas_diego = [13, 13, 4]

def calcular_promedio(lista_de_notas):
  if not lista_de_notas:
    return 0
  suma_de_notas = sum(lista_de_notas)
  cantidad_de_notas = len(lista_de_notas)
  return suma_de_notas / cantidad_de_notas

promedio_diego = calcular_promedio(notas_diego) 
print(promedio_diego) 
promedio_clase_2025 = calcular_promedio(clase_2025)
"""



# Ejercicio 3

"""
def calcular_promedio(lista_de_notas):
  if not lista_de_notas:
    return 0
  suma_de_notas = sum(lista_de_notas)
  cantidad_de_notas = len(lista_de_notas)
  return suma_de_notas / cantidad_de_notas

def top_talent(lista_de_clase):
  top_alumnos = []
  for alumno in lista_de_clase:
    notas_alumnos = alumno['notas']
    promedio_alumno = calcular_promedio(notas_alumnos)
    if promedio_alumno > 15:
      nombre_de_alumno = alumno['nombre']
      top_alumnos.append(nombre_de_alumno)
  return top_alumnos


clase_2025 = [
    {'nombre': 'Elena Torres', 'notas': [18, 17, 19]},
    {'nombre': 'Marco Diaz', 'notas': [12, 14, 13]},
    {'nombre': 'Lucía Jimenez', 'notas': [16, 15, 17]},
    {'nombre': 'Javier Morales', 'notas': [10, 11, 9]},
    {'nombre': 'Diego Alvarado', 'notas': [10, 13, 18]}
]

top_estudiantes = top_talent(clase_2025)
print(top_estudiantes)
"""


# Ejercicio 4
""" 
lista_notas = [13, 8, 15, 19, 9, 20, 15, 13, 6, 15, 20, 15, 5]

def contar_categoria(lista_de_notas):
  count_nm = 0
  count_s = 0
  count_d = 0
  for nota in lista_de_notas:
    if nota >= 17:
      count_d += 1
    elif nota >= 11:
      count_s += 1
    else:
      count_nm += 1
  return {
    "Necesita mejora": count_nm,
    "Satisfactorio": count_s,
    "Destacado": count_d
  }

contando_categorias = contar_categoria(lista_notas)
print(contando_categorias)
"""

# Ejercicio 5
"""
estudiante = {
  "nombre": "Diego",
  "apellido": "Alvarado",
  "email": "diego.alvarado@upch.pe"
}

def generar_id(dict_estudiante):
  nombre_min = dict_estudiante["nombre"].lower()
  apellido_min = dict_estudiante["apellido"][0].lower()
  concat = nombre_min + apellido_min
  return concat

def validar_email(dic_estudiante):
  correo = dic_estudiante["email"]
  if correo.endswith("@upch.pe"):
    return True
  else:
    return False

if validar_email(estudiante):
  id_estudiante = generar_id(estudiante)
  print(f"ID generado = {id_estudiante}")
else:
  print("ERROR: NO ESTÁ USANDO UN CORREO CORPORATIVO")
"""


# Ejercicio 6

clase_de_historia = [
    {'nombre': 'Ana García', 'notas': [15, 18, 16, 17]},
    {'nombre': 'Carlos Rodríguez', 'notas': [12, 11, 13, 14]},
    {'nombre': 'Sofía Martínez', 'notas': [19, 20, 18, 19]},
    {'nombre': 'Luis Hernandez', 'notas': [8, 10, 9, 11]},
    {'nombre': 'Valentina Lopez', 'notas': [16, 15, 14, 15]},
    {'nombre': 'Javier Perez', 'notas': [10, 13, 12, 14]},
    {'nombre': 'Camila Gomez', 'notas': [20, 18, 17, 19]}
]

def buscar_notas_por_mombre (lista_clase, nombre_buscado):
  for alumno in lista_clase:
    if alumno['nombre'] == nombre_buscado:
      return alumno['notas']
  return f"Estudiante: {nombre_buscado} => no hay registros"

buscar_Ana = buscar_notas_por_mombre (clase_de_historia, 'Javier Perez')
print(buscar_Ana)    
