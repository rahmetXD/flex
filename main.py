import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import time
import random
from telethon.tl import types
from telethon import Button
import asyncio
import ping3
from urllib.parse import quote

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

ozel_list = [1948748468]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    await event.reply("❤️ Merhaba Ben **Lais User Tagger**\n🏷 Gruplarda Kullanıcıları Etiketlemek İçin Tasarlandım. Butonları Kullanarak Botu Yönetebilirsin.",
                    buttons=(
                        [
                            Button.inline("📚 Komutlar", data="help"),
                        ],
                        [
                            Button.url('📮 Beni Gruba Ekle', f"https://t.me/{bot_username}?startgroup=a")
                        ],
                        [
                            Button.url('👨🏻‍💻 Developers', 'https://t.me/lusttqw'),
                            Button.url('📣 Channel', 'https://t.me/laisbots')
                        ]
                    ),
                    link_preview=False
                   )


@client.on(events.callbackquery.CallbackQuery(data="etiket"))
async def help(event):
    await event.edit(f"📮 Etiket Komutları:\n\n🕹 Komut: `/tag` \n📱Kullanım: `/tag (Yazı)` \n📄Açıklama: Üyeleri 5'li Şekilde Etiketlemek İçindir.\n\n🕹 Komut: `/tektag` \n📱Kullanım: `/tektag (Yazı)` \n📄Açıklama: Üyeleri Tekli Şekilde Etiketlemek İçindir.\n\n🕹 Komut: `/gecetag` \n📱Kullanım: `/gecetag` \n📄Açıklama: Üyeleri İyi Geceler Mesajıyla Etiketlemek İçindir.\n\n🕹 Komut: `/guntag` \n📱Kullanım: `/guntag` \n📄Açıklama: Üyeleri Günaydın Mesajı İle Etiketlemek İçindir.\n\n🕹 Komut: `/rtag` \n📱Kullanım: `/rtag` \n📄Açıklama: Üyeleri Random Sorularla Etiketlemek İçindir.\n\n🕹 Komut: `/ntag` \n📱Kullanım: `/ntag` \n📄Açıklama: Üyeleri Soru Sorarak Chete Çağırması İçindir.\n\n🕹 Komut: `/etag` \n📱Kullanım: `/etag (Yazı)` \n📄Açıklama: Üyeleri Emojili  Şekilde Etiketlemek İçindir.\n\n🕹 Komut: `/btag` \n📱Kullanım: `/btag (Yazı)` \n📄Açıklama: Üyeleri Bayrak Emojili Şekilde Etiketlemek İçindir.\n\n🕹 Komut: `/atag` \n📱Kullanım: `/atag` \n📄Açıklama: Gruptaki Yetkili Üyeleri 5 Saniye Arayla Etiketlemek İçin Kullanılır.\n\n🕹 Komut: `/cancel` \n📱Kullanım: `/cancel` \n📄Açıklama: Aktif Olan Etiketleme İşlemini Durdurmak İçin Kullanılır.", buttons=(

                   
                  [
                   Button.inline("➡️ ɢᴇʀɪ", data="start")
                    ]
                 ),
               link_preview=False)   

@client.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit(f"🕹 Komutlar\n\n`Bota Bulunan Komutlar.`", buttons=(

                   
                  [
                        [Button.inline("📮 Etiket Komutları", data="etiket")],               
                        [Button.inline("⚙️ Ek Komutlar", data="ek")],               
                    ]
                 ),
               link_preview=False)   

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def help(event):
    await event.edit(f"❤️ Merhaba Ben **Lais User Tagger**\n🏷 Gruplarda Kullanıcıları Etiketlemek İçin Tasarlandım. Butonları Kullanarak Botu Yönetebilirsin.", buttons=(                  
		       
                       [Button.inline("📚 Komutlar", data="help")],               
                      [Button.url('📮 Beni Gruba Ekle', f"https://t.me/{bot_username}?startgroup=a")],
		                  [Button.url(' 👨🏻‍💻 Developers', 'https://t.me/lusttqw')],
		                  [Button.url('📣 Channel', 'https://t.me/laisbots')],

                    ),
                    link_preview=False
                   )

@client.on(events.callbackquery.CallbackQuery(data="ek"))
async def help(event):
    await event.edit(f"⚙️ Ek Komutlar:\n\n🕹 Komut: `/slap` \n📄Açıklama: Gruptaki Yanıt Verilen Bir Üyeyi Trollemek İçin Kullanılır.\n\n🕹 Komut: `/bots` \n📄Açıklama: Botun Bulunduğu Gruptaki Botları Gösterir.\n\n🕹 Komut: `/grup` \n📄Açıklama: Grup Bilgilerini Gösterir.\n\n🕹 Komut: `/reload` \n📄Açıklama: Bot Anlamsızca Hata Veya Komutlara Cevap Vermese Botu Yeniler.\n\n🕹 Komut: `/id` \n📄Açıklama: İd Öğrenmenize Yardım Eder.\n\n🕹 Komut: `/arama` \n📄Açıklama: Google Üzerinden Arama Yapabilirsin (/arama Zeus-Pro).\n\n🕹 Komut: `/ping` \n📄Açıklama: Botun Bağlı Olduğu VPS'in Pingini Ölçün.\n\n🕹 Komut: `/eros` \n📄Açıklama: Gruptaki Herhangibi 2 Kişiyi Shipleyin.", buttons=(
                   
                  [
                        [Button.inline("➡️ ɢᴇʀɪ", data="start")],               
                    ]
                 ),
               link_preview=False)   

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"❌**Etiket işlemi durduruldu.\n\n Etiketlerin Sayı👤: {rxyzdev_tagTot[event.chat_id]}**")


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩  🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Geçmiş Mesajları Etiketleyemem.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  else:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)	

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Geçmiş Mesajları Etiketleyemem.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiketleme İşlemi İçin  Bir Mesaj Belirt!")
  else:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Geçmiş Mesajları Etiketleyemem.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etikete Başlamam İçin Bir Mesaj Yazmalısın!")
  else:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➜ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➜ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir. ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Geçmiş Mesajları Etiketleyemem.*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  else:
    return await event.respond("Etiketleme İşlemine Başlamam İçin Bir Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**➜ [{usr.first_name}](tg://user?id={usr.id})**"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➜ [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(2)
	

@client.on(events.NewMessage(pattern='/slap'))
async def slap(event):
    if event.is_private:
        return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = user.first_name
            slap_phrases = [
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'nin üstüne benzin döktü!",
                f"{user_name}'yi ateşe attı!",
                f"{user_name}'nin üstüne su döktü!",
                f"{user_name}'yi dondurdu!",
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'yi Zencilere Sattı!",
                f"{user_name}'yi Turşu Kavonozuna Soktu!",
                f"{user_name}'nin Üzerine Buz Dolabı Attı!",
                f"{user_name}'nin Kafasını Duvara Sürterek Yaktı!",
                f"{user_name}'yi Ormana Kaçırdı!",
                f"{user_name}'yi Banyoda Sukast Etti!",
            ]
            slap_phrase = random.choice(slap_phrases)
            await event.respond(f"{event.sender.first_name} {slap_phrase}")
        else:
            await event.respond("Üzgünüm, kullanıcıyı bulamıyorum!")
    else:
        await event.respond("Bu komutu kullanabilmek için bir mesaja yanıt vermelisiniz!")

@client.on(events.NewMessage(pattern='/grup'))
async def grup_info(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir!")
        return

    user = await event.get_sender()
    user_first_name = user.first_name

    # İlk yanıtı gönder
    response_text = f'Hey! {user_first_name}, Bilgiler Geliyor Bekle!'
    response = await event.respond(response_text)

    # Bekleme süresi (5 saniye)
    await asyncio.sleep(5)

    # İlk yanıtı sil
    await response.delete()

    # Grup bilgilerini gönder
    chat = await event.get_chat()
    group_name = chat.title
    group_id = chat.id

    # Grup bilgilerini al
    chat_info = await event.client.get_entity(group_id)

    # Diğer bilgileri al
    deleted_count = 0
    active_count = 0
    bot_count = 0
    total_count = 0

    # Katılmış üyelerin listesini al
    async for participant in event.client.iter_participants(chat_info):
        total_count += 1
        if participant.deleted:
            deleted_count += 1
        elif not participant.bot:
            active_count += 1
        elif participant.bot:
            bot_count += 1

    # Özel durumları kontrol et
    special_status = ""
    if deleted_count > 0:
        special_status += f'→ Delete Hesap: {deleted_count}\n'
    if bot_count > 0:
        special_status += f'→ Bot Sayısı: {bot_count}\n'

    # Özel durumlar olmadığında "Bulunamadı" mesajı ver
    if not special_status:
        special_status = "Bulunamadı"

    # Owner'ın kullanıcı adını belirtin
    owner_username = "owner"  # Değiştirin

    # Owner butonunu oluşturun
    owner_button = Button.url('🛡ᴏᴡɴᴇʀ🛡', f"https://t.me/{owner}")

    response_text = (
        f'→ Grup Adı: {group_name}\n'
        f'→ Grup ID: {group_id}\n'
        f'→ Aktif Kullanıcıları: {active_count}\n'
        f'→ Grup Üye Sayısı: {total_count}\n'
        f'{special_status}'
    )

    # Bilgileri yanıt olarak gönder ve Owner butonunu ekleyin
    await event.respond(response_text, buttons=[[owner_button]])

@client.on(events.NewMessage(pattern="^/bots$"))
async def list_bots(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir!")
        return

    # "Bir saniye bekleyin..." mesajını gönder
    message = await event.respond("🔁 Hazırlanıyor...")

    # 3 saniye bekle
    await asyncio.sleep(3)

    # "Bir saniye bekleyin..." mesajını sil
    await message.delete()

    # Grup veya kanal katılımcılarını al
    users = await client.get_participants(event.chat_id, limit=200)

    bot_list = []
    for user in users:
        if user.bot:
            bot_list.append(user)

    # Bot listesini oluştur ve gönder
    if bot_list:
        bot_names = "\n".join([f"➻ @{user.username}" for user in bot_list])
        await event.respond(f"🤖 Gruptaki Botlar Şunlar:\n\n{bot_names}")
    else:
        await event.respond("🤖 Bu Grupta Hiç Bot Bulamadım!")

@client.on(events.NewMessage(pattern="^/id"))
async def get_id(event):
    # Kullanıcının kendi ID'sini ve grup ID'sini al
    user_id = event.sender_id
    chat_id = event.chat_id

    if event.is_private:
        # Kişiye özel sohbetse
        await event.respond(f"Senin ID'n: `{user_id}`\nGrup ID'si: `{chat_id}`")
    elif event.is_group or event.is_channel:
        if event.reply_to_msg_id:
            # Bir kişinin mesajına yanıt verilmişse
            reply_message = await event.get_reply_message()
            replied_user_id = reply_message.sender_id

            await event.respond(
                f"├Kullanıcı ID'si: `{user_id}`\n"
                f"├Yanıt Verilen Kullanıcı ID'si: `{replied_user_id}`\n"
                f"├Grup ID'si: `{chat_id}`"
            )
        else:
            # Sadece grup veya kanal sohbeti
            await event.respond(f"Senin ID'n: `{user_id}`")

import subprocess

@client.on(events.NewMessage(pattern="^/reload$"))
async def reload_vps(event):
    try:
        # Mesajı gönder
        reload_message = await event.respond("VPS Yenileniyor... ⏳ Bu birkaç saniye sürebilir.")

        # 10 saniye bekleyin
        await asyncio.sleep(10)

        # Mesajı güncelle
        await reload_message.edit("VPS Yenilendi! ✅")
    except Exception as e:
        # Hata durumunda mesaj gönder
        await event.respond(f"Hata oluştu: {str(e)}")

@client.on(events.NewMessage(pattern='/alive'))
async def handler(event):
    # Alive Bot Durumunu Kontrol Etme Yalnızca Adminler İçin !
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("Sen Benim Efendim Değilsin!")
    await event.reply('efendim, Sorunsuz Şekilde Aktifim. Teşşekürler!')
	
@client.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    # Bot Stats 
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("**Sen sudo değilsin. Botun Statiklerini Öğrenemezsin!")
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**{bot_username} İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern="^/ping$"))
async def ping_pong(event):
    try:
        vps_address = "213.142.157.170"  # VPS'in IP adresini veya alan adını buraya ekleyin

        # Komutu kullanan kişiye "Ölçülüyor..." mesajı gönder
        measuring_msg = await event.respond("Ölçülüyor... ⏳")

        # 5 saniye bekle
        await asyncio.sleep(5)

        # Ping değerini ölç
        ping_result = ping3.ping(vps_address)

        # Ölçüm sonucunu güncelle ve kullanıcıya gönder
        await measuring_msg.edit(f"🏓 Ping: {ping_result} ms")
    except Exception as e:
        # Hata durumunda mesaj gönder
        await event.respond(f"Hata oluştu: {str(e)}")

@client.on(events.NewMessage(pattern="^/arama (.+)$"))
async def google_search(event):
    try:
        # Komuttan arama terimini al
        search_query = event.pattern_match.group(1)

        # Google'da arama yap
        search_url = f"https://www.google.com/search?q={quote(search_query)}"
        
        # Sonuç mesajını oluştur
        result_message = f"🔍 Google Arama: {search_query}"

        # Mesajı kullanıcıya gönder ve bağlantıyı ekleyerek link önizlemesini engelle
        await event.respond(result_message, buttons=[Button.url("Tıkla", search_url)], link_preview=False)
    except Exception as e:
        # Hata durumunda mesaj gönder
        await event.respond(f"Hata oluştu: {str(e)}")

@client.on(events.ChatAction)
async def welcome_user(event):
    try:
        if event.user_joined:
            # Yeni katılan kullanıcının ID'sini al
            user_id = event.user_id

            # Belirtilen özel ID'ye sahip bir kullanıcı katıldığında
            if user_id == 5944841427:
                # Yeni katılan kullanıcının adını al
                user = await client.get_entity(user_id)
                user_name = user.first_name if user.first_name else user.username

                # Özel bir karşılama mesajı oluştur
                welcome_message = (
                    f"Merhaba {user_name}! 🌟 Hoşgeldin, İşte Bu Gelen Benim Geliştiricim!\n\n"
                )

                # Mesajı gruba gönder
                await event.respond(welcome_message)
    except Exception as e:
        # Hata durumunda mesaj gönder
        await event.respond(f"Hata oluştu: {str(e)}")


@client.on(events.NewMessage(pattern="^/eros$"))
async def eros_command(event):
    try:
        # Sadece özel mesajlarda veya kanallarda çalışmasına izin ver
        if not (isinstance(event.chat, types.Chat) or isinstance(event.chat, types.Channel)):
            return await event.respond("Bu komut yalnızca gruplarda ve kanallarda çalışır.")

        # Grup üyelerini al
        group_participants = await event.client.get_participants(event.chat_id)

        # Botları ve silinmiş hesapları filtrele
        eligible_users = [user for user in group_participants if not user.bot and not user.deleted]

        # Rasgele iki kullanıcı seç
        selected_users = random.sample(eligible_users, min(len(eligible_users), 2))

        # Kullanıcıları etiketle
        tagged_users = [f"[{user.first_name}](tg://user?id={user.id})" for user in selected_users]

        # Sevgi oranını belirle
        love_percentage = random.randint(1, 100)

        # Mesajı oluştur
        message = (
            "💘 Erosun Oku Atıldı !\n"
            "✦  Gizli Aşıklar :\n\n"
            f"{tagged_users[0]}  💕  {tagged_users[1]}\n\n"
            f"💞 Sevgi Oranı : {love_percentage}%"
        )

        # Mesajı gönder
        await event.respond(message)

    except Exception as e:
        # Hata durumunda mesaj gönder
        await event.respond(f"Hata oluştu: {str(e)}")


# Sorular listesi
sorular = [
    "Hangi konuda yardıma ihtiyacınız var?",
    "En sevdiğiniz film nedir?",
    "Bugün ne yaptınız?",
    "Bir hedefiniz var mı?",
    "En sevdiğiniz renk nedir?",
    "Hangi kitabı okudunuz?",
    "Güzel bir anınızı paylaşabilir misiniz?",
    "En sevdiğiniz yemek nedir?",
    "Hayalinizdeki tatil nereye olurdu?",
    "Son zamanlarda izlediğiniz en iyi dizi/film nedir?",
    "Hangi müzik türünü dinlersiniz?",
    "En sevdiğiniz spor dalı nedir?",
    "Bir hayvan sahibi misiniz?",
    "Hangi ülkeleri ziyaret etmek istersiniz?",
    "En sevdiğiniz meyve nedir?",
    "Bir süper gücünüz olsaydı, ne olmasını isterdiniz?",
    "Hangi tarihi kişiyi tanımak isterdiniz?",
    "En sevdiğiniz içecek nedir?",
    "Bir sanat eseri yaratmak isteseydiniz, konusu ne olurdu?",
    "Hangi sporu yapmaktan hoşlanırsınız?",
    "En sevdiğiniz tatlı nedir?",
    "Bir dil öğrenmek isteseydiniz, hangisi olurdu?",
    "Hangi kıyafet tarzını benimsersiniz?",
    "En sevdiğiniz mevsim nedir?",
    "Bir şehirde yaşamak mı yoksa kırsalda mı yaşamak isterdiniz?",
    "Hangi film karakteriyle tanışmak isterdiniz?",
    "En sevdiğiniz oyun nedir?",
    "Bir konserde hangi sanatçıyı görmek isterdiniz?",
    "Hangi tarihi dönemde yaşamak isterdiniz?",
    "En sevdiğiniz hava durumu nedir?",
    "Bir restoranda sipariş verirken ne tercih edersiniz?",
    "Hangi yemekleri yapmayı sever ve iyi yaparsınız?",
    "En sevdiğiniz renk kombinasyonu nedir?",
    "Bir kahve dükkanında siparişiniz nedir?",
    "Hangi kitabı tekrar tekrar okursunuz?",
    "En sevdiğiniz kış aktivitesi nedir?",
    "Bir konser veya etkinlik için hangi şehre seyahat ederdiniz?",
    "Hangi tarihi olaya şahit olmayı isterdiniz?",
    "En sevdiğiniz çizgi film karakteri kimdir?",
    "Bir günü nasıl geçirmek isterdiniz?",
    "Hangi sanat dalında yetenekli olmak isterdiniz?",
    "En sevdiğiniz korku filmi nedir?",
    "Bir hayvanın dilini konuşabilseydiniz, hangi hayvanla konuşmak isterdiniz?",
    "Hangi tür müzik sizi motive eder?",
    "En sevdiğiniz plaj aktivitesi nedir?",
    "Bir aktör veya aktris ile bir gün geçirme şansınız olsaydı, kim olurdu?",
    "Hangi yemek kültürünü daha yakından tanımak istersiniz?",
    "En sevdiğiniz hobi nedir?",
    "Bir zaman makinesi olsaydı, hangi döneme gitmek isterdiniz?",
    "Hangi doğal güzellikleri görmek istersiniz?",
    "En sevdiğiniz cinsiyet ötesi karakter kimdir?",
    "Bir süper kahraman gücü seçebilseydiniz, hangisini seçerdiniz?",
    "Hangi ünlü kişiyi tanımak isterdiniz?",
    "En sevdiğiniz aktivite nedir?",
    "Bir şehirde bir gün boyunca neler yapmak isterdiniz?",
    "Hangi spor takımını desteklersiniz?",
    "En sevdiğiniz fast food nedir?",
    "Bir enstrüman çalmak isteseydiniz, hangisini çalardınız?",
    "Hangi sanat eseri sizi etkiledi?",
    "En sevdiğiniz manzara nedir?",
    "Bir keşif yapmak için gitmek istediğiniz yer neresi?",
    "Hangi festivale katılmak isterdiniz?",
    "En sevdiğiniz tarih dönemi nedir?",
    "Bir dil bilseniz, hangisi olurdu?",
    "Hangi etkinlik sizi rahatlatır?",
    "En sevdiğiniz şarkı sözü nedir?",
    "Bir hayvanla konuşabilseydiniz, hangisi olurdu?",
    "Hangi sanatçının eserlerini seversiniz?",
    "En sevdiğiniz manzara nedir?",
    "Bir karakterin hayatını yaşayabilseydiniz, kim olurdu?",
    "Hangi hayali gerçekleştirmek istersiniz?",
    "En sevdiğiniz içecek nedir?",
    "Bir tatil destinasyonu seçme şansınız olsaydı, nereye gitmek isterdiniz?",
    "Hangi bilgiye sahip olmak isterdiniz?",
    "En sevdiğiniz kış sporu nedir?",
    "Bir filmi veya diziyi yeniden yazabilseydiniz, hangisi olurdu?"
    # ... diğer sorular ...
]

# Aktif çalışan grupları takip etmek için liste
anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
    global anlik_calisan
    anlik_calisan.remove(event.chat_id)

@client.on(events.NewMessage(pattern="^/rtag"))
async def basla_etiketleme(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")

    anlik_calisan.append(event.chat_id)
    await event.respond("Etiketleme İşlemi Başlatıldı! Biraz bekleyin...")

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
        usrnum += 1
        soru = random.choice(sorular)
        usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}), {soru}\n"
        if event.chat_id not in anlik_calisan:
            await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
            return
        if usrnum == 1:
            await client.send_message(event.chat_id, usrtxt, parse_mode='Markdown')
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

# Günaydın mesajları listesi
gunaydin_mesajlari = [
    "Günaydın! Umarım harika bir gün geçirirsiniz.",
    "Günaydın dostlar! Bugün size güzellikler getirsin.",
    "Günaydın herkese! Yeni bir gün, yeni başlangıçlar demektir.",
    "Sabahın güzelliği üzerinize olsun, günaydın!",
    "Günaydın sevgili arkadaşlar! Bugün sizin için harika bir gün olacak.",
    "Günaydın! Hayalinizdeki başarıya bir adım daha yaklaştığınız bir gün olsun.",
    "Günaydın! Bugünün enerjisi size pozitiflik ve mutluluk getirsin.",
    "Günaydın herkese! Güzel bir gülümsemeyle gününüzü başlatın.",
    "Sabahları güne güzel bir gülümsemeyle başlamak, tüm gününüzü aydınlatabilir.",
    "Günaydın dostlar! Bugünün güzellikleri sizi sarsın.",
    "Günaydın! Yeni başarılar ve mutluluklar sizi bekliyor.",
    "Günaydın! Sevdiklerinizle güzel anlar yaşamanız dileğiyle.",
    "Günaydın! Her anın kıymetini bilin ve keyif alın.",
    "Günaydın! İyi enerjili bir gün geçirmeniz dileğiyle.",
    "Günaydın! Bugün kendinize biraz zaman ayırın ve keyif alın.",
    "Günaydın! Hayatın güzelliklerini keşfetmek için bir gün daha.",
    "Günaydın! Sevdiklerinizle beraber geçireceğiniz güzel bir gün olsun.",
    "Günaydın! Hayatta sizi mutlu eden şeylere odaklanın.",
    "Günaydın dostlar! Güne pozitif enerjiyle başlayın.",
    "Günaydın! Başarılarınızın devam ettiği bir gün olsun.",
    "Günaydın! Bugün küçük mutluluklara odaklanın.",
    "Günaydın herkese! İyi bir gün geçirmeniz dileğiyle.",
    "Günaydın! Sizi motive eden şeylere odaklanın.",
    "Günaydın! Bugünün sizin için güzel geçmesini dilerim.",
    "Günaydın! Kendinize sevgiyle davranın.",
    "Günaydın! Yeni başlangıçlara hazır olun.",
    "Günaydın! Sevdiklerinizle geçireceğiniz keyifli anlar sizi bekliyor.",
    "Günaydın! Bugünün size güzellikler getirmesini dilerim.",
    "Günaydın! Hayatın tadını çıkarın ve minnettar olun.",
    "Günaydın! İyi şeylere odaklanın ve olumlu düşünün.",
    "Günaydın! Bugün sizin için başarılarla dolu olsun.",
    "Günaydın! İyi enerjiyi içselleştirin ve paylaşın.",
    "Günaydın! Bugünü özel kılan şeylere odaklanın.",
    "Günaydın! Yeni fırsatlar ve güzellikler sizleri bekliyor.",
    "Günaydın! İçsel huzurunuzu bulmanız dileğiyle.",
    "Günaydın! Kendinize biraz zaman ayırın ve dinlenin.",
    "Günaydın! Başkalarına gülümseyerek güzel bir gün geçirin.",
    "Günaydın! Bugün sizin için olumlu değişikliklere gebe.",
    "Günaydın! Hayatın küçük zevklerinin tadını çıkarın.",
    "Günaydın! Sevdiklerinizle birlikte geçireceğiniz anların kıymetini bilin.",
    "Günaydın! Hayallerinizin peşinden koşun ve başarılı olun.",
    "Günaydın! Bugün sizin için mutlu bir gün olsun.",
    "Günaydın! Kendinize güvenin ve başarıya odaklanın.",
    "Günaydın! İyi düşüncelerle güne başlayın ve pozitif enerjiyi yayın.",
    "Günaydın! Yeni bir gün, yeni bir başlangıç demektir.",
    "Günaydın! Kendinize sevgiyle bakın ve mutlu olun.",
    "Günaydın! Bugünün size başarılar getirmesini dilerim.",
    "Günaydın! Hayatın sürprizlerini keşfetmek için açık olun.",
    "Günaydın! Sevdiklerinizle birlikte geçireceğiniz anların kıymetini bilin.",
    "Günaydın! İyi düşüncelerle güne başlayın ve pozitif enerjiyi yayın.",
    "Günaydın! Yeni bir gün, yeni bir başlangıç demektir.",
    "Günaydın! Kendinize sevgiyle bakın ve mutlu olun.",
    "Günaydın! Bugünün size başarılar getirmesini dilerim.",
    "Günaydın! Hayatın sürprizlerini keşfetmek için açık olun."
    # ... diğer günaydın mesajları ...
]


# Aktif çalışan grupları takip etmek için liste
anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
    global anlik_calisan
    anlik_calisan.remove(event.chat_id)

@client.on(events.NewMessage(pattern="^/guntag"))
async def gunaydin_etiketleme(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")

    anlik_calisan.append(event.chat_id)
    await event.respond("Guntag İşlemi Başlatıldı! Biraz bekleyin...")

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
        usrnum += 1
        mesaj = random.choice(gunaydin_mesajlari)
        usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}), {mesaj}\n"
        if event.chat_id not in anlik_calisan:
            await event.respond("Guntag İşlemi Başarıyla Durdurulmuştur!")
            return
        if usrnum == 1:
            await client.send_message(event.chat_id, usrtxt, parse_mode='Markdown')
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

# İyi geceler mesajları listesi
iyi_geceler_mesajlari = [
    "İyi geceler! Tatlı rüyalar dilerim.",
    "Güzel bir gecenin ardından sizi bekleyen bir sabah olsun.",
    "İyi geceler dostlar! Huzurlu bir uykuya dalmanız dileğiyle.",
    "Gecenin sihirli atmosferinde huzur bulun. İyi geceler!",
    "Uyumadan önce sevdiklerinizi düşünün ve içsel huzuru bulun.",
    "İyi geceler! Yarın için enerji toplamanız dileğiyle.",
    "Gecenin sessizliğinde huzur bulun. İyi geceler!",
    "Rüyalarınız gerçekleşsin. İyi geceler!",
    "Uykuya dalarken güzel düşüncelerle dolu bir zihinle olun.",
    "Gecenin siyah örtüsü sizi huzurla sarssın. İyi geceler!",
    "İyi geceler! Kalbiniz huzur ve sevgiyle dolsun.",
    "Gecenin huzurunu hissedin ve rahat bir uyku geçirin.",
    "İyi geceler! Yarın için taze bir başlangıç yapmanız dileğiyle.",
    "Gecenin yıldızları sizi koruyacak. İyi geceler!",
    "Uyumadan önce sevdiklerinize iyi dilekler bırakın.",
    "İyi geceler! Güzel rüyalar sizi beklesin.",
    "Gecenin sükuneti içinde huzur bulun. İyi geceler!",
    "Uyumadan önce gününüzü değerlendirin ve minnettar olun.",
    "İyi geceler! Yarının size güzellikler getirmesini dilerim.",
    "Gecenin sessizliğinde ruhunuzu dinlendirin. İyi geceler!",
    "Uykunuzun derin ve huzurlu olması dileğiyle. İyi geceler!",
    "İyi geceler! Geceyi huzurla geçirmeniz dileğiyle.",
    "Gecenin yıldızları size rehberlik etsin. İyi geceler!",
    "Uyumadan önce içsel huzurunuzu bulun. İyi geceler!",
    "İyi geceler! Yarın için enerji toplamanız dileğiyle.",
    "Gecenin huzurunu hissedin ve rahat bir uyku geçirin.",
    "İyi geceler! Kalbiniz huzur ve sevgiyle dolsun.",
    "Gecenin siyah örtüsü sizi huzurla sarssın. İyi geceler!",
    "Rüyalarınız gerçekleşsin. İyi geceler!",
    "Uykuya dalarken güzel düşüncelerle dolu bir zihinle olun.",
    "Gecenin sessizliğinde huzur bulun. İyi geceler!",
    "İyi geceler! Tatlı rüyalar dilerim.",
    "Güzel bir gecenin ardından sizi bekleyen bir sabah olsun.",
    "İyi geceler dostlar! Huzurlu bir uykuya dalmanız dileğiyle.",
    "Gecenin sihirli atmosferinde huzur bulun. İyi geceler!",
    "Uyumadan önce sevdiklerinizi düşünün ve içsel huzuru bulun.",
    "İyi geceler! Yarın için enerji toplamanız dileğiyle.",
    "Gecenin sessizliğinde huzur bulun. İyi geceler!",
    "Rüyalarınız gerçekleşsin. İyi geceler!",
    "Uykuya dalarken güzel düşüncelerle dolu bir zihinle olun.",
    "Gecenin siyah örtüsü sizi huzurla sarssın. İyi geceler!",
    "İyi geceler! Kalbiniz huzur ve sevgiyle dolsun.",
    "Gecenin huzurunu hissedin ve rahat bir uyku geçirin.",
    "İyi geceler! Yarın için taze bir başlangıç yapmanız dileğiyle.",
    "Gecenin yıldızları sizi koruyacak. İyi geceler!",
    "Uyumadan önce sevdiklerinize iyi dilekler bırakın.",
    "İyi geceler! Güzel rüyalar sizi beklesin.",
    "Gecenin sessizliğinde ruhunuzu dinlendirin. İyi geceler!",
    "Uykunuzun derin ve huzurlu olması dileğiyle. İyi geceler!",
    "İyi geceler! Geceyi huzurla geçirmeniz dileğiyle.",
    "Gecenin yıldızları size rehberlik etsin. İyi geceler!",
    "Uyumadan önce içsel huzurunuzu bulun. İyi geceler!",
    "İyi geceler! Yarın için enerji toplamanız dileğiyle.",
    "Gecenin huzurunu hissedin ve rahat bir uyku geçirin.",
    "İyi geceler! Kalbiniz huzur ve sevgiyle dolsun.",
    "Gecenin siyah örtüsü sizi huzurla sarssın. İyi geceler!",
    "Rüyalarınız gerçekleşsin. İyi geceler!",
    "Uykuya dalarken güzel düşüncelerle dolu bir zihinle olun.",
    "Gecenin sessizliğinde huzur bulun. İyi geceler!",
]


