# CASO 6 - BÚSQUEDA BINARIA
# COMPLEJIDAD: O(log n)
lista = []

n = int(input("Cantidad de elementos ordenados: "))

for i in range(n):
    valor = int(input(f"Ingrese elemento {i+1}: "))
    lista.append(valor)

x = int(input("Número a buscar: "))

inicio = 0
fin = len(lista) - 1

encontrado = False

while inicio <= fin:

    medio = (inicio + fin) // 2

    if lista[medio] == x:
        encontrado = True
        break

    elif lista[medio] < x:
        inicio = medio + 1

    else:
        fin = medio - 1

if encontrado:
    print("Elemento encontrado")
else:
    print("Elemento no encontrado")