from discord.ext import commands


class Hello(commands.Cog):
    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send(f'Hi {ctx.author}! Try !foo or !bar')

    @commands.Cog.listener()
    async def on_mention(self, message, text):
        # Fired when a Member @mentions the bot with anything that isn't a Command
        await message.reply(f'Hi {message.author}!. Unfortunately I can\'t respond to that. Try !foo or !bar instead.')
