import discord
import json
from discord.ext import commands, tasks
from itertools import cycle




client=commands.Bot(command_prefix='')
status = cycle(['status 1', 'status 2'])
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Please invite this bot to your server'))
    print("bot is ready")

@tasks.loop(seconds=10)
async def statusOfBot():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 3000)} ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages has been deleted')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    await member.send(f'Hello {member}')
    #await ctx.send(f'say hello to {member}')

    





@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick()
    await member.send(f'You have been kicked for {reason}')
    await ctx.send(f'{member.mention} has been kicked')
    print(f'{member} has been kicked')

@client.command()
async def ban(ctx, member : discord.member, *, reason=None):
    await member.kick()
    await member.send(f'You have been banned for {reason}')
    await ctx.send(f'{member.mention} has been kicked')
    print(f'{member} has been kicked')




client.run('NzU2OTA3NTMxMjc1NzMxMDA1.X2YrEg.LEQaXXR6TNujLX4W_70scPV7nOw')

