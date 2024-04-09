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
        # No seleccionar el artículo actual
        solucion_no_sel_art, valor_no_sel_art \
            = haz_busqueda_con_poda(mochila, indice_articulo + 1,
                                    valor_actual,
                                    peso_actual,
                                    valor_restante,
                                    mejor_valor_hasta_ahora)

        # Seleccionar el artículo actual si es posible
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

            # Comprobar si la selección actual es mejor que la no selección
            if valor_sel_art > valor_no_sel_art:
                return (solucion_sel_art, valor_sel_art)

        # Si no se selecciona el artículo actual o su selección no es mejor,
        # simplemente retornamos la solución y valor de no selección
        return (solucion_no_sel_art, valor_no_sel_art)
