from discord.ext import (commands)
from libs.help import EmbedHelp
from libs.embed import Embed
from typing import Any

import wolframalpha

APP_ID = "im not posting the app id publicly" # use enviorment vars/secrets or something ltr
CLIENT = wolframalpha.Client(APP_ID)

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *args):
        """Queries WolframAlpha"""
        args = " ".join(args)
        if args.strip() == "":
            await ctx.send(Embed(title="Error", description="No Query"))
        else:
            res = CLIENT.query(args)
            result = next(res.results).text
            result_embed = Embed(title="Solution", description=result)
            await ctx.send(result_embed())


def setup(bot) -> dict[str, Any]:
    return {
        "Object": Ask(bot),
        "name": "ask",
        "description": "Adds the ability to ask computational intelligence a complex question"
    }
