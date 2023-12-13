import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=".",intents = discord.Intents.all()) # Creating bot

@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.tree.sync()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.content)

@bot.tree.command(name="dan",description="...")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hi aekkawit :D")

@bot.command()
async def av(ctx,member: discord.Member):
    await ctx.send(member.display_avatar)

@bot.tree.command(name="avatar",description="Get user avatar")
async def avatar(interaction:discord.Interaction,member:discord.Member):
    await interaction.response.send_message(member.display_avatar)


bot.run("MTE3NzIyMzA1NTk5NTU4ODYzOA.G5aVji.v-8JhIBQ4Ya_j9B8VL7O_SzIFOBk8AR-6dQabI")