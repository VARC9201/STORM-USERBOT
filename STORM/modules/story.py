from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["lovestory"], ["."]))
async def hearts(client: Client, message: Message):
    await message.edit("ʟᴇᴛ ᴍᴇ ᴛᴇʟʟ ʏᴏᴜ ᴀ ʟᴏᴠᴇ ꜱᴛᴏʀʏ 🥳")
    await asyncio.sleep(0.5)
    await message.edit("1 ❤️ ʟᴏᴠᴇ ꜱᴛᴏʀʏ")
    await asyncio.sleep(0.5)
    await message.edit("  😐             😕 \n/👕\         <👗\ \n 👖               /|")
    await asyncio.sleep(0.5)
    await message.edit("  😉          😳 \n/👕\       /👗\ \n  👖            /|")
    await asyncio.sleep(0.5)
    await message.edit("  😚            😒 \n/👕\         <👗> \n  👖             /|")
    await asyncio.sleep(0.5)
    await message.edit("  😍         ☺️ \n/👕\      /👗\ \n  👖          /|")
    await asyncio.sleep(0.5)
    await message.edit("  😍          😍 \n/👕\       /👗\ \n  👖           /|")
    await asyncio.sleep(0.5)
    await message.edit("  😘   😊 \n /👕\/👗\ \n   👖   /|")
    await asyncio.sleep(0.5)
    await message.edit(" 😳  😁 \n /|\ /👙\ \n /     / |")
    await asyncio.sleep(0.5)
    await message.edit("😈    /😰\ \n<|\      👙 \n /🍆    / |")
    await asyncio.sleep(0.5)
    await message.edit("😅 \n/(),✊😮 \n /\         _/\\/|")
    await asyncio.sleep(0.5)
    await message.edit("😎 \n/\\_,__😫 \n  //    //       \\")
    await asyncio.sleep(0.5)
    await message.edit("😖 \n/\\_,💦_😋  \n  //         //        \\")
    await asyncio.sleep(0.5)
    await message.edit("  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ")
    await asyncio.sleep(0.5)
    await message.edit("ᴛʜᴇ ᴇɴᴅ 😂.......")
