mi_lista = []
#print(mi_lista)

my_list = [2, 5, 6, 12]
#print(len(mi_lista))

mi_lista = ["hola", 3, "azul"]

#print(mi_lista + my_list)  =  ['hola', 3, 'azul', 2, 5, 6, 12]

mi_lista.insert(1,"blue")
mi_lista.append(4) # al final
mi_lista.remove("hola")
mi_lista.pop() # elimina por posición 
print(mi_lista)

#my_pop_element = mi_lista.pop(1) # extrae el elemento según la posición
#print(my_pop_element) # se asigna a una variable y se imprime

my_new_list = mi_lista.copy()
print(my_new_list)
my_new_list.reverse()
print(my_new_list)


otra_lista = [24, 145, 13.5, 45, 2]
otra_lista.sort()
print(otra_lista)