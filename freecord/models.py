import aiohttp



class ApplicationCommand:
    def __init__(self, callback, scope) -> None:
        self.callback = callback
        self.scope = scope


    async def create_register_task(self, application_ctx: 'ApplicationContext'):
        self.headers = {
            "Authorization": f"Bot {application_ctx.token}"
        }

        self.json = {
            ...
        }
        if self.scope: ...



class ApplicationContext:
    def __init__(self, token, application_id, public_key) -> None:
        self.token = token
        self.application_id = application_id
        self.public_key = public_key