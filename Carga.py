#cargar todos los archivos y pequeño analisis de cada base de datos
#buscar relaciones entre bases (min 5 tablas) (si hay muchso registros 100 registros)

import pandas as pd

common_player_info = pd.read_csv('./csv/common_player_info.csv')
draft_combine_stats = pd.read_csv('./csv/draft_combine_stats.csv')
draft_history = pd.read_csv('./csv/draft_history.csv')
game_info = pd.read_csv('./csv/game_info.csv')
game_summary = pd.read_csv('./csv/game_summary.csv')
game = pd.read_csv('./csv/game.csv')
inactive_players = pd.read_csv('./csv/inactive_players.csv')
line_score = pd.read_csv('./csv/line_score.csv')
officials = pd.read_csv('./csv/officials.csv')
other_stats = pd.read_csv('./csv/other_stats.csv')
player = pd.read_csv('./csv/player.csv')
team_details = pd.read_csv('./csv/team_details.csv')
team_history = pd.read_csv('./csv/team_history.csv')
team_info_common = pd.read_csv('./csv/team_info_common.csv')
team = pd.read_csv('./csv/team.csv')

diccionarioDataFrame = {
    'common_player_info': common_player_info,
    'draft_combine_stats': draft_combine_stats,
    'draft_history': draft_history,
    'game_info': game_info,
    'game_summary': game_summary,
    'game': game,
    'inactive_players': inactive_players,
    'line_score': line_score,
    'officials': officials,
    'other_stats': other_stats,
    'player': player,
    'team_details': team_details,
    'team_history': team_history,
    'team_info_common': team_info_common,
    'team': team
}

for name, df in diccionarioDataFrame.items():
    print(f"\n=== {name} ===")
    print(df.head())
    print("\nDescripción estadística:")
    print(df.describe())