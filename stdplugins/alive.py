""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Jinda Hai apun Jab Tak Ye khel Khatam Nahi Hota Apun Idharich Hai\n\nTelethon version: 1.10.6\nPython: 3.7.4\nUser: @rajdeshmukh7\nGithub repo: https://github.com/Rajdeshmukh77/Pornhub`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
