# CASO 1 - BUCLE SIMPLE
# COMPLEJIDAD: O(n)
n = int(input("Ingrese el tamaño: "))

for i in range(n):
    for j in range(n):
        print(f"({i},{j})")
