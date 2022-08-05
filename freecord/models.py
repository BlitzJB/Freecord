import aiohttp

class ApplicationCommand:
    def __init__(self, callback, scope, application_ctx: 'ApplicationContext') -> None:
        self.callback = callback
        self.scope = scope

        self.headers = {
            "Authorization": f"Bot {application_ctx.token}"
        }

        self.json = {
            ...
        }

    async def create_register_task(self):
        if self.scope: ...


class ApplicationContext:
    def __init__(self, token, application_id) -> None:
        self.token = token
        self.application_id = application_id