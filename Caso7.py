# CASO 7 - BUCLE TRIANGULAR
# COMPLEJIDAD: O(n²)
n = int(input("Ingrese el tamaño: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
