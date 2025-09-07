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

