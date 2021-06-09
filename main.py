from dotenv import dotenv_values

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

config = dotenv_values(".env")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

guild_ids = [int(config['GUILD_ID'])] # Put your server ID in this array.

@slash.slash(name="TeamCreate", description="Create a team in the league.", guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(config['BOT_TOKEN'])