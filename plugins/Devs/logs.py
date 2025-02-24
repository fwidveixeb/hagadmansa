import os
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command(['log', 'logs']) & filters.user(ADMINS))
async def logs(bot, message):
    try:
        os.rename('TelegramBot.log', 'Hagadmansa.log')
        await message.reply_document(document='Hagadmansa.log', caption='Bot Logs')
    except FileNotFoundError:
        try:
            await message.reply_document(document='Hagadmansa.log', caption='Bot Logs')
        except Exception as e:
            await message.reply(str(e))
    except Exception as e:
        await message.reply(str(e))
