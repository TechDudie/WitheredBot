from discord import (Embed)


PREFIX = "!"


async def embed_help(help="", accepted_args=[], usage=""):

    embed = Embed(
        title="Usage", description=msgf(f"[C]{PREFIX}{help}[C]"),
    )
    if accepted_args != []:
        accepted_args = ', '.join(accepted_args)
        embed.add_field(name="Args", value=f"```{accepted_args}```")
    if usage != "":
        embed.add_field(name="Usage", value=f"```{usage}```")
    return embed


def msgf(s):
    format_info = {
        "[B]": "**",
        "[I]": "*",
        "[H]": "||",
        "[C]": "```",
         "[L]": "`",
        "[Q/]": "> ",
    }
    sk = []
    for key, val in format_info.items():
        if key in s:
            s = s.replace(key, val)
    sk = s
    return sk