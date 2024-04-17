import pandas as pd
import matplotlib.pyplot as plt

# Lee los datos del archivo CSV en un DataFrame
df_exhaustiva_poda = pd.read_csv('escalabilidad_exhaustiva_vs_poda.csv')
df_poda_voraz = pd.read_csv('escalabilidad_poda_vs_voraz.csv')

# Filtra los datos por algoritmo
busqueda_exhaustiva = df_exhaustiva_poda[df_exhaustiva_poda['algoritmo'] == 'busqueda_exhaustiva']
busqueda_con_poda_1 = df_exhaustiva_poda[df_exhaustiva_poda['algoritmo'] == 'busqueda_con_poda']

busqueda_con_poda_2 = df_poda_voraz[df_poda_voraz['algoritmo'] == 'busqueda_con_poda']
algoritmo_voraz = df_poda_voraz[df_poda_voraz['algoritmo'] == 'algoritmo_voraz']


# Crea el gráfico
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.title('Búsqueda exhaustiva vs. Búsqueda con poda')
# Trazar la línea para búsqueda exhaustiva
plt.plot(busqueda_exhaustiva['numero_de_articulos'], busqueda_exhaustiva['segundos'], label='Búsqueda Exhaustiva', marker='.')
# Trazar la línea para búsqueda con poda
plt.plot(busqueda_con_poda_1['numero_de_articulos'], busqueda_con_poda_1['segundos'], label='Búsqueda con Poda', marker='.')
# Personaliza el gráfico
plt.xlabel('Número de Artículos')
plt.ylabel('Tiempo (segundos)')
plt.legend()

plt.subplot(2, 1, 2)
plt.title('Búsqueda con poda vs. Algoritmo voraz')
# Trazar la línea para búsqueda con poda
plt.plot(busqueda_con_poda_2['numero_de_articulos'], busqueda_con_poda_2['segundos'], label='Búsqueda con poda', marker='.')
# Trazar la línea para algoritmo voraz
plt.plot(algoritmo_voraz['numero_de_articulos'], algoritmo_voraz['segundos'], label='Algoritmo voraz', marker='.')
# Personaliza el gráfico
plt.xlabel('Número de Artículos')
plt.ylim(0, 0.05)
plt.ylabel('Tiempo (segundos)')
plt.legend()

# Muestra el gráfico
plt.tight_layout()
plt.show()

