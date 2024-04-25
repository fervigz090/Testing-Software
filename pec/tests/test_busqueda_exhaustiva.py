import csv
import random
import time
import pytest
import pandas as pd
from mochila.mochila import Mochila
from mochila.busqueda_exhaustiva import busqueda_exhaustiva
from mochila.busqueda_con_poda import busqueda_con_poda
from mochila.algoritmo_voraz import algoritmo_voraz

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
    
def test_escalabilidad_exhaustiva_vs_poda():
    with open('escalabilidad_exhaustiva_vs_poda.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['algoritmo', 'numero_de_articulos', 'valor_optimo', 'segundos'])
        for numArticulos in range(5, 18):
            kp = genera_aleatorio(numArticulos)

            t0_exhaustiva = time.time()
            solucion_exhaustiva, valor_exhaustiva = busqueda_exhaustiva(kp)
            t1_exhaustiva = time.time()
            t_exhaustiva = t1_exhaustiva - t0_exhaustiva

            writer.writerow(['busqueda_exhaustiva', numArticulos, valor_exhaustiva, t_exhaustiva])

            t0_poda = time.time()
            solucion_poda, valor_poda = busqueda_con_poda(kp)
            t1_poda = time.time()
            t_poda = t1_poda - t0_poda

            writer.writerow(['busqueda_con_poda', numArticulos, valor_poda, t_poda])

def test_escalabilidad_poda_vs_voraz():
    with open('escalabilidad_poda_vs_voraz.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['algoritmo', 'numero_de_articulos', 'valor_optimo', 'segundos'])
        for numArticulos in range(5, 18):
            kp = genera_aleatorio(numArticulos)

            t0_poda = time.time()
            solucion_poda, valor_poda = busqueda_con_poda(kp)
            t1_poda = time.time()
            t_poda = t1_poda - t0_poda

            writer.writerow(['busqueda_con_poda', numArticulos, valor_poda, t_poda])

            t0_voraz = time.time()
            solucion_voraz, valor_voraz = algoritmo_voraz(kp)
            t1_voraz = time.time()
            t_voraz = t1_voraz - t0_voraz

            writer.writerow(['algoritmo_voraz', numArticulos, valor_voraz, t_voraz])

# Tests ACTS
def test_ACTS_JP1():
    # Lee el fichero csv exportado con ACTS
    df = pd.read_csv('JP1-output.csv')

    fallo_valor = False
    fallo_peso = False
    fallo_capacidad = False

    for index, row in df.iterrows():
        capacidad = row['capacidad']
        valor = row['valor']
        peso = row['peso']
        num_articulos = row['articulos']

        try:
            mochila = Mochila(capacidad)
            for i in range(num_articulos):
                mochila.insertar_articulo(valor, peso)

            solucion, valor = busqueda_exhaustiva(mochila)
        except ValueError:
            if valor < 0:
                fallo_valor = True
            if capacidad < 0:
                fallo_capacidad = True
            if peso <= 0:
                fallo_peso = True
            continue  # Continua con la siguiente iteración del bucle
                
    # Debe detectar los fallos en todas las variables
    assert fallo_valor == True
    assert fallo_peso == True
    assert fallo_capacidad == True


