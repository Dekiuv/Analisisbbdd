#Numero equipos por estado

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
team = pd.read_csv('./csv/team.csv')

# Agrupa los equipos por estado y cuenta la cantidad de equipos en cada estado
equipos_por_estado = team.groupby('state').size()

# Convierte el resultado en un DataFrame para mayor facilidad y ordena por cantidad en orden descendente
equipos_por_estado_df = equipos_por_estado.reset_index(name='cantidad').sort_values(by='cantidad', ascending=False)

# Configura el estilo de la gráfica
sns.set(style="whitegrid")

# Crea la gráfica de barras
plt.figure(figsize=(12, 8))
sns.barplot(x='state', y='cantidad', data=equipos_por_estado_df, color='skyblue')

# Añade etiquetas y título
plt.title('Cantidad de Equipos por Estado')
plt.xlabel('Estado')
plt.ylabel('Cantidad de Equipos')

# Muestra la gráfica
plt.xticks(rotation=90)  # Rota las etiquetas del eje x para que se vean mejor si hay muchos estados
plt.show()