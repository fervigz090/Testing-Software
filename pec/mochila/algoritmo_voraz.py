from copy import deepcopy

def algoritmo_voraz(mochila):
    solucion = deepcopy(mochila)
    peso_disponible = solucion.capacidad
    valor = 0
    while peso_disponible > 0:
        i = solucion.articulo_de_max_valor(peso_disponible)
        if i == -1:
            break
        solucion.articulos[i].seleccionado = True
        valor += solucion.articulos[i].valor
        peso_disponible -= solucion.articulos[i].peso
    return solucion, valor


