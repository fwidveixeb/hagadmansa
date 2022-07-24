import os
import aiofiles
from aiofiles import os
from telegraph import upload_file
from pyrogram import Client, filters

@Client.on_message(filters.command("telegraph"))
async def telegraph(bot, message):
    
    replied = message.reply_to_message
    
    if not replied:
        await message.reply("Command Incomplete, read Help Menu first.")
        return
            
    if replied.photo:
        p = await message.reply("Downloading...")
        user_id = str(message.chat.id)
        img_path = (f"./DOWNLOADS/{user_id}.jpg")
        img_download = await bot.download_media(message=replied, file_name=img_path)
        await p.edit("Uploading...")
        try:         
            tgraph_img = upload_file(img_download)
            await p.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_img[0]}", disable_web_page_preview=True)     
            os.remove(img_download) 
        except Exception as e:
            await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    elif replied.video:
        if replied.video.file_size < 5242880:
            a = await message.reply_text("Downloading...")
            user_id = str(message.chat.id)
            vid_path = (f"./DOWNLOADS/{user_id}.mp4")
            vid_download = await bot.download_media(message=replied, file_name=vid_path)
            await a.edit("Uploading...")
            try:
                tgraph_vid = upload_file(vid_download)
                await a.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_vid[0]}", disable_web_page_preview=True)     
                os.remove(vid_download) 
            except Exception as e:
                await a.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.animation:
        if replied.animation.file_size < 5242880:
            g = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            gif_path = (f"./DOWNLOADS/{user_id}.mp4")
            gif_download = await bot.download_media(message=replied, file_name=gif_path)
            await g.edit("Uploading...")
            try:
                tgraph_gif = upload_file(gif_download)
                await g.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_gif[0]}", disable_web_page_preview=True)     
                os.remove(gif_download) 
            except Exception as e:
                await g.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.document:
        if replied.document.file_size < 5242880 and replied.document.file_name.endswith('.html', '.txt', '.py'):
            l = await message.reply("Downloading...")
            down = await bot.download_media(message=replied)
            await l.edit("Uploading...")
            async with aiofiles.open(down, "r") as jv:
                text = await jv.read()
            header = message.input_str
            if not header:
                header = "Hagadmansa"
            from telegraph import Telegraph
            telegraph = Telegraph()
            telegraph.create_account(short_name="Hagadmansa")
            try:
                resp = telegraph.create_page(f'{header}',html_content=text)
                await b.edit(f"Here is your link:\n\n{resp['url']}", disable_web_page_preview=True)
            except Exception as e:
                await b.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    elif replied:
        b = await message.reply("Uploading...")
        from telegraph import Telegraph
        telegraph = Telegraph()
        telegraph.create_account(short_name="Hagadmansa")
        if (message.command):
            title = message.command[1:]
            try:
                title = title
            except: 
                title = "Hagadmansa"
        br = replied.text.html.replace("\n", "<br>")
        try:
            response = telegraph.create_page(f'{title}',html_content=br)
            await b.edit(f"Here is your link:\n\n{response['url']}", disable_web_page_preview=True)
        except Exception as e:
            await b.delete()
            await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    else:     
        await bot.reply("Reply to a Photo, Video, Gif or Text only.")
    
    
                
