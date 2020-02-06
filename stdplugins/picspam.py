Learn more or give us feedback

# Copyright (C) 2019 The Raphielscape Company LLC.

#

# Licensed under the Raphielscape Public License, Version 1.b (the "License");

# you may not use this file except in compliance with the License.

#

from asyncio import wait

from telethon import events

@register(outgoing=True, pattern="^.picspam")

async def tiny_pic_spam(e):

    message = e.text

        text = message.split()

            counter = int(text[1])

                link = str(text[2])

                    await e.delete()

                        for i in range(1, counter):

                                await e.client.send_file(e.chat_id, link)

                                    if BOTLOG:

                                            await e.client.send_message(

                                                        BOTLOG_CHATID, "#PICSPAM\n"

                                                                    "PicSpam was executed successfully")