# Aktif çalışan grupları takip etmek için liste
anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
    global anlik_calisan
    anlik_calisan.remove(event.chat_id)

@client.on(events.NewMessage(pattern="^/gecetag"))
async def gunaydin_etiketleme(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")

    anlik_calisan.append(event.chat_id)
    await event.respond("Guntag İşlemi Başlatıldı! Biraz bekleyin...")

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
        usrnum += 1
        mesaj = random.choice(iyi_geceler_mesajlari)
        usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}), {mesaj}\n"
        if event.chat_id not in anlik_calisan:
            await event.respond("Guntag İşlemi Başarıyla Durdurulmuştur!")
            return
        if usrnum == 1:
            await client.send_message(event.chat_id, usrtxt, parse_mode='Markdown')
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

# Random sorular listesi
random_sorular = [
    "Nerdesin?",
    "Nasılsın?",
    "Napiyorsun?",
    "Kimlerlesin?",
    "Neler yapıyorsun?",
    "Hangi şehirdesin?",
    "Hangi ülkedesin?",
    "En son ne yedin?",
    "En son ne izledin?",
    "Hangi müzik türünü dinliyorsun?",
    "Hangi kitabı okuyorsun?",
    "Hangi aktiviteye meraklısın?",
    "En son gittiğin yer neresi?",
    "Hangi konuda konuşmak istersin?",
    "Bir dilek hakkın olsa, ne dilerdin?",
    "Hangi hobiyle ilgileniyorsun?",
    "En sevdiğin renk nedir?",
    "Bir yetenek kazanma şansın olsa, neyi seçerdin?",
    "Hayalinizdeki tatil nasıl bir yerde?",
    "Bir gün boyunca bir ünlü ile değişme şansın olsa, kim olurdu?",
    "Bir super güç seçme şansın olsa, neyi seçerdin?",
    "En son ne zaman gülümsedin?",
    "Hangi sporu yapmayı seversin?",
    "Hangi konuda uzman olmak istersin?",
    "Bir film karakteri olma şansın olsa, kim olurdu?",
    "Hayalindeki ev nasıl bir yerde?",
    "Hangi tür film/dizi izlemeyi seversin?",
    "Bir dilek gerçekleşse, ne dilek tutarsın?",
    "Hangi mevsim seni daha mutlu eder?",
    "En son hangi şarkıyı dinledin?",
    "Bir şehirde yaşama şansın olsa, hangi şehri seçerdin?",
    "Hayalindeki iş nedir?",
    "En sevdiğin içecek nedir?",
    "Bir gün boyunca başka birini oynama şansın olsa, kim olurdu?",
    "Bir yetenek kazanma şansın olsa, neyi seçerdin?",
    "Bir keşif yapma şansın olsa, nereyi keşfederdin?",
    "Hangi sanat dalı seni daha çok etkiler?",
    "En sevdiğin doğa harikası nedir?",
    "Bir gün boyunca başka bir ülkede yaşama şansın olsa, hangi ülkeyi seçerdin?",
    "Hangi hayvanı evcil beslemek istersin?",
    "En son ne zaman bir dostunla güzel bir anı paylaştın?",
    "Bir gün boyunca hangi aktiviteyi yapmak isterdin?",
    "Hangi dilde daha iyi olmak isterdin?",
    "Hangi şey seni motive eder?",
    "Bir gün boyunca bir kitap karakteri olma şansın olsa, kim olurdu?",
    "Bir tatil destinasyonu seçme şansın olsa, nereyi seçerdin?",
]

# Aktif çalışan grupları takip etmek için liste
anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
    global anlik_calisan
    anlik_calisan.remove(event.chat_id)

@client.on(events.NewMessage(pattern="^/ntag"))
async def gunaydin_etiketleme(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Grup Ve Kanallarda Geçerlidir.")

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("🤚🏻Opss! Bu Komut Sadece Yöneticiler Kullanabilir.")

    anlik_calisan.append(event.chat_id)
    await event.respond("Etiketleme İşlemi Başlatıldı! Biraz bekleyin...")

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
        usrnum += 1
        mesaj = random.choice(random_sorular)
        usrtxt += f"➪ [{usr.first_name}](tg://user?id={usr.id}), {mesaj}\n"
        if event.chat_id not in anlik_calisan:
            await event.respond("Etiketleme İşlemi Başarıyla Durdurulmuştur!")
            return
        if usrnum == 1:
            await client.send_message(event.chat_id, usrtxt, parse_mode='Markdown')
            await asyncio.sleep(15)
            usrnum = 0
            usrtxt = ""

print("YESSS!, Bot Çalışıyor lexper.")
client.run_until_disconnected()
