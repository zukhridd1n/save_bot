# bot_config.py
# Telegram bot sozlamalari

# MUHIM: Bu yerga o'z bot tokeningizni qo'ying!
# @BotFather dan oling
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']

# Admin ID (ixtiyoriy - statistika uchun)
# O'z ID ingizni bilish uchun @userinfobot ga yozing
ADMIN_ID = os.environ['ADMIN_ID']  # O'z Telegram ID ingiz

# Fayl hajmi cheklovi (baytlarda)
MAX_FAYL_HAJMI = 1000 * 1024 * 1024  # 50 MB

# Xabarlar matni
XABARLAR = {
    "start": """
🎬 **Video Yuklovchi Bot**

Assalomu alaykum! Men YouTube va Instagram'dan video va audio yuklab beraman.

📌 **Qanday ishlatish:**
1️⃣ Menga video havolasini yuboring
2️⃣ Video yoki Audio tugmasini tanlang
3️⃣ Faylni oling!

🔗 **Qo'llab-quvvatlanadigan saytlar:**
✅ YouTube (youtube.com, youtu.be)
✅ Instagram (instagram.com)

❓ Yordam: /help
""",

    "help": """
❓ **Yordam**

**Buyruqlar:**
/start - Botni boshlash
/help - Bu yordam xabari
/stats - Statistika (faqat admin)

**Misol havolalar:**
- `https://youtube.com/watch?v=dQw4w9WgXcQ`
- `https://instagram.com/p/ABC123/`

**Cheklovlar:**
⚠️ Maksimal fayl hajmi: 50 MB
⚠️ Ba'zi videolar mualliflik huquqi sababli yuklanmasligi mumkin

**Muammolar:**
Agar video yuklanmasa:
1. Havola to'g'riligini tekshiring
2. Video ochiq ekanligini tekshiring
3. Video 50 MB dan kichik ekanligini tekshiring
4. Iltimos, biroz kutib qayta urinib ko'ring
""",

    "tanlang": "✅ Havola qabul qilindi!\n\n📥 Nima yuklamoqchisiz?",
    "kutish": "⏳ Yuklanmoqda, iltimos kuting...",
    "video_tayyor": "✅ Video tayyor!\n📄 {nomi}\n⏱️ {davomiylik}\n\n📤 Yuborilmoqda...",
    "audio_tayyor": "✅ Audio tayyor!\n🎵 {nomi}\n⏱️ {davomiylik}\n\n📤 Yuborilmoqda...",
    "katta_fayl": "⚠️ Fayl juda katta ({hajmi}).\nTelegram cheklovi: 50 MB\n\nℹ️ Kichikroq video tanlang yoki faqat audio yuklab oling.",
    "havola_topilmadi": "❌ Havola topilmadi. Iltimos, qaytadan video havolasini yuboring.",
    "bekor_qilindi": "❌ Bekor qilindi. Yangi havola yuboring.",
}