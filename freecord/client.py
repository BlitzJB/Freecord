from types import FunctionType
from typing import Dict, List

from .server import build_flask_app
from .models import ApplicationContext, ApplicationCommand

class Client:
    def __init__(self) -> None:
        self._callbacks = {}


    def command(self, name: str = None, description: str = None, options = [], scope = None) -> None:
        """
            Registers a command
        """
        print(name)
        def wrapper(callback: FunctionType):
            if not name:
                name = callback.__name__

            if not description:
                description = ''
            
            if name in self._callbacks:
                raise Exception(f"Command function with name `{name}` has already been defined!")

            self._callbacks[name]: Dict[str, ApplicationCommand] = ApplicationCommand(callback, name, description, options, scope)
        return wrapper


    def _register_commands(self, application_context: ApplicationContext):
        """
            Regsiters all the added comands with discord
        """
        commands: List[ApplicationCommand] = list(self._callbacks.values())
        register_tasks = [command.create_register_task(application_context) for command in commands]
        # TODO Execute async and retry failed


    def run(self, token, application_id, public_key, host='0.0.0.0', port=5000):
        self._server = build_flask_app(public_key)
        context = ApplicationContext(token, application_id, public_key)
        self._register_commands(context)
        self._server.run(host, port)
        

    def _seialized(self):
        return [command.serialize() for command in self._callbacks.values()]


if __name__ == '__main__':
    client = Client()

    @client.command(scope=1823818238)
    def fun():
        print('fun')
