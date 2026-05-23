# CASO 9 - TRIPLE BUCLE
# COMPLEJIDAD: O(n³)
n = int(input("Ingrese el tamaño: "))

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(f"({i},{j},{k})")
