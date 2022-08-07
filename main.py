from freecord.client import Client
from freecord.models import Option, ApplicationContext
from freecord.enums import OptionType


client = Client()

@client.command(
    name='imagined_commadn',
    description='This is an awesome command',
    options=[
        Option(
            name='first',
            description='first option',
            type=OptionType.BOOLEAN
        )
    ],
)
def functionname(ctx, first):
    ...



app = client.run(
    'ODA5NDg1MTQ2MjY0MDQzNTMw.GENofT.jkQZSx2V29uFAQXc3T5n2gIXusdnUDudeFact0',
    809485146264043530,
    '9f4bdc04868c707bd3061801691edc551277781ae0180e32ca0f1bf15ca8ed34'
)