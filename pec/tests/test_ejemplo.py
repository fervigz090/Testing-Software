import pytest
from mochila.mochila import Mochila
from mochila.busqueda_exhaustiva import busqueda_exhaustiva


def test_ejemplo():
    mochila = Mochila(8)
    mochila.insertar_articulo(10, 6)
    mochila.insertar_articulo(2, 2)
    mochila.insertar_articulo(1, 1)
    mochila.insertar_articulo(10, 3)
    mochila.insertar_articulo(5, 4)
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 16
    assert solucion.articulos[0].seleccionado == False
    assert solucion.articulos[1].seleccionado == False
    assert solucion.articulos[2].seleccionado == True
    assert solucion.articulos[3].seleccionado == True
    assert solucion.articulos[4].seleccionado == True
