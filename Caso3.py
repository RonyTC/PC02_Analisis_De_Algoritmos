# CASO 3 - BÚSQUEDA LINEAL
# COMPLEJIDAD: O(n)
lista = []

n = int(input("Cantidad de elementos: "))

for i in range(n):
    valor = int(input(f"Ingrese elemento {i+1}: "))
    lista.append(valor)
    encontrado = False

buscar = int(input("Número a buscar: "))
for elemento in lista:
    if elemento == buscar:
        encontrado = True
        break

if encontrado:
    print("Elemento encontrado")
else:
     print("Elemento no encontrado")