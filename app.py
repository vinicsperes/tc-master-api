from flask import Flask, jsonify
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import shotchartdetail

app = Flask(__name__)

def get_shot_chart(player_name, season_id, season_progress):
    # Obter o ID do jogador
    nba_players = players.get_players()
    player = next((p for p in nba_players if p['full_name'] == player_name), None)
    if not player:
        return {"error": "Player not found"}

    # Obter o ID do time do jogador
    # Supondo que o jogador está no time correto nesta temporada
    nba_teams = teams.get_teams()
    player_id = player['id']
    
    # Obter os dados do shot chart
    shotchart = shotchartdetail.ShotChartDetail(
        team_id=0,  # Aqui, tente substituir pelo ID do time correto
        player_id=player_id,
        season_nullable=season_id,
        season_type_all_star=season_progress
    ).get_data_frames()
    
    # Retorna os dados em formato JSON
    shot_data = shotchart[0].to_dict(orient="records")
    return shot_data

@app.route('/shot-chart/<player_name>/<season_id>/<season_progress>')
def shot_chart(player_name, season_id, season_progress):
    try:
        data = get_shot_chart(player_name, season_id, season_progress)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
