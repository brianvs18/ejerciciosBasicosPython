# Operadores relacionales
variable_uno = 10
variable_dos = 10

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

# Operadores logicos
resultado = True and True and diferente
print(resultado)
# Se puede comparar si dos variables son iguales con "is" Ejemplo:
igual2 = variable_uno is variable_dos
print(igual2)