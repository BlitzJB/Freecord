from flask import Flask, request, jsonify
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


def build_flask_app(public_key):

    app = Flask(__name__)

    @app.route('/interactions', methods = ['POST'])
    @verify_key_decorator(public_key)
    def interactions():
        if request.json['type'] == InteractionType.APPLICATION_COMMAND:
            return jsonify({
                'type': InteractionResponseType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE,
                'data': {
                    'content': str(dict(request.json))
                }
            })
    
    return app
