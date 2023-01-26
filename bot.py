from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', '71d5948e599ac45557a9ea0da696d2a7470e5ab1')

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
    links1 = message.text
    links2 = "https://url.mysteryfacts.xyz/st?api=b6bc7bf0a57506f205a4ae8a04694ce5de1501d1&url=" + links1
    substr = "https://t.me/mvtmoviesearcherbot?start"
    if substr in links1 : 
      links = links1.split("\n")
    else : 
      links = links2.split("\n")
    
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
