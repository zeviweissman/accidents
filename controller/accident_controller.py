from repository.seed_repository import init_accidents
import repository.accident_repository as repos
from flask import Blueprint, jsonify, request

accident_blueprint = Blueprint("controller", __name__)


@accident_blueprint.route('/', methods=['GET'])
def seed_data_base():
    init_accidents()
    return jsonify("OK"), 200


@accident_blueprint.route('/<beat>', methods=['GET'])
def get_total_accidents_by_beat(beat):
    return jsonify(repos.get_total_accidents_by_beat(beat)), 200


@accident_blueprint.route('/<beat>/date', methods=['GET'])
def get_total_accidents_by_beat_and_date(beat):
    date = request.args.get('date')
    return jsonify(repos.get_total_accidents_by_beat_and_date(beat, date)), 200


@accident_blueprint.route('/<beat>/week', methods=['GET'])
def get_total_accidents_by_beat_and_week(beat):
    date = request.args.get('date')
    return jsonify(repos.get_total_accidents_by_beat_and_week(beat, date)), 200

@accident_blueprint.route('/<beat>/cause', methods=['GET'])
def get_accidents_by_beat_grouped_by_cause(beat):
    return jsonify(repos.get_accident_info_by_beat_grouped_by_primary_cause(beat))