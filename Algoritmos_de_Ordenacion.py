# ==========================================
# ALGORITMOS DE ORDENACIÓN EN PYTHON
# Burbuja, Inserción, Selección,
# Quicksort y Mergesort
# ==========================================

# Conjunto de datos
datos_originales = [45, 12, 78, 3, 56, 89, 23, 1, 67, 34]


# ------------------------------------------
# MÉTODO BURBUJA
# ------------------------------------------
def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# ------------------------------------------
# MÉTODO INSERCIÓN
# ------------------------------------------
def insercion(lista):

    for i in range(1, len(lista)):

        clave = lista[i]
        j = i - 1

        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave

    return lista


# ------------------------------------------
# MÉTODO SELECCIÓN
# ------------------------------------------
def seleccion(lista):

    n = len(lista)

    for i in range(n):

        minimo = i

        for j in range(i + 1, n):

            if lista[j] < lista[minimo]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

    return lista


# ------------------------------------------
# MÉTODO QUICKSORT
# ------------------------------------------
def quicksort(lista):

    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


# ------------------------------------------
# MÉTODO MERGESORT
# ------------------------------------------
def mergesort(lista):

    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2

    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return fusionar(izquierda, derecha)


def fusionar(izquierda, derecha):

    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# ------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------
def mostrar_menu():

    while True:

        print("\n===================================")
        print("   MENÚ DE ALGORITMOS DE ORDENACIÓN")
        print("===================================")

        print("1. Ordenamiento Burbuja")
        print("2. Ordenamiento Inserción")
        print("3. Ordenamiento Selección")
        print("4. Ordenamiento Quicksort")
        print("5. Ordenamiento Mergesort")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        # Copia de la lista original
        datos = datos_originales.copy()

        if opcion == "1":
            print("\nMétodo Burbuja")
            print("Lista original:", datos)
            print("Lista ordenada:", burbuja(datos))

        elif opcion == "2":
            print("\nMétodo Inserción")
            print("Lista original:", datos)
            print("Lista ordenada:", insercion(datos))

        elif opcion == "3":
            print("\nMétodo Selección")
            print("Lista original:", datos)
            print("Lista ordenada:", seleccion(datos))

        elif opcion == "4":
            print("\nMétodo Quicksort")
            print("Lista original:", datos)
            print("Lista ordenada:", quicksort(datos))

        elif opcion == "5":
            print("\nMétodo Mergesort")
            print("Lista original:", datos)
            print("Lista ordenada:", mergesort(datos))

        elif opcion == "6":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


# ------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------
mostrar_menu()