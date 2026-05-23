# CASO 10 - COMPARACIÓN DE DOS LISTAS
# COMPLEJIDAD: O(n²)
lista1 = []
lista2 = []

n1 = int(input("Cantidad de elementos lista 1: "))

for i in range(n1):
    valor = int(input(f"Ingrese elemento {i+1}: "))
    lista1.append(valor)

n2 = int(input("Cantidad de elementos lista 2: "))

for i in range(n2):
    valor = int(input(f"Ingrese elemento {i+1}: "))
    lista2.append(valor)

print("Elementos repetidos:")

for i in lista1:
    for j in lista2:
        if i == j:
            print(i)