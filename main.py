import os 
import discord
from discord.ext import commands
import sqlite3
import traceback
import sys
import asyncpg
from asyncpg.pool import create_pool
import json
import keep_alive


token = os.environ.get("token")
prefix = os.environ.get("prefix")
database_url = os.environ.get("DATABASE_URL")





intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.all())
bot.remove_command('help')
intents.members = True

#databse
async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database_url)
    print("[\] DATABASE CONNECTED")

#Ready
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="DMs for help") )
    print("[\] BOT ONLNE")


#modules Importing
with open ('./config/modules.json', 'r') as f:
    cogsData = json.load(f)
    module = cogsData['extensions']

if __name__ == "__main__":
    for values in module:
        try:
            bot.load_extension(values)
            print(f"[/] loaded | {values}")
        except:
            print(f'Error loading {values}', file=sys.stderr)
            traceback.print_exc()

keep_alive.keep_alive()
bot.loop.run_until_complete(create_db_pool())
bot.run(token)