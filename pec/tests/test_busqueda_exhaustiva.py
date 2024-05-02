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

def genera_valores(id):
    if id == "C1":
        return random.randint(1,20)
    if id == "C2":
        return -2
    if id == "C3" or id == "N3" or id == "P2" or id == "V3":
        return 0
    if id == "N1":
        return random.randint(1,5)
    if id == "N2":
        return -1
    if id == "P1" or id == "V1":
        return random.randint(1,10)
    if id == "P3":
        return -2
    if id == "V2":
        return -3
    else:
        return "Error ID valor"
    

# Tests ACTS
def test_ACTS_JP1():
    # Lee el fichero csv exportado con ACTS
    df = pd.read_csv('JP1-output.csv')

    fallo_valor = False
    fallo_peso = False
    fallo_capacidad = False

    for index, row in df.iterrows():
        id_capacidad = row['C']
        id_num_articulos = row['N']
        id_peso = row['P']
        id_valor = row['V']

        try:
            capacidad = genera_valores(id_capacidad)
            num_articulos = genera_valores(id_num_articulos)
            mochila = Mochila(capacidad)
            for i in range(num_articulos):
                valor = genera_valores(id_valor)
                peso = genera_valores(id_peso)
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


def test_ACTS_JP2():
    # Lee el fichero csv exportado con ACTS
    df = pd.read_csv('JP2-output.csv')

    for index, row in df.iterrows():
        id_capacidad = row['C']
        id_num_articulos = row['N']
        id_peso = row['P']
        id_valor = row['V']
    
        try:
            capacidad = genera_valores(id_capacidad)
            num_articulos = genera_valores(id_num_articulos)
            mochila = Mochila(capacidad)
            for i in range(num_articulos):
                valor = genera_valores(id_valor)
                peso = genera_valores(id_peso)
                mochila.insertar_articulo(valor, peso)

            solucion, valor = busqueda_exhaustiva(mochila)
        except ValueError:
            # Si detecta un error, la prueba falla
            assert False
        assert True

# Tests de escalabilidad
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


            

