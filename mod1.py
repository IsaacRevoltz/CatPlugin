import asyncio
from collections import deque

from userbot.plugins import catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="k$",
    command=("k", plugin_category),
    info={
        "header": "Animation command",
        "usage": "{tr}k",
    },
)
async def K(e):
    "Animation command."
    t = "K"
    catevent = await edit_or_reply(e, t)
    for _ in range(20):
        await asyncio.sleep(0.1)
        t = t[:-1] + "KKK"
        await catevent.edit(t)
        

@catub.cat_cmd(
    pattern="fds$",
    command=("fds", plugin_category),
    info={
        "header": "Foda-se?",
        "usage": "{tr}fds",
    },
)
async def iqless(e):
    "Foda-se?"
    await edit_or_reply(e, "F\n"
"     O\n"
"　　 O\n"
"　　　O\n"
"　　　 o\n"
"ₒ ᵒ 。   o\n"
"ᵒ ₒ °ₒ  ᵒ\n"
"　 ˚\n"
"　°\n"
"　•\n"
"　 .\n"
"　　.   \n"
"           da-se?")


@catub.cat_cmd(
    pattern="sexo$",
    command=("sexo", plugin_category),
    info={
        "header": "kkkkkkkhkkkkk sexo bixo",
        "usage": "{tr}sexo",
    },
)
async def _(event):
    "Mostra um meme sexokkkkkkkk."
    animation_ttl = range(4)
    event = await edit_or_reply(event, "sexo?")
    animation_chars = [
        "HOLY SHIT!!",
        "IS THAT A\n"
"MOTHERFUCKING\n"
"█▀▀ █▀▀ █─█ █▀▀█ \n"
"▀▀█ █▀▀ ▄▀▄ █──█ \n"
"▀▀▀ ▀▀▀ ▀─▀ ▀▀▀▀\n"
"           REFERENCE???",
        "Perai...é aqui que estão falando de...",
        "KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"KKKK\n"
"KKKK\n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"               KKKK\n"
"               KKKK\n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"  \n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"KKKK\n"
"KKKK\n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"KKKK\n"
"KKKK\n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"  \n"
"KKKK       KKKK\n"
" KKKK    KKKK\n"
"   KKKK KKKK\n"
"      KKKKKK\n"
"      KKKKKK\n"
"      KKKKKK\n"
"  KKKK     KKKK\n"
"KKKK        KKKK\n"
"  \n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"KKKK     KKKK\n"
"KKKK     KKKK\n"
"KKKK     KKKK\n"
"KKKK     KKKK\n"
"KKKKKKKKKK\n"
"KKKKKKKKKK\n"
"  \n"
"  KKKKKKKK\n"
"KKKKKKKKKK\n"
"KKK        KKK\n"
"              KKK\n"
"            KKK\n"
"          KKK\n"
"        KKK\n"
"      KKK\n"  
"      KKK\n"   
"    \n"
"      KKK\n"
"      KKK",
    ]
    for i in animation_ttl:
        await asyncio.sleep(2)
        await event.edit(animation_chars[i % 4])


