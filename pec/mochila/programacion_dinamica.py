
from mochila.mochila import Articulo, Mochila


def programacion_dinamica(mochila):
    n = len(mochila.articulos)
    capacidad = mochila.capacidad
    tabla = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla de programación dinámica
    for i in range(1, n + 1):
        for j in range(1, capacidad + 1):
            if mochila.articulos[i - 1].peso <= j:
                tabla[i][j] = max(
                    tabla[i - 1][j],
                    tabla[i - 1][j - mochila.articulos[i - 1].peso]
                    + mochila.articulos[i - 1].valor
                )
            else:
                tabla[i][j] = tabla[i - 1][j]
    
    # Reconstruir la seleccion de artículos
    seleccionados = [False] * n
    i, j = n, capacidad
    while i > 0 and j > 0:
        if tabla[i][j] != tabla[i - 1][j]:
            seleccionados[i - 1] = True
            j -= mochila.articulos[i - 1].peso
        i -= 1
    
    # Crear una nueva mochila con los artículos seleccionados
    nuevos_articulos = []
    for articulo, seleccionado in zip(mochila.articulos, seleccionados):
        nuevo_articulo = Articulo(articulo.valor, articulo.peso)
        nuevo_articulo.seleccionado = seleccionado
        nuevos_articulos.append(nuevo_articulo)
    nueva_mochila = Mochila()
    nueva_mochila.capacidad = capacidad
    nueva_mochila.articulos = nuevos_articulos
    
    return nueva_mochila, tabla[n][capacidad]
