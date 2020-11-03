import discord
from discord.ext import commands
from decouple import config
from PyInquirer import prompt

from admin import AdminTools
from misc import Miscellaneous
from roles import RoleManagement
from mensa import Mensa

cogs = (AdminTools, Miscellaneous, RoleManagement, Mensa)


def application_choice():  # choosing application
    application_question = [
        {
            'type': 'list',
            'name': 'application',
            'message': 'Which application should be logged in?',
            'choices': ['Chester McTester', 'infobot'],
        },
    ]
    application = prompt(application_question)

    print('...')

    if application['application'] == 'infobot':
        return config('INFOBOT')
    else:
        return config('TEST')


if __name__ == '__main__':

    intents = discord.Intents.default()
    intents.members = True

    client = commands.Bot(command_prefix='!',
                          help_command=None,
                          intents=intents)

    app = application_choice()

    for cog in cogs:
        client.add_cog(cog(client, app))
        print(f'Added cog {cog}')

    @client.event  # Connection confirmation
    async def on_ready():
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Prefix: '!'"))
        print(f'🆗 {client.user} has connected to Discord!')

    client.run(app)
