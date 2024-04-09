
import random
from busqueda_exhaustiva import busqueda_exhaustiva
from busqueda_con_poda import busqueda_con_poda
from algoritmo_voraz import algoritmo_voraz
from mochila import Mochila

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
        print("numero de articulos", numArticulos)
        kp = genera_aleatorio(numArticulos)
        s1, v1 = busqueda_exhaustiva(kp)
        s2, v2 = busqueda_con_poda(kp)
        print(v1 == v2)
        print("-------------------- Mochila KP --------------------")
        kp.imprimir()
        print(kp.articulos[1].valor)
        print("-------------------- Mochila Busqueda Exhaustiva --------------------")
        s1.imprimir()
        print("--------------------- Mochila Busqueda con Poda ---------------------")
        s2.imprimir()
        for i in range(numArticulos):
            print(s1.articulos[i].seleccionado == s2.articulos[i].seleccionado)

test_busqueda_con_poda()




    
