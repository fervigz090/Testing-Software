from copy import deepcopy

def busqueda_exhaustiva(mochila):
    return haz_busqueda_exhaustiva(mochila, 0)

def haz_busqueda_exhaustiva(mochila, indice_articulo):
    if indice_articulo == len(mochila.articulos):
        return (deepcopy(mochila), mochila.valor())
    else:
        mochila.articulos[indice_articulo].seleccionado = True
        solucion_sel_art, valor_sel_art \
            = haz_busqueda_exhaustiva(mochila, indice_articulo + 1)
        mochila.articulos[indice_articulo].seleccionado = False
        solucion_no_sel_art, valor_no_sel_art \
            = haz_busqueda_exhaustiva(mochila, indice_articulo + 1)
        if valor_sel_art > valor_no_sel_art:
            return (solucion_sel_art, valor_sel_art)
        else:
            return (solucion_no_sel_art, valor_no_sel_art)