import csv
import time
from pec.mochila.algoritmo_voraz import algoritmo_voraz
from pec.mochila.busqueda_con_poda import busqueda_con_poda
from pec.tests.test_algoritmos_alternativos import genera_aleatorio
import pytest
from mochila.mochila import Articulo, Mochila
from mochila.programacion_dinamica import programacion_dinamica

def test_programacion_dinamica():
    # Definir una mochila de prueba
    capacidad = 10
    mochila = Mochila(capacidad)
    mochila.insertar_articulo(10, 5)
    mochila.insertar_articulo(40, 4)
    mochila.insertar_articulo(30, 6)
    mochila.insertar_articulo(50, 3)
    
    # Calcular la solución utilizando programación dinámica
    mochila_resuelta, valor_optimo = programacion_dinamica(mochila)
    
    # Verificar que la mochila resuelta tenga la misma capacidad
    assert mochila_resuelta.capacidad == capacidad
    
    # Verificar que la suma de los pesos de los artículos seleccionados no excede la capacidad
    suma_pesos = sum(articulo.peso for articulo in mochila_resuelta.articulos if articulo.seleccionado)
    assert suma_pesos <= capacidad
    
    # Verificar que el valor de la solución obtenida sea correcto
    valor_esperado = 90  # El valor óptimo esperado para esta instancia particular
    assert valor_optimo == valor_esperado

# Test de escalabilidad
def test_escalabilidad_dinamica_vs_voraz():
    with open('escalabilidad_dinamica_vs_voraz.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['algoritmo', 'numero_de_articulos', 'valor_optimo', 'segundos'])
        for numArticulos in range(5, 18):
            kp = genera_aleatorio(numArticulos)

            t0_dinamica = time.time()
            solucion_dinamica, valor_dinamica = programacion_dinamica(kp)
            t1_dinamica = time.time()
            t_poda = t1_dinamica - t0_dinamica

            writer.writerow(['busqueda_con_poda', numArticulos, valor_dinamica, t_poda])

            t0_voraz = time.time()
            solucion_voraz, valor_voraz = algoritmo_voraz(kp)
            t1_voraz = time.time()
            t_voraz = t1_voraz - t0_voraz

            writer.writerow(['algoritmo_voraz', numArticulos, valor_voraz, t_voraz])

def test_escalabilidad_dinamica_vs_poda():
    with open('escalabilidad_dinamica_vs_poda.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['algoritmo', 'numero_de_articulos', 'valor_optimo', 'segundos'])
        for numArticulos in range(5, 18):
            kp = genera_aleatorio(numArticulos)

            t0_dinamica = time.time()
            solucion_dinamica, valor_dinamica = programacion_dinamica(kp)
            t1_dinamica = time.time()
            t_dinamica = t1_dinamica - t0_dinamica

            writer.writerow(['busqueda_dinamica', numArticulos, valor_dinamica, t_dinamica])

            t0_poda = time.time()
            solucion_poda, valor_poda = busqueda_con_poda(kp)
            t1_poda = time.time()
            t_poda = t1_poda - t0_poda

            writer.writerow(['busqueda_con_poda', numArticulos, valor_poda, t_poda])
