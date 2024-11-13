from flask import Flask, jsonify, request
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, shotchartdetail

app = Flask(__name__)

def get_player(player_name):
    nba_players = players.get_players()
    
    # Imprimir todos os jogadores para debug
    print([player['full_name'] for player in nba_players])
    
    # Busca por nome de jogador, ignorando diferenças de maiúsculas/minúsculas
    player_dict = [player for player in nba_players if player_name.lower() in player['full_name'].lower()]
    
    # Verifica se o jogador foi encontrado
    if not player_dict:
        raise ValueError("Player not found")
    
    player_dict = player_dict[0]  # Pegue o primeiro jogador que corresponde
    player_regular_info = playercareerstats.PlayerCareerStats(player_id=int(player_dict['id']), per_mode36='PerGame')
    player_regular_info_df = player_regular_info.get_data_frames()[0].drop_duplicates(subset=['SEASON_ID'], keep='last')
    
    # Exibir todas as temporadas disponíveis para o jogador
    print("Available seasons for the player:", player_regular_info_df['SEASON_ID'].tolist())
    
    return player_regular_info_df

@app.route('/api/player_stats', methods=['GET'])
def player_stats():
    player_name = request.args.get('player_name')
    season_id = request.args.get('season_id')

    # Verifica se os parâmetros foram fornecidos
    if not player_name or not season_id:
        return jsonify({"error": "player_name and season_id are required"}), 400
    
    try:
        player_regular_info_df = get_player(player_name)
        season = player_regular_info_df[player_regular_info_df['SEASON_ID'] == season_id]
        
        if season.empty:
            return jsonify({"error": "No data found for the given player and season"}), 404
        
        stats = {
            "age": int(season['PLAYER_AGE']),
            "gp": int(season['GP']),
            "gs": int(season['GS']),
            "min": round(float(season['MIN']), 2),
            "pts": float(season['PTS']),
            "reb": float(season['REB']),
            "ast": float(season['AST']),
            "fg_pct": round(float(season['FG_PCT']*100), 2),
            "fg3_pct": round(float(season['FG3_PCT']*100), 2),
            "ft_pct": round(float(season['FT_PCT']*100), 2),
            "stl": float(season['STL']),
            "blk": float(season['BLK']),
            "tov": float(season['TOV']),
        }
        return jsonify(stats)
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/player_shotchart', methods=['GET'])
def player_shotchart():
    player_name = request.args.get('player_name')
    season_id = request.args.get('season_id')

    # Verifica se os parâmetros foram fornecidos
    if not player_name or not season_id:
        return jsonify({"error": "player_name and season_id are required"}), 400
    
    try:
        nba_players = players.get_players()
        player_dict = [player for player in nba_players if player_name.lower() in player['full_name'].lower()]
        
        # Verifica se o jogador foi encontrado
        if not player_dict:
            raise ValueError("Player not found")
        
        player_dict = player_dict[0]
        
        career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
        career_df = career.get_data_frames()[0].drop_duplicates(subset=['SEASON_ID'], keep='last')
        team_id = career_df[career_df['SEASON_ID'] == season_id]['TEAM_ID']
        
        if team_id.empty:
            return jsonify({"error": "No team found for the given season"}), 404
        
        shotchart_data = shotchartdetail.ShotChartDetail(
            team_id=int(team_id),
            player_id=int(player_dict['id']),
            season_nullable=season_id,
            season_type_all_star='Regular Season'
        ).get_data_frames()

        shot_data = shotchart_data[0].to_dict(orient='records')  # Convert to list of dictionaries
        return jsonify(shot_data)
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
