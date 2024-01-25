#Beta Bot 0.5
#Templet copy

import unittest
import discord
from discord.ext import commands
from contextlib import contextmanager
from unittest.mock import patch
import logging

import setting

logger = logging.getLogger("bot")


class Beta_Bot(unittest.TestCase):
    def setUp(self):
        self.bot = commands.Bot(command_prefix='!')
        self.ctx = self.bot.get_context('dummy message')

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logging.info(f"User: {bot.user} (ID: {bot.user.id})")
        await utils.load_videocmds(bot)

    @bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send("pong")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__ == "__main__":
    run()