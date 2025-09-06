cartas = ["Pikachu", "Charmander", "Bulbasaur", "Pikachu", "Squirtle", "Pikachu"]
mi_coleccion = set(cartas)
# pikachu se repite 3 veces pero alm convertir una lista en set automáticamente
# los duplicados se eliminan
mi_coleccion.add("mewtwo") # un set no es una estructura ordenada
print(mi_coleccion)
# print(len(mi_coleccion)) = 5

# una gran ventaja es comprobar si tengo una carta casi al instante
print("Pikachu" in mi_coleccion)
print("Charizard" in mi_coleccion)
print(f"\ntengo a 'Squirtle' en mi colección: {'si' if 'Squirtle' in mi_coleccion else 'no'}")
print(f"\ntengo a 'Ditto' en mi colección: {'si' if 'Ditto' in mi_coleccion else 'no'}")

