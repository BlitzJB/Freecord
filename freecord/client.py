from types import FunctionType
from typing import Dict, List
import aiohttp, asyncio

from .server import build_flask_app
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
        context = ApplicationContext(token, application_id, public_key)
        self._register_commands(context)
        return build_flask_app(public_key)
        

    def _seialized(self):
        return [command.serialize() for command in self._callbacks.values()]


if __name__ == '__main__':
    ...
