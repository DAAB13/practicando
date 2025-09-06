### Diccionarios ###

my_dict = dict()
# print(type(my_dict)) = class 'dict'

contacto = {
  "Nombre":"Diego",
  "Apellido":"Alvarado",
  "Edad":33,
  "leguajes":{"Python", "Swift", "Javascript"},
  1:1.70
}

contacto["Nombre"] = "Diego Alberto" # cambiar
contacto["Apellido"] = "Alvarado Benel" # cambiar
contacto["ciudad"] = "Lima" # agregar

print(contacto)
print(len(contacto))

print(contacto.items())
print(contacto.keys())
print(contacto.values())