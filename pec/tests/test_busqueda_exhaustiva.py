import pytest
from mochila.mochila import Mochila
from mochila.busqueda_exhaustiva import busqueda_exhaustiva

def test_M1():
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

def test_M2():
    mochila = Mochila(8)
    mochila.insertar_articulo(1, 1)
    mochila.insertar_articulo(2, 2)
    mochila.insertar_articulo(5, 4)
    mochila.insertar_articulo(10, 3)
    mochila.insertar_articulo(10, 6)
    
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 16
    assert solucion.articulos[0].seleccionado == True
    assert solucion.articulos[1].seleccionado == False
    assert solucion.articulos[2].seleccionado == True
    assert solucion.articulos[3].seleccionado == True
    assert solucion.articulos[4].seleccionado == False

def test_M2():
    mochila = Mochila(20)
    mochila.insertar_articulo(1, 1)
    mochila.insertar_articulo(2, 2)
    mochila.insertar_articulo(5, 4)
    mochila.insertar_articulo(10, 3)
    mochila.insertar_articulo(10, 6)
    
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 28
    assert solucion.articulos[0].seleccionado == True
    assert solucion.articulos[1].seleccionado == True
    assert solucion.articulos[2].seleccionado == True
    assert solucion.articulos[3].seleccionado == True
    assert solucion.articulos[4].seleccionado == True

def test_M4():
    mochila = Mochila(8)
    
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 0
    

def test_M5():
    mochila = Mochila(0)
    mochila.insertar_articulo(10, 6)
    mochila.insertar_articulo(2, 2)
    mochila.insertar_articulo(1, 1)
    mochila.insertar_articulo(10, 3)
    mochila.insertar_articulo(5, 4)
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 0
    assert solucion.articulos[0].seleccionado == False
    assert solucion.articulos[1].seleccionado == False
    assert solucion.articulos[2].seleccionado == False
    assert solucion.articulos[3].seleccionado == False
    assert solucion.articulos[4].seleccionado == False

def test_M6():
    mochila = None
    with pytest.raises(ValueError):
        mochila = Mochila(-1)

def test_M7():
    mochila = Mochila()
    mochila.insertar_articulo(10, 6)
    mochila.insertar_articulo(2, 2)
    mochila.insertar_articulo(1, 1)
    mochila.insertar_articulo(10, 3)
    mochila.insertar_articulo(5, 4)
    solucion, valor = busqueda_exhaustiva(mochila)
    assert valor == 0
    assert solucion.articulos[0].seleccionado == False
    assert solucion.articulos[1].seleccionado == False
    assert solucion.articulos[2].seleccionado == False
    assert solucion.articulos[3].seleccionado == False
    assert solucion.articulos[4].seleccionado == False

def test_M8():
    mochila = Mochila(8)
    with pytest.raises(ValueError):
        mochila.insertar_articulo(-1, 6)
    
def test_M9():
    mochila = Mochila(8)
    with pytest.raises(ValueError):
        mochila.insertar_articulo(10, -3)

def test_M10():
    mochila = Mochila(8)
    with pytest.raises(ValueError):
        mochila.insertar_articulo(10, 0)
    

