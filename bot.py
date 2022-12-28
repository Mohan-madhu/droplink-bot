# DO NOT REMOVE CREDITS
# Copyright (c) 2021 dakshy/droplink-bot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = "17473920"
API_HASH = "e69dbca72db91d1f4e9a5d46508202e9"
BOT_TOKEN = "5545000937:AAG4mUaYKjJw3Vd3Q4hX1eYV2xtsLSXNzfQ"
API_KEY = "e34f8597fe26034bf77a3878242c0b1c62b2ec49"

bot = Client('tnlink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)
          


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm a specialised bot for shortening Tnlink links which can help you earn money by just sharing links. Made by <a href=\"https://github.com/dakshy\">ToonsHub</a>.")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        await message.reply(f' `{short_link}`', quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://tnlink.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
