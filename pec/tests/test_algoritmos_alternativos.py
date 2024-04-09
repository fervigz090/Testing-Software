import random
from mochila.busqueda_exhaustiva import busqueda_exhaustiva
from mochila.busqueda_con_poda import busqueda_con_poda
from mochila.algoritmo_voraz import algoritmo_voraz
from mochila.mochila import Mochila
import pytest

def genera_aleatorio(numArticulos):
    capacidad = 0
    mochila = Mochila()
    for _ in range(numArticulos):
        valor = random.randint(0, 10)
        peso = random.randint(1, 10)
        capacidad = capacidad + peso
        mochila.insertar_articulo(valor, peso)

    mochila.capacidad = capacidad//2
    return mochila

def test_busqueda_con_poda():
    kp = None
    numArticulos = 0
    for _ in range(100):
        numArticulos = random.randint(5, 10)
        kp = genera_aleatorio(numArticulos)
        s1, v1 = busqueda_exhaustiva(kp)
        s2, v2 = busqueda_con_poda(kp)
        assert v1 == v2
        for i in range(numArticulos):
            assert s1.articulos[i].seleccionado == s2.articulos[i].seleccionado

def test_algotitmo_voraz():
    kp = None
    numArticulos = 0
    for _ in range(100):
        numArticulos = random.randint(5, 10)
        kp = genera_aleatorio(numArticulos)
        s1, v1 = busqueda_exhaustiva(kp)
        s2, v2 = algoritmo_voraz(kp)
        assert v1 == v2
        for i in range(numArticulos):
            assert s1.articulos[i].seleccionado == s2.articulos[i].seleccionado
            
