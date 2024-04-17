
import random
from busqueda_exhaustiva import busqueda_exhaustiva
from busqueda_con_poda import busqueda_con_poda
from algoritmo_voraz import algoritmo_voraz
from mochila import Mochila
import pandas as pd


mochila = Mochila(16)
mochila.insertar_articulo(8, 5)
mochila.insertar_articulo(3, 3)
mochila.insertar_articulo(2, 5)
mochila.insertar_articulo(6, 7)

solucion, valor = busqueda_exhaustiva(mochila)

data = []
numArticulos = 4
for i in range(numArticulos):
    data.append([f"{solucion.articulos[i].valor}, {solucion.articulos[i].peso}, {solucion.articulos[i].seleccionado}"])
df = pd.DataFrame(data, columns=["busqueda_exhaustiva"])
print(df)



    
