from flask import request, jsonify, abort, make_response
from flask_api import FlaskAPI

# local import
from controller import generate_tracks
from settings import app_config
from error import NotEnoughLecturesError

app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object(app_config['production'])

@app.route('/api/v1/lecture_manager', methods=['POST', ])
def lecture_manager():
    if not request.json:
        return make_response(jsonify({"error": "No lecture to manage"}), 400)

    data = request.json
    if type(data) is not dict:
        return make_response(jsonify({"error": "payload must be a json with key, value"}), 400)

    if not data.get('data'):
        return make_response(jsonify({"error": "Data must by a value of a 'data' key"}), 400)

    if type(data.get('data')) is not list:
        return make_response(jsonify({"error": "Data set must by an array"}), 400)
    try:
        response = generate_tracks(data['data'])
    except NotEnoughLecturesError:
        response = {'error': 'Not enough lectures to create a single track'}
        status_code = 400
    except Exception:
        response = {'error': 'payload is not in a correct format'}
        status_code = 400
    else:
        status_code = 200
    finally:
        return make_response(jsonify(response), status_code)

if __name__ == "__main__":
    app.run()