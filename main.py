#Beta Bot 0.5
#Templet copy

import logging
import discord
from discord.ext import commands
import utils

import settings

logger = logging.getLogger("bot")

#The cod below is part of Python function that is being defined:
def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)
#These lines are setting up the bot's intents and creating an instance of the Bot class from the commands module.
    #The intents variavle is set to the default intents provied by Discord API,and the message_content variable is set to True,
    #which allows the bot to receive the contents of messages.

#the next few lines are defing event listeners for the bot:
    @bot.event
    async def on_ready():
        logging.info(f"User: {bot.user} (ID: {bot.user.id})")
        await utils.load_videocmds(bot)
#The on_ready event listener is being defind, which will be triggered when the bot connects to Discord.
#In this function, the bot's user information is logged, and the load_videocmds function is being called,
#witch will load any video commands that have been defined


#The next few lines are defing a command that can be use by users:
    @bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send("pong")
#The ping command is being defined, which will respond with "pong" when it is invoked.
#The ctx parameter is a Context that provides information about the invocation, including the message that trggered the command.


#Finally, the bot is being started using the API token stored in the DISCORD_API_SECRET environment variable,
#and the root logger is being used
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__ == "__main__":
    run()
