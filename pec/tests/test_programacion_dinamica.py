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

# Ejecutar el test
test_programacion_dinamica()
