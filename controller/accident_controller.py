import repository.seed_repository as seed_repos
from flask import Blueprint, jsonify

accident_blueprint = Blueprint("controller", __name__)


@accident_blueprint.route('/<player_position>', methods=['GET'])
def get_players_by_postion(player_position):
    players = player_service.get_all_players_by_postion(player_position)
    return jsonify(players), 200



