from types import FunctionType
from typing import Dict, List
import aiohttp, asyncio
from flask import Flask, request, jsonify
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


from .models import ApplicationContext, ApplicationCommand

class Client:
    def __init__(self) -> None:
        self._callbacks = {}


    def command(self, name: str = None, description: str = None, options = [], scope = None) -> None:
        """
            Registers a command
        """

        def wrapper(callback: FunctionType):

            if name in self._callbacks:
                raise Exception(f"Command function with name `{name}` has already been defined!")

            self._callbacks[name]: Dict[str, ApplicationCommand] = ApplicationCommand(callback, name, description, options, scope)
        return wrapper


    def build_flask_app(self, token, application_id, public_key):

        app = Flask(__name__)


        @app.route('/')
        def index():

            async def register():
                context = ApplicationContext(token, application_id, public_key)
                self._register_commands(context)

            return str(asyncio.run(register()))


        @app.route('/interactions', methods = ['POST'])
        @verify_key_decorator(public_key)
        def interactions():
            if request.json['type'] == InteractionType.APPLICATION_COMMAND:
                print('command_triggered', dict(request.json))
                return jsonify({
                    'type': InteractionResponseType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE,
                    'data': {
                        'content': 'str(dict(request.json))'
                    }
                })
        
        return app


    async def _register_commands(self, application_context: ApplicationContext):
        """
            Regsiters all the added comands with discord
        """
        commands: List[ApplicationCommand] = list(self._callbacks.values())
        async with aiohttp.ClientSession() as session:
            register_tasks = [command.create_register_task(session, application_context) for command in commands]
            output = await asyncio.gather(*register_tasks)
        print(output)
        # TODO Execute async and retry failed


    def run(self, token, application_id, public_key):
        return self.build_flask_app(token, application_id, public_key)
        

    def _seialized(self):
        return [command.serialize() for command in self._callbacks.values()]


if __name__ == '__main__':
    ...
