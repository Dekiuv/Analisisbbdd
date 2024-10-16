#Numero de jugadores por equipo

import Carga
import matplotlib.pyplot as plt
import seaborn as sns

# Agrupa los jugadores por equipo y cuenta la cantidad de jugadores en cada equipo
jugadores_por_equipo = Carga.common_player_info.groupby('team_name').size()

# Convierte el resultado en un DataFrame para mayor facilidad y ordena los equipos por cantidad de jugadores
jugadores_por_equipo_df = jugadores_por_equipo.reset_index(name='cantidad').sort_values(by='cantidad', ascending=False)

# Configura el estilo de la gráfica
sns.set(style="whitegrid")

# Crea la gráfica de barras
plt.figure(figsize=(14, 8))
sns.barplot(x='team_name', y='cantidad', data=jugadores_por_equipo_df, color='orange')

# Añade etiquetas y título
plt.title('Cantidad de Jugadores por Equipo')
plt.xlabel('Equipo')
plt.ylabel('Cantidad de Jugadores')

# Ajusta las etiquetas del eje X
plt.xticks(rotation=90)

# Muestra la gráfica
plt.show()

