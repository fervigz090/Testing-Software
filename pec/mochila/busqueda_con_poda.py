from copy import deepcopy

def busqueda_con_poda(mochila):
    indice_articulo = 0
    valor_actual = 0
    peso_actual = 0
    valor_restante = mochila.suma_valores(True)
    mejor_valor_hasta_ahora = [0]
    return haz_busqueda_con_poda(mochila, indice_articulo,
                                 valor_actual,
                                 peso_actual,
                                 valor_restante,
                                 mejor_valor_hasta_ahora)


def haz_busqueda_con_poda(mochila, indice_articulo,
                          valor_actual,
                          peso_actual,
                          valor_restante,
                          mejor_valor_hasta_ahora):
    if indice_articulo == len(mochila.articulos):
        valor = mochila.valor()
        if valor > mejor_valor_hasta_ahora[0]:
            mejor_valor_hasta_ahora[0] = valor
        return (deepcopy(mochila), mochila.valor())

    else:

        if valor_actual + valor_restante <= mejor_valor_hasta_ahora[0]:
            return (None, 0)

        solucion_sel_art = None
        valor_sel_art = 0
        if peso_actual + mochila.articulos[indice_articulo].peso \
                <= mochila.capacidad:
            mochila.articulos[indice_articulo].seleccionado = True
            solucion_sel_art, valor_sel_art \
                = haz_busqueda_con_poda(mochila, indice_articulo + 1,
                                        valor_actual + mochila.articulos[indice_articulo].valor,
                                        peso_actual + mochila.articulos[indice_articulo].peso,
                                        valor_restante - mochila.articulos[indice_articulo].valor,
                                        mejor_valor_hasta_ahora)

        mochila.articulos[indice_articulo].seleccionado = False
        solucion_no_sel_art, valor_no_sel_art \
            = haz_busqueda_con_poda(mochila, indice_articulo + 1,
                                    valor_actual,
                                    peso_actual,
                                    valor_restante - mochila.articulos[indice_articulo].valor,
                                    mejor_valor_hasta_ahora)

        if valor_sel_art > valor_no_sel_art:
            return (solucion_sel_art, valor_sel_art)
        else:
            return (solucion_no_sel_art, valor_no_sel_art)