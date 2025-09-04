my_string = "este es mi string"
my_other_string = "mi otro string"
line_string = "este string\ntendrá un salto de linea"

#print(my_string + " " + my_other_string)
#print(line_string)

name, surname, age = "Diego", "Alvarado", 33
print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))

word = "python"
print(word.capitalize()) # "Python" siempre con la primera en mayúscula
print(word.upper()) # "PYTHON" todo en mayúscula
print(word.count("h"))