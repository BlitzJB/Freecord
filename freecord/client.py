from types import FunctionType
from typing import List

from .server import build_flask_app
from .models import ApplicationContext, ApplicationCommand

class Client:
    def __init__(self) -> None:
        self.__callbacks = {}


    def command(self, callback: FunctionType, scope = None) -> None:
        """
            Registers a command
        """

        if callback.__name__ in self.__callbacks:
            raise Exception(f"Command function with name `{callback.__name__}` has already been defined!")
        
        self.__callbacks[callback.__name__] = ApplicationCommand(callback, scope)


    def _register_commands(self, application_context: ApplicationContext):
        """
            Regsiters all the added comands with discord
        """
        commands: List[ApplicationCommand] = list(self.__callbacks.values())
        register_tasks = [command.create_register_task(application_context) for command in commands]
        # TODO Execute async and retry failed


    def run(self, token, application_id, public_key, host='0.0.0.0', port=5000):
        self.__server = build_flask_app(public_key)
        context = ApplicationContext(token, application_id, public_key)
        self._register_commands(context)
        self.__server.run(host, port)
        

if __name__ == '__main__':
    client = Client()

    @client.command(scope=1823818238)
    def fun():
        print('fun')
