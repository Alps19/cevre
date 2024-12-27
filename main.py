import discord  # Discord API'si ile iletişim kurmak için kullanılan kütüphane
from discord.ext import commands  # Komut tabanlı bot oluşturmak için framework
import requests  # HTTP isteklerini yapmak için kullanılan kütüphane

# Discord botunun mesaj içeriğine erişmesini sağlamak için gerekli izinleri ayarlıyoruz.
intents = discord.Intents.default()
intents.message_content = True

# Botun komut ön ekini belirliyoruz ($) ve izinleri aktarıyoruz.
bot = commands.Bot(command_prefix='$', intents=intents)

# Botun Discord'a başarıyla bağlandığını kontrol etmek için bir olay tanımlıyoruz.
@bot.event
async def on_ready():
    # Botun başarıyla çalıştığını ve giriş yaptığını terminalde yazdırır.
    print(f'{bot.user} olarak giriş yaptık')


@bot.command(name='cevre')
async def cevre(ctx):
    '''
    '''
    öneriler = [
        "1. Tekrar kullanılabilir çantalar kullanın.",
        "2. Plastik yerine cam veya metal şişeler tercih edin.",
        "3. Enerji tasarrufu için LED ampuller kullanın.",
        "4. Geri dönüşüm kutularını kullanarak atıkları ayırın.",
        "5. Yerel ürünleri satın alarak karbon ayak izinizi azaltın."
    ]
    await ctx.send("Çevre için yapabileceğiniz bazı şeyler:\n" + "\n".join(öneriler))


TOKEN = 'MTMyMTkzMTI1ODI1OTA1MDU3Nw.GAJ5mc.GotXfEfmbT2L7yce0iBSWQHSzu91MU5QsaIljY'  # Buraya botunuzun tokenini ekleyin
bot.run(TOKEN)
