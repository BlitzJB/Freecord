from aiohttp import ClientSession


async def register_as_global_command(session: ClientSession, payload, app_id, token):
    url = f"https://discord.com/api/v10/applications/{app_id}/commands" 
    headers = {
        "Authorization": f"Bot {token}"
    }

    async with session.post(url, json=payload, headers=headers) as resp:
        print(f'Registering Global command {payload["name"]}', resp.status)
        print(await resp.text('utf-8'))


async def register_as_guild_command(session: ClientSession, payload, app_id, token, guild_id): 
    url = f"https://discord.com/api/v10/applications/{app_id}/guilds/{guild_id}/commands"
    headers = {
        "Authorization": f"Bot {token}"
    }

    async with session.post(url, json=payload, headers=headers) as resp:
        print(f'Registering Guild Command {payload["name"]}', resp.status)
        print(await resp.text('utf-8'))
