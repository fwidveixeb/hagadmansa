import os
from telegraph import Telegraph
from telegraph import upload_file
from pyrogram import Client, filters

#Create Telegra.ph Account
tg = Telegraph()
tg.create_account(short_name="Hagadmansa")

def listToString(s):
    str1 = " "
    return (str1.join(s))

@Client.on_message(filters.command("telegraph"))
async def telegraph(bot, message):
    
    replied = message.reply_to_message
    
    if not replied:
        await message.reply("Command Incomplete, read Help Menu first.")
        return
    
    if not replied.text and not replied.photo and not replied.video and not replied.animation and not replied.document:
        await message.reply("Reply to a message, photo, video, animation or document only")
        return
        
    if replied.photo:
        p = await message.reply("`Downloading...`")
        img_path = (f"./DOWNLOADS/{message.chat.id}.jpg")
        img_download = await bot.download_media(message=replied, file_name=img_path)
        await p.edit("`Uploading...`")
        try:         
            tgraph_img = upload_file(img_download)
            await p.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_img[0]}", disable_web_page_preview=True)     
            os.remove(img_download) 
        except Exception as e:
            await p.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    elif replied.video:
        if replied.video.file_size < 5242880:
            a = await message.reply_text("`Downloading...`")
            vid_path = (f"./DOWNLOADS/{message.chat.id}.mp4")
            vid_download = await bot.download_media(message=replied, file_name=vid_path)
            await a.edit("`Uploading...`")
            try:
                tgraph_vid = upload_file(vid_download)
                await a.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_vid[0]}", disable_web_page_preview=True)     
                os.remove(vid_download) 
            except Exception as e:
                await a.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.animation:
        if replied.animation.file_size < 5242880:
            g = await message.reply("`Downloading...`")
            gif_path = (f"./DOWNLOADS/{message.chat.id}.mp4")
            gif_download = await bot.download_media(message=replied, file_name=gif_path)
            await g.edit("`Uploading...`")
            try:
                tgraph_gif = upload_file(gif_download)
                await g.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_gif[0]}", disable_web_page_preview=True)     
                os.remove(gif_download) 
            except Exception as e:
                await g.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.document:
        if replied.document.file_size < 5242880:
            if replied.document.file_name.lower().endswith('.png'):
                q = await message.reply("`Downloading...`")
                img_pathq = (f"./DOWNLOADS/{message.chat.id}.png")
                img_downloadq = await bot.download_media(message=replied, file_name=img_pathq)
                await q.edit("`Uploading...`")
                try:   
                    tgraph_imgq = upload_file(img_downloadq)
                    await q.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_imgq[0]}", disable_web_page_preview=True)     
                    os.remove(img_downloadq) 
                except Exception as e:
                    await q.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            elif replied.document.file_name.lower().endswith('.jpg'):
                i = await message.reply("`Downloading...`")
                img_pathi = (f"./DOWNLOADS/{message.chat.id}.jpg")
                img_downloadi = await bot.download_media(message=replied, file_name=img_pathi)
                await i.edit("`Uploading...`")
                try:   
                    tgraph_imgi = upload_file(img_downloadi)
                    await i.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_imgi[0]}", disable_web_page_preview=True)     
                    os.remove(img_downloadi) 
                except Exception as e:
                    await i.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            elif replied.document.file_name.lower().endswith('.jpeg'):
                y = await message.reply("`Downloading...`")
                img_pathy = (f"./DOWNLOADS/{message.chat.id}.jpeg")
                img_downloady = await bot.download_media(message=replied, file_name=img_pathy)
                await y.edit("`Uploading...`")
                try:   
                    tgraph_imgy = upload_file(img_downloady)
                    await y.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_imgy[0]}", disable_web_page_preview=True)     
                    os.remove(img_downloadi) 
                except Exception as e:
                    await y.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            elif replied.document.file_name.lower().endswith('.mp4'):
                z = await message.reply("`Downloading...`")
                img_pathz = (f"./DOWNLOADS/{message.chat.id}.mp4")
                img_downloadz = await bot.download_media(message=replied, file_name=img_pathz)
                await z.edit("`Uploading...`")
                try:   
                    tgraph_imgz = upload_file(img_downloadz)
                    await z.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_imgz[0]}", disable_web_page_preview=True)     
                    os.remove(img_downloadz)
                except Exception as e:
                    await z.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            else:
                x = await message.reply("`Downloading...`")
                path = (f"./DOWNLOADS/{message.chat.id}.txt")
                await bot.download_media(message=replied, file_name=path)
                await x.edit("`Uploading...`")
                k = open(path)
                p = k.read()
                if (message.command):
                    pk = message.command[1:]
                    if not pk:  
                        pk = "Hagadmansa" 
                if pk == "Hagadmansa":
                    monu = "Hagadmansa"
                else:
                    monu = listToString(pk)
                try:
                    response = tg.create_page(title=f'{monu}', content=[f"{p}"], author_name="Hagadmansa", author_url="https://hagadmansa.com")  
                    await x.edit(f"Here is your link:\n\n{response['url']}", disable_web_page_preview=True)
                    k.close()
                except Exception as e:
                    await x.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
        
        
    elif replied.text:
        b = await message.reply("`Uploading...`")
        if (message.command):
            dj = message.command[1:]
            if not dj:
                dj = "Hagadmansa"
        if dj == "Hagadmansa":
            somu = "Hagadmansa"
        else:
            somu = listToString(dj)
        try:
            response = tg.create_page(title=f'{somu}', content=[f"{replied.text}"], author_name="Hagadmansa", author_url="https://hagadmansa.com")
            await b.edit(f"Here is your link:\n\n{response['url']}", disable_web_page_preview=True)
        except Exception as e:
            await b.edit(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
   
