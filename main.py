# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import helper
import random
import zipfile
from helper import get_drm_keys

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message 
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

@bot.on_message(filters.command(["jaishreeram"]))    
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text("**👋 ʜᴇʟʟᴏ!\n🌟ɪ ᴀᴍ ᴛxᴛ ꜰɪʟᴇ ᴅᴏᴡʟᴏᴀᴅᴇʀ ʙᴏᴛ ** \n\n❤️‍🔥 **ᴘʀᴇꜱꜱ [baap se permission li?] ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʙʏ ᴛxᴛ**\n\n❤💖 **ᴊᴏɪɴ ᴏᴜʀ <a href='https://t.me/LP_YAGAMI/'>ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ</a>** \n\n<pre>💕 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : https://t.me/LP_LUCIFER</pre>\n-═════━‧₊˚❀༉‧₊˚.━═════-")
    
@bot.on_message(filters.command("ruko"))
async def restart_handler(_, m):
    await m.reply_text("💀💀**ꜱᴛᴏᴘᴘᴇᴅ**💀💀", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["shiv"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/de` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text   
    await input1.delete(True)
    if raw_text0 == '/de':
        b_name = file_name  
    else: 
        b_name = raw_text0   
    

    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 🌱144\n┣⪼ 🪴240\n┣⪼ 🌿360\n┣⪼ 🌳480\n┣⪼ 🌴720\n┣⪼ 🎄1080\n╰━━⌈⚡[𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀]⚡⌋━━➣ **")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nNow Enter A Caption to add caption on your uploaded file\n\n>>OR Send `de` for use default\n-═════━‧₊˚❀༉‧₊˚.━═════-**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'de':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `https://graph.org/file/6b3baeaf82f7eee52e7f9-b7a6b2c5d5c13bf1c0.jpg`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcwOTYwODIsIm9yZ0lkIjozNTExODAsInR5cGUiOjEsIm1vYmlsZSI6IjkxODAwNDQ1ODkwNCIsIm5hbWUiOiJzdWppdCB0aXdhcmkiLCJlbWFpbCI6InN1aml0dGl3YXJpMjIxMzA4QGdtYWlsLmM5bSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiYnZqaGkiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMmIzMDFjMzRiODkxZmJhMmE1Y2YyYjYyNDA3NjVhNDIiLCJpYXQiOjE3MjQzMzEwNzcsImV4cCI6MTcyNDkzNTg3N30.0oi58SRgPcKtA-vSoYFBiBh2_dIsGnFnlTak1oaxXZZtAzpEo1omoE5zoc4cim9U'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': tokencp}).json()['url']
            
            elif 'media-cdn.classplusapp.com' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcwOTYwODIsIm9yZ0lkIjozNTExODAsInR5cGUiOjEsIm1vYmlsZSI6IjkxODAwNDQ1ODkwNCIsIm5hbWUiOiJzdWppdCB0aXdhcmkiLCJlbWFpbCI6InN1aml0dGl3YXJpMjIxMzA4QGdtYWlsLmM5bSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiYnZqaGkiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMmIzMDFjMzRiODkxZmJhMmE1Y2YyYjYyNDA3NjVhNDIiLCJpYXQiOjE3MjQzMzEwNzcsImV4cCI6MTcyNDkzNTg3N30.0oi58SRgPcKtA-vSoYFBiBh2_dIsGnFnlTak1oaxXZZtAzpEo1omoE5zoc4cim9U'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': tokencp}).json()['url']
            
            
            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                
                
            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MzQ3NTIzMTcsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiTnpoSmIyeEtjRmw0WldOblltcHRPUzl6ZG1Kdlp6MDkiLCJmaXJzdF9uYW1lIjoiU0VsTllVSXJaR1pOZFhBMFpWaDJhbkZ6Y1ZaVFFUMDkiLCJlbWFpbCI6IkwzSkRkR2wxV0c5aEsyWldkSFZVY3pFMWEwVnVVa0owZGxWSWNXeHNRVnB5UjBZNE5FbHdPWEJhVVQwPSIsInBob25lIjoiVjFoaVUzQXlRVWxrWmpCYWVVdGpRMWwzZDJkcFVUMDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJNSE5STjBGaWVVZE1aRmREYTBwWWRXbHhSazh6UVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiWGlhb21pIE0yMDA3SjIwQ0kiLCJyZW1vdGVfYWRkciI6IjMuODQuMTQuMiJ9fQ.bxswfOhz0oDmhcu_W2ojVQ6NcCjmWGDCeZoahsCDnfwfalrmT1rONogeFaLg6Sh7BK-oSxOZXxalYOwEFfs2UlFxsLWjUYD4MdOwIl03HRnW4dY9cQ4uw5_9tVJj4IPZunXid_c-SiFZXlUKmb_fnfjpIAnCpu4ZhlMkG_YmbMU0w93zgUc5PYsnSEu3WP2cMFaRJSMDlsPDxAy5UWdQdBpP7FmVflcIgedptt0JKR8zqvUlNAxBFer4iFX_LABkMNitAoq72bp17Nb3V9DAvNt8ZVigZQmfis_3yFnOTsP9zEvxAsI8HoU1v-zQ6IXT36_1TMCntQg9G7YmORDT5g'
                url = url.split("bcov_auth")[0]+bcov

            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
              id = url.split("/")[3]
              url = "https://madxpw.onrender.com/" + id + "/master.m3u8?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzU1NzkzMDcuMzMzLCJkYXRhIjp7Il9pZCI6IjYzNTE4YzkyOWIwNjg3MDAxOGIyMGM4NCIsInVzZXJuYW1lIjoiNzM4MDgzODQ5MSIsImZpcnN0TmFtZSI6IktyYXRpayIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoia3JhdGlrNDM3QGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTczNDk3NDUwN30.EcclpscuE5LwK_F71MHSS01YaPbX5xTqgEoHFjnjrOc"
            
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "/master.mpd" in url :
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/","https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                
            if "/master.mpd" in url:
                cmd= f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'[🎥]**Vid_id  »** {str(count).zfill(3)}\n**Tɪᴛᴛʟᴇ  »** {name1} {res} «﹝𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀﹞».mkv\n**Bᴀᴛᴄʜ Nᴀᴍᴇ »** {b_name}\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                cc1 = f'[📕]**Pdf_id {str(count).zfill(3)}\n**Tɪᴛᴛʟᴇ »** {name1} «﹝𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀﹞».pdf \n**Bᴀᴛᴄʜ Nᴀᴍᴇ »** {b_name}\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                   f"**downloading failed 🔰『«﹝𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀﹞»』🔰**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝙳𝙾𝙽𝙴 𝙹𝙰𝙽𝙴𝙼𝙰𝙽😎\n\nBY: 𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀\n\nHO GYA BE YE AUR KUCH HAI?💀\nBY @LP_LUCIFER**")


print("ALL LECTURES DOWLOADED SUCCESFULLY.🤗\nBY @LP_LUCIFER")
print("CHLTA HU BYE😎")
bot.run()
