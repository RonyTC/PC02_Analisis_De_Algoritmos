# CASO 2 - BUCLE DOBLE
# COMPLEJIDAD: O(n²)
n = int(input("Ingrese el tamaño: "))

for i in range(n):
    for j in range(n):
        print(f"({i},{j})")
