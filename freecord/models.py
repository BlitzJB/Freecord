from typing import Dict, List
import aiohttp

from freecord.enums import ApplicationCommandType, OptionType
from freecord.register import register_as_global_command, register_as_guild_command



class ApplicationCommand:
    def __init__(self, callback, name, description, options, scope) -> None:
        self.name = name
        self.description = description
        self.options: List[Option] = options
        self.callback = callback
        self.scope = scope


    async def create_register_task(self, session: aiohttp.ClientSession,  application_ctx: 'ApplicationContext'):
        self.headers = {
            "Authorization": f"Bot {application_ctx.token}"
        }

        self.json = self.serialize()

        if self.scope: 
            register_as_guild_command(session, self.json, application_ctx.application_id, application_ctx.token, self.scope)
            return

        register_as_global_command(session, self.json, application_ctx.application_id, application_ctx.token)

    
    def serialize(self):
        return {
            'name': self.name,
            'type': ApplicationCommandType.CHAT_INPUT,
            'description': self.description,
            'options': [option.serialize() for option in self.options]
        }


class ApplicationContext:
    def __init__(self, token, application_id, public_key) -> None:
        self.token = token
        self.application_id = application_id
        self.public_key = public_key


class Option:
    def __init__(self, name: str, description: str, type: OptionType, required: bool = False, choices: Dict[str, str] = None) -> None:
        self.name = name
        self.description = description
        self.type = type
        self.required = required
        self.choices = choices

    def serialize(self) -> dict:
        options = {
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'required': self.required
        }
        if self.choices:
            options['choices'] = self.choices

        return options


