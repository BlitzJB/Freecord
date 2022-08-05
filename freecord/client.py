from types import FunctionType

import inspect




class Client:
    def __init__(self) -> None:
        self.__callbacks = {}


    def command(self, callback: FunctionType, name=None, description=None) -> None:
        """
            Registers a command
        """

        if not name:
            name = callback.__name__

        if not description:
            pass # TODO check if description is mandatory to define command else leave blank

        if name in self.__callbacks:
            raise Exception(f"Command function with name `{name}` has already been defined!")
        
        self.__callbacks[callback.__name__] = callback

    def _register_commands(self):
        """
            Regsiters all the added comands with discord
        """
        ...


if __name__ == '__main__':
    client = Client()

    @client.command
    def fun():
        print('fun')
