import pandas as pd
from sqlalchemy import create_engine

# Ruta de cada CSV y el nombre de la tabla que cargara
csv_files = {
    'common_player_info': './csv/common_player_info.csv',
    'draft_combine_stats': './csv/draft_combine_stats.csv',
    'draft_history': './csv/draft_history.csv',
    'game_info': './csv/game_info.csv',
    'game_summary': './csv/game_summary.csv',
    'game': './csv/game.csv',
    'inactive_players': './csv/inactive_players.csv',
    'line_score': './csv/line_score.csv',
    'officials': './csv/officials.csv',
    'other_stats': './csv/other_stats.csv',
    'play_by_play':'./csv/play_by_play.csv',
    'player': './csv/player.csv',
    'team_details': './csv/team_details.csv',
    'team_history': './csv/team_history.csv',
    'team_info_common': './csv/team_info_common.csv',
    'team': './csv/team.csv'
}

# Crear una conexión a la base de datos SQLite
engine = create_engine('sqlite:///BBDD_Grupo1.db')

# Cargar los primeros 100 registros de cada archivo CSV
for nombre_tabla, ruta in csv_files.items():
    print("####################################################")
    print(f"Leyendo el archivo {ruta}...")
    data = pd.read_csv(ruta)
    
    # Filtrar los primeros 100 registros
    data_subset = data.head(100)
    
    # Crear la tabla e insertar los datos en SQLite
    data_subset.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)
    
    print(f"Los primeros 100 registros de {nombre_tabla} han sido cargados en la BBDD de Grupo1.")

print("#####################################")
print("El archivo BBDD_Grupo1 ha sido creado")
print("#####################################")