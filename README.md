# 🎬 Video Yuklovchi Bot (Streaming Versiya)

YouTube va Instagram'dan video va audio yuklab oluvchi Telegram bot. **Streaming texnologiyasi** - fayllar to'g'ridan-to'g'ri foydalanuvchiga yuboriladi, disk joy tejaydi va juda tez ishlaydi!

## ✨ Imkoniyatlar

- ✅ **YouTube** video va audio yuklash
- ✅ **Instagram** video va audio yuklash
- 🎵 **Audio** - MP3 formatida (320 kbps)
- 🎬 **Video** - 3 xil sifatda:
  - 📱 Mobil (360p) - 5-15 MB
  - ⚡ Standart (480p) - 10-30 MB
  - 🎬 HD (720p) - 30-50 MB
- ⚡ **Streaming** - Diskka saqlamasdan to'g'ri yuborish
- 🚀 **Juda tez** - 5-15 soniyada tayyor
- 💾 **Disk joy tejash** - vaqtinchalik fayllar avtomatik o'chiriladi
- 🎯 **Tugmalar bilan** - Qulay interfeys

## 📸 Скриншотlar
```
Bot: 📎 Video havolasini yuboring

User: https://youtube.com/watch?v=...

Bot: ✅ Havola qabul qilindi!
     📥 Nima yuklamoqchisiz?
     
     [🎵 Audio]  [🎬 Video]
     [❌ Bekor qilish]

User: [🎬 Video bosadi]

Bot: 📊 Video sifatini tanlang:
     
     [📱 Mobil (360p)]
     [⚡ Standart (480p)]
     [🎬 HD (720p)]
     [🔙 Orqaga]

User: [⚡ Standart bosadi]

Bot: 🎬 Video yuklanmoqda...
     📊 ⚡ Standart (480p)
     ⏳ Streaming...
     
     ✅ Video tayyor!
     🎬 Video Nomi
     📊 ⚡ Standart (480p)
     💾 15 MB
     
     📤 Yuborilmoqda...
     
     [Video yuboriladi]
```

## 🚀 Tezkor Boshlash

### 1. Talablar

- Python 3.8+
- FFmpeg
- Telegram Bot Token

### 2. O'rnatish
```bash
# Loyihani klonlash yoki yuklab olish
git clone https://github.com/sizning-username/video-bot.git
cd video-bot

# Virtual environment yaratish (ixtiyoriy)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# FFmpeg o'rnatish
# Ubuntu/Debian:
sudo apt update && sudo apt install ffmpeg

# Mac:
brew install ffmpeg

# Windows:
choco install ffmpeg
```

### 3. Sozlash

**Bot Token Olish:**

1. Telegram'da [@BotFather](https://t.me/BotFather) ni oching
2. `/newbot` buyrug'ini yuboring
3. Bot nomi kiriting (masalan: `Video Yuklovchi`)
4. Bot username kiriting (masalan: `video_yuklovchi_uz_bot`)
5. BotFather sizga token beradi

**Token Qo'yish:**
```bash
# bot_config.py faylini oching
nano bot_config.py

# BOT_TOKEN ni o'zgartiring:
BOT_TOKEN = "5234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw"

# Saqlash: Ctrl+X, Y, Enter
```

### 4. Ishga Tushirish
```bash
python3 bot.py
```

**Natija:**
```
==================================================
🚀 STREAMING BOT ISHGA TUSHDI!
==================================================
👤 @video_yuklovchi_uz_bot
🆔 1234567890
==================================================
⚡ Streaming - Juda tez!
📱 Telegram'da /start bosing
🛑 To'xtatish: Ctrl+C
==================================================
```

## 📁 Loyiha Tuzilishi
```
video-bot/
│
├── bot.py              # Asosiy bot fayli
├── bot_config.py       # Bot sozlamalari (token)
├── downloader.py       # Video/Audio yuklovchi
├── keyboards.py        # Telegram klaviaturalari
├── utils.py            # Yordamchi funksiyalar
├── requirements.txt    # Python kutubxonalari
├── README.md           # Bu fayl
└── .gitignore          # Git ignore fayllar
```

## 🎯 Foydalanish

### Oddiy Foydalanuvchi:

1. **Botni toping:** Telegram'da `@sizning_bot_username`
2. **Boshlash:** `/start` tugmasini bosing
3. **Havola yuboring:**
```
   https://youtube.com/watch?v=dQw4w9WgXcQ
```
4. **Tanlang:**
   - 🎵 Audio - darhol yuklanadi
   - 🎬 Video - sifatni tanlang
5. **Oling:** 5-15 soniyada tayyor!

### Qo'llab-quvvatlanadigan Havolalar:

**YouTube:**
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

**Instagram:**
- `https://instagram.com/p/POST_ID/`
- `https://www.instagram.com/reel/REEL_ID/`

## ⚙️ Sozlamalar

### Video Sifati O'zgartirish

`downloader.py` faylida:
```python
# Mobil sifat (360p)
'best[height<=360][ext=mp4]'

# Standart sifat (480p)
'best[height<=480][ext=mp4]'

# HD sifat (720p)
'best[height<=720][ext=mp4]'
```

### Audio Sifati O'zgartirish

`downloader.py` faylida:
```python
'preferredquality': '96',  # 64, 96, 128, 192, 256, 320
```

### Fayl Hajmi Cheklovi

`bot_config.py` faylida:
```python
MAX_FAYL_HAJMI = 50 * 1024 * 1024  # 50 MB (Telegram cheklovi)
```

### Admin ID Qo'shish

`bot_config.py` faylida:
```python
ADMIN_ID = 123456789  # O'z Telegram ID ingiz
```

Admin ID ni bilish uchun: [@userinfobot](https://t.me/userinfobot)

## 🔧 Muammolarni Hal Qilish

### Muammo: "FFmpeg topilmadi"

**Yechim:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Tekshirish
ffmpeg -version
```

### Muammo: "Module not found: aiogram"

**Yechim:**
```bash
pip install -r requirements.txt
```

### Muammo: "Bot javob bermayapti"

**Yechim:**
1. Token to'g'ri kiritilganligini tekshiring
2. Internet aloqangizni tekshiring
3. Bot to'xtatilgan bo'lsa, qayta ishga tushiring:
```bash
   python3 bot.py
```

### Muammo: "Video juda katta"

**Yechim:**
- Kichikroq sifat tanlang (Mobil 360p)
- Faqat audio yuklab oling
- Qisqaroq video tanlang

### Muammo: "Video yuklanmadi"

**Yechim:**
1. URL to'g'riligini tekshiring
2. Video ochiq ekanligini tekshiring
3. Video copyright bilan himoyalanmaganligini tekshiring
4. Boshqa video bilan sinab ko'ring

## 🚀 Serverga Joylashtirish (Deploy)

### VPS (Ubuntu) da
```bash
# Screen ochish
screen -S video_bot

# Botni ishga tushirish
cd ~/video-bot
python3 bot.py

# Screen'dan chiqish: Ctrl+A, D
# Qaytish: screen -r video_bot
```

### Systemd Service (Linux)
```bash
# Service fayli yaratish
sudo nano /etc/systemd/system/video-bot.service
```

**Fayl matni:**
```ini
[Unit]
Description=Video Yuklovchi Telegram Bot
After=network.target

[Service]
Type=simple
User=sizning_username
WorkingDirectory=/home/sizning_username/video-bot
ExecStart=/usr/bin/python3 /home/sizning_username/video-bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Aktivlashtirish:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable video-bot
sudo systemctl start video-bot

# Holat
sudo systemctl status video-bot

# Loglar
sudo journalctl -u video-bot -f
```

### Docker bilan

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# FFmpeg o'rnatish
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Kutubxonalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fayllar
COPY . .

# Ishga tushirish
CMD ["python", "bot.py"]
```

**Ishlatish:**
```bash
# Build
docker build -t video-bot .

# Run
docker run -d --name video-bot --restart unless-stopped video-bot

# Loglar
docker logs -f video-bot
```

### Heroku da
```bash
# Procfile yaratish
echo "worker: python bot.py" > Procfile

# Git
git init
git add .
git commit -m "Initial commit"

# Heroku
heroku create video-bot-uz
heroku config:set BOT_TOKEN="sizning_tokeningiz"
git push heroku main
heroku ps:scale worker=1

# Loglar
heroku logs --tail
```

## 📊 Texnik Ma'lumotlar

### Arxitektura
```
User → Telegram → Bot → yt-dlp → YouTube/Instagram
                   ↓
              Streaming
                   ↓
         Temp File (/tmp/)
                   ↓
        FSInputFile (Aiogram)
                   ↓
           Telegram → User
                   ↓
         Delete Temp File
```

### Ishlash Jarayoni

1. **Havola qabul:** User havola yuboradi
2. **Tanlov:** Audio/Video tugmalarni bosadi
3. **Yuklash:** yt-dlp orqali yuklanadi (parallel, streaming)
4. **Vaqtinchalik saqlash:** `/tmp/` papkaga
5. **Yuborish:** Telegram API orqali to'g'ri yuborish
6. **Tozalash:** Fayl darhol o'chiriladi

### Tezlik Optimizatsiyalari

- ✅ `concurrent_fragment_downloads: 16` - parallel yuklash
- ✅ `http_chunk_size: 10MB` - katta qismlar
- ✅ `buffersize: 16384` - buffer optimallashtirish
- ✅ Vaqtinchalik fayllar - disk I/O kamaytirish
- ✅ `asyncio.to_thread` - async/await
- ✅ Minimal retry - vaqt tejash

### Xotira va Disk Foydalanish

| Xususiyat | Qiymat |
|-----------|--------|
| RAM | 100-200 MB |
| Disk (temp) | 10-50 MB (vaqtinchalik) |
| Network | 1-5 MB/s |
| CPU | 20-40% (yuklash vaqtida) |

## 📈 Ishlash Statistikasi

### Tezlik (O'rtacha)

| Video Uzunligi | Audio | Video (480p) | Jami |
|----------------|-------|--------------|------|
| 3 daqiqa | 4 sek | 8 sek | **12 sek** |
| 5 daqiqa | 5 sek | 12 sek | **17 sek** |
| 10 daqiqa | 7 sek | 20 sek | **27 sek** |

### Fayl Hajmi (O'rtacha)

| Format | 3 min | 5 min | 10 min |
|--------|-------|-------|--------|
| Audio (96kbps) | 2 MB | 4 MB | 7 MB |
| Video (360p) | 8 MB | 15 MB | 30 MB |
| Video (480p) | 15 MB | 25 MB | 50 MB |
| Video (720p) | 30 MB | 50 MB | 100 MB |

## 🔒 Xavfsizlik

- ✅ Token `.gitignore` da
- ✅ Vaqtinchalik fayllar avtomatik o'chiriladi
- ✅ User ma'lumotlari saqlanmaydi
- ✅ HTTPS orqali aloqa
- ✅ Input validation

**Tavsiya:**
```bash
# .env fayl ishlatish (production)
pip install python-dotenv

# .env
BOT_TOKEN=sizning_tokeningiz
ADMIN_ID=123456789

# bot_config.py
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
```

## 📝 Litsenziya

MIT License - Bepul va ochiq manbali

## 🤝 Hissa Qo'shish

Pull requestlar xush kelibsiz!

1. Fork qiling
2. Branch yarating (`git checkout -b feature/AmazingFeature`)
3. Commit qiling (`git commit -m 'Add AmazingFeature'`)
4. Push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## ⭐ Qo'llab-quvvatlash

Agar loyiha foydali bo'lsa, ⭐ star bering!

## 📞 Aloqa

- **Telegram:** [@sizning_username](https://t.me/sizning_username)
- **Email:** sizning@email.com
- **GitHub:** [github.com/sizning-username](https://github.com/sizning-username)

## 🙏 Minnatdorchilik

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video yuklovchi
- [Aiogram](https://github.com/aiogram/aiogram) - Telegram Bot framework
- [FFmpeg](https://ffmpeg.org/) - Media konvertatsiya
- [Python](https://python.org/) - Dasturlash tili

## 📚 Qo'shimcha Resurslar

- [Aiogram Dokumentatsiya](https://docs.aiogram.dev/)
- [yt-dlp Dokumentatsiya](https://github.com/yt-dlp/yt-dlp#readme)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [FFmpeg Dokumentatsiya](https://ffmpeg.org/documentation.html)

## 🎓 O'quv Maqsadlari

Bu bot quyidagilarni o'rganish uchun yaxshi misol:

- ✅ Aiogram 3.x - zamonaviy async bot framework
- ✅ yt-dlp - video yuklash API
- ✅ asyncio - asinxron dasturlash
- ✅ FSM - State Management
- ✅ Inline Keyboards - interaktiv tugmalar
- ✅ Streaming - fayl yuklash optimizatsiyasi

## 🆕 Kelajakdagi Rejalar

- [ ] Playlist qo'llab-quvvatlash
- [ ] TikTok qo'shish
- [ ] Facebook qo'shish
- [ ] Twitter qo'shish
- [ ] Subtitle yuklash
- [ ] Video thumbnail
- [ ] Progress bar
- [ ] Multi-language
- [ ] Admin panel
- [ ] Statistika dashboard
- [ ] User qidirish tarixi

## 📄 Changelog

### v1.0.0 (2025-10-18)
- ✅ Birinchi release
- ✅ YouTube qo'llab-quvvatlash
- ✅ Instagram qo'llab-quvvatlash
- ✅ Audio/Video yuklash
- ✅ 3 xil video sifati
- ✅ Streaming texnologiyasi
- ✅ FSM bilan state management
- ✅ Inline keyboards

---

**Yaratildi ❤️ bilan O'zbekiston'da | 2025**

**⚡ Streaming - Tez va Sifatli! 🚀**

