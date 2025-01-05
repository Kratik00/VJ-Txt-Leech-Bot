import os
import re
import sys
import json
import m3u8
import time
import asyncio
import requests
import subprocess
import helper
import random
import zipfile
from helper import get_drm_keys
from pyrogram.types.messages_and_media import message
import tgcrypto
import pyrogram
from pyrogram.types import User, Message
from bot import botStartTime
import shutil, psutil
from subprocess import getstatusoutput
import logging

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters 
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)
auth_users = [7376514183,7372337682,5398544600]
sudo_users = auth_users
sudo_groups = [-1002422521925]

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Devloper",
                url="https://t.me/LP_LUCIFER",
            ),
            InlineKeyboardButton(
                text="Repo",
                url="https://github.com/",
            ),
        ],
    ]
)

@bot.on_message(filters.command(["jaishreeram"]))    
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text("**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫  👋!\n\n➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 CHUTIYAPA\n➠ Can Extract Videos & Pdf Form Your Text File and Upload to Telegram\n\n➠ 𝐔𝐬𝐞 [BHAG JA NALLE] 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞\n\n➠Type /pro /top /adda for more proceedings\n\n➠𝐌𝐚𝐝𝐞 𝐁𝐲: @LP_LUCIFER **\n")
    
@bot.on_message(filters.command("ruko"))
async def restart_handler(_, m):
    await m.reply_text("🚦🛑**ꜱᴛᴏᴘᴘᴇᴅ**🛑🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["shiv"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('*➠ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐀 𝐏𝐫𝐨𝐩𝐞𝐫 𝐖𝐚𝐲 \n\n➠ TXT FORMAT : LINK : URL \n➠ 𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲:  @LP_LUCIFER*')
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
    
   
    await editable.edit(f"*Total links found are : {len(links)}\n┠ Send From where you want to download initial is  : `1` \n┃\n┠ Send `stop` If don't want to Contine \n┖ Bot By : @LP_LUCIFER*")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send /de for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text   
    await input1.delete(True)
    if raw_text0 == 'de':
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
    
    

    await editable.edit("**Now Enter A Caption to add caption on your uploaded file\n\n>>OR Send `de` for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'de':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("🖼 Thumbnail \n\n• Custom Thumbnail : Send me link :- https://graph.org/file/84504a34a8c386fcb0a27.jpg \n• If you don't want Send :  `no` ")
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

@bot.on_message(filters.command(["pro"]))
async def account_login(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**Nikal Lowde**", quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I am Lucifer Downloader Bot**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            cook, url = requests.get(
                f"https://api.telegramadmin.ga/gurukul/link={link}").json().values()

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}'
            if "youtu" in url:
                cmd = f'yt-dlp -f best "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝙳𝙾𝙽𝙴 𝙹𝙰𝙽𝙴𝙼𝙰𝙽😎\n\nBY: 𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀\n\nHO GYA BE YE AUR KUCH HAI?💀\nBY @LP_LUCIFER**")

@bot.on_message(filters.command(["top"]))
async def account_login(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**BHAG BHOSADI KE**", quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I am top Downloader Bot by LUCIFER💀**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}"
       ,reply_markup=keyboard)
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
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text(f"**Copy Paste the App Name of which you want to download videos.**\n\n`vikramjeet`\n\n`sure60`\n\n`theoptimistclasses`")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    editable2 = await m.reply_text("**Enter Title**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text    
    

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://graph.org/file/6b3baeaf82f7eee52e7f9-b7a6b2c5d5c13bf1c0.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)        
           
    try:
        for i in range(arg, len(links)):
        
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace(":","").replace("*","").replace(".","").strip()
                # await m.reply_text(name +":"+ url)

            # Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
            # prog = await m.reply_text(Show)
            # cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}'


            if raw_text0 in "vikramjeet" :
                
                y= url.replace("/", "%2F")
#                 rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Flivehttporigin%2F{y[56:-14]}%2Fmaster.m3u8"
                rout =f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2F{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            elif raw_text0 in "sure60":
                y1= url.replace("/", "%2F")
#                 rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Flivehttporigin%2F{y[49:-14]}%2Fmaster.m3u8"
                rout =f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2F{y1[32:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"            
            elif raw_text0 in "theoptimistclasses":
                y= url.replace("/", "%2F")
                rout=f"https://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2F{y[44:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')              
                cook = "cookie.txt"
                
            name = f'{str(count).zfill(3)}) {name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n**rout** :- `{rout}`"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mp4\n**Caption »** {raw_text5}\n**Index »** {str(count).zfill(3)}'
            
            cmd = f'yt-dlp -o "{name}.mp4" --cookies {cook} "{url}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()

                await m.reply_video(f"{name}.mp4",supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count+=1
                os.remove(f"{name}.mp4")

                os.remove(f"{filename}.jpg")
                os.remove(cook)
                await reply.delete (True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n**rout** :- `{rout}`")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝙳𝙾𝙽𝙴 𝙹𝙰𝙽𝙴𝙼𝙰𝙽😎\n\nBY: 𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀\n\nHO GYA BE YE AUR KUCH HAI?💀\nBY @LP_LUCIFER**")

@bot.on_message(filters.command(["adda"]))
async def account_login(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**bhag bhosadi ke**", quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I am adda pdf Downloader Bot by LUCIFER💀**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** :Pyrogram\n\nSend **TXT** File {Name : Link}"
       ,reply_markup=keyboard)
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
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace(
                "+",
                "").replace("#", "").replace("|", "").replace("@", "").replace(
                    ":", "").replace("*", "").replace(".", "").replace(
                        "'", "").replace('"', '').strip()
            name = f'{str(count).zfill(3)} {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'
            try:
                getstatusoutput(
                    f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"'
                )
                await m.reply_document(f"{name}.pdf", caption=cc)
                count += 1
                await prog.delete(True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(
                    f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["stats","status"]))
async def stats(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    currentTime = readable_time((time.time() - botStartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Down:</b> {recv}\n\n' \
            f'<b>CPU:</b> {cpuUsage}% ' \
            f'<b>RAM:</b> {memory}% ' \
            f'<b>Disk:</b> {disk}%'
    await update.reply_text(botstats)


@bot.on_message(filters.command(["cw"]))
async def start(bot, update):
       await update.reply_text("Hi i am **Careerwill Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/login** to continue..\n\n"
                                     "Bot made by **@LP_LUCIFER**" )

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = (
    f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
)
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

url="https://elearn.crwilladmin.com/api/v1/"

info= {
 "deviceType":"android",
    "password":"",
    "deviceModel":"Asus ASUS_X00TD",
    "deviceVersion":"Pie(Android 9.0)",
    "email":"",
}

@bot.on_message(filters.command(["login"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**"
    )

    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)

    login_response=requests.post(url+"login-other",info)
    token=login_response.json( )["data"]["token"]
    await editable.edit("**login Successful**")
    #await editable.edit(f"You have these Batches :-\n{raw_text}")
    
    url1 = requests.get("https://elearn.crwilladmin.com/api/v1/comp/my-batch?&token="+token)
    b_data = url1.json()['data']['batchData']

    cool=""
    for data in b_data:
        FFF="**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa =f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
        #aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}')>4096:
            await m.reply_text(aa)
            cool =""
        cool+=aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')

    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

# topic id url = https://elearn.crwilladmin.com/api/v1/comp/batch-topic/881?type=class&token=d76fce74c161a264cf66b972fd0bc820992fe576
    url2 = requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-topic/"+raw_text2+"?type=class&token="+token)
    topicid = url2.json()["data"]["batch_topic"]
    bn =url2.json()["data"]["batch_detail"]["name"]
#     await m.reply_text(f'Batch details of **{bn}** are :')
    vj=""
    for data in topicid:
        tids = (data["id"])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
        
    
    
    vp = ""
    for data in topicid:
        tn = (data["topicName"])
        tns=f"{tn}&"
        if len(f"{vp}{tn}")>4096:
            await m.reply_text(tns)
            vp=""
        vp+=tns
        
    cool1 = ""    
    for data in topicid:
        t_name=(data["topicName"])
        tid = (data["id"])
        
        urlx = "https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+tid+"&token="+token
        ffx = requests.get(urlx)
        vcx =ffx.json()["data"]["class_list"]["batchDescription"]
        vvx =ffx.json()["data"]["class_list"]["classes"]
        vvx.reverse()
        zz= len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"
        
#         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"
        
        if len(f'{cool1}{hh}')>4096:
            await m.reply_text(hh)
            cool1=""
        cool1+=hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
#     await m.reply_text(f'**{vcx}**')
#     await m.reply_text(f'```{vj}```')

    editable3= await m.reply_text("**Now send the Resolution**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text

    editable4= await m.reply_text("Now send the **Thumb url** Eg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text


    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    
    editable2= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    
#     editable9= await m.reply_text(f"Now send the **Topic Names**\n\nSend like this **1&2&3&4** and so on\nor copy paste or edit **below names according to you in Order of ids you entered above** :\n\n**Enter this to download full batch :-**\n```{vp}```")
    
#     input9 = message = await bot.listen(editable.chat.id)
#     raw_text9 = input9.text
  
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]
        
        
            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            
            url3 = "https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token   
            ff = requests.get(url3)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff.json()["data"]["class_list"]["batchName"]
            
            vv =ff.json()["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
#                     lessonName = re.sub('\|', '_', cf)
                    
                
                
                    if bcvid.startswith("62"):
                        try:
                            video_response = requests.get(f"{bc_url}/{bcvid}", headers=bc_hdr)
                            video = video_response.json()
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)

                            surl=requests.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token)
                            stoken = surl.json()["data"]["token"]
                            #print(stoken)

                            link = video_url+"&bcov_auth="+stoken
                            #print(link)
                        except Exception as e:
                            print(str(e))
                        
                    else:
                        link="https://www.youtube.com/embed/"+bcvid
                    # await m.reply_text(link)

                    #editable3= await m.reply_text("**Now send the Resolution**")
                    #input4 = message = await bot.listen(editable.chat.id)
                    #raw_text4 = input4.text

                    cc = f"**{count}) Title :** {lessonName}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}"
                    Show = f"**Downloading:-**\n**Title -** ```{lessonName}\n\nQuality - {raw_text4}```\n\n**Url :-** ```{link}```"
                    prog = await m.reply_text(Show)

                    if "youtu" in link:
                        if raw_text4 in ["144", "240", "480"]:
                            ytf = f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]'
                        elif raw_text4 == "360":
                            ytf = 18
                        elif raw_text4 == "720":
                            ytf = 22
                        else:
                            ytf = 18
                    else:
                        ytf=f"bestvideo[height<={raw_text4}]"
                        
                    if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}" "{link}"'
                    else:
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'


                    #cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
                    try:
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd)
                        

                        filename = f"{lessonName}.mp4"
#                         await prog.delete (True)
#                         reply = await m.reply_text("Uploading Video")
                        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:19 -vframes 1 "{filename}.jpg"', shell=True)
    
                        #thumbnail = f"{filename}.jpg"
                        await prog.delete (True)
                        reply = await m.reply_text("Uploading Video")
                        

                        try:
                            if thumb == "no":
                                thumbnail = f"{filename}.jpg"
                            else:
                                thumbnail = thumb
                        except Exception as e:
                            await m.reply_text(str(e))



                        dur = int(helper.duration(filename))
#                         await prog.delete (True)
                        start_time = time.time()
                        await m.reply_video(f"{lessonName}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{lessonName}.mp4")
                        
                        os.remove(f"{filename}.jpg")
                        await reply.delete (True)
                    except Exception as e:
                        await m.reply_text(f"**Video downloading failed ❌**\n{str(e)}\n\n**Url :-** ```{link}```")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")
    
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            url5=requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token)
            k=url5.json()["data"]["notesDetails"]
            bb = len(url5.json()["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                 
                    
                    ww = f"**{count1}) File Name :- **{name}\n**Date : **{xi}\n{bn}"
                    show2 = f'**Downloading :-**\n\n**Link :** ```{s}```'
                    prog2 = await m.reply_text(show2)
                    cmd2=f'yt-dlp -o "{name}.pdf" "{s}"'
                    try:
                        download_cmd2 = f"{cmd2} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd2)
                        await m.reply_document(f'{name}.pdf', caption=ww)

                        count1+=1
                        await prog2.delete (True)
                        os.remove(f'{name}.pdf')
                        time.sleep(2)
                        
                    except Exception as e:
                        await m.reply_text(f"**PDF downloading failed ❌**\n{str(e)}")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")

bot.run()
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝙳𝙾𝙽𝙴 𝙹𝙰𝙽𝙴𝙼𝙰𝙽😎\n\nBY: 𝙇𝙐𝘾𝙄𝙁𝙀𝙍💀\n\nHO GYA BE YE AUR KUCH HAI?💀\nBY @LP_LUCIFER**")


print("ALL LECTURES DOWLOADED SUCCESFULLY.🤗\nBY @LP_LUCIFER")
print("CHLTA HU BYE😎")
bot.run()
