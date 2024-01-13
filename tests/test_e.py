import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'Año': [2010, 2011, 2012, 2013, 2014],
        'Ventas': [500, 600, 800, 750, 900]}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame Original:")
print(df)

# Crear un gráfico de barras
plt.bar(df['Año'], df['Ventas'])

# Agregar etiquetas y título
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Ventas por Año')

# Mostrar el gráfico
plt.show()# Guardar el gráfico en un archivo PDF
plt.savefig('grafico_ventas.png')