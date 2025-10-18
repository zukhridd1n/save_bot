# 🚀 Aiogram Bot Sozlash

## Aiogram nima?

Aiogram 3.x - zamonaviy va tez Telegram bot kutubxonasi. Python-telegram-bot dan tezroq va soddaroq.

## 📁 Fayllar
```
video-yuklovchi-bot/
│
├── config.py              # Eski sozlamalar
├── bot_config.py          # Bot sozlamalari (YANGI)
├── keyboards.py           # Klaviaturalar (YANGI)
├── bot.py                 # Asosiy bot fayli (YANGI)
├── utils.py               # Yordamchi funksiyalar
├── downloader.py          # Yuklovchi
└── requirements.txt       # Kutubxonalar
```

## 1️⃣ O'rnatish
```bash
pip install -r requirements.txt
```

## 2️⃣ Token Olish

1. @BotFather ga yozing
2. /newbot
3. Bot nomini va username kiriting
4. Tokenni nusxalang

## 3️⃣ Token Qo'yish

`bot_config.py` ni oching:
```python
BOT_TOKEN = "5234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw"
```

## 4️⃣ Admin ID Qo'yish (ixtiyoriy)

O'z Telegram ID ingizni bilish uchun @userinfobot ga yozing.
```python
ADMIN_ID = 123456789  # O'z ID ingiz
```

## 5️⃣ Ishga Tushirish
```bash
python bot.py
```

## 🎯 Afzalliklari

✅ **Tez** - Python-telegram-bot dan 2-3 marta tezroq
✅ **Sodda** - Async/await bilan qulay
✅ **Zamonaviy** - Aiogram 3.x eng yangi versiya
✅ **FSM** - Foydalanuvchi holatini saqlash o'rnatilgan
✅ **Middleware** - Qo'shimcha funksiyalar oson qo'shiladi

## 📊 Yangi Funksiyalar

1. **Statistika** - /stats buyrug'i (admin uchun)
2. **FSM** - Foydalanuvchi holatini saqlash
3. **Bekor qilish** - Jarayonni to'xtatish
4. **Logging** - Xatolarni kuzatish
5. **Tezkor** - Async/await ishlatadi

## 🔧 Sozlamalarni O'zgartirish

`bot_config.py` da:
```python
# Fayl hajmi cheklovi
MAX_FAYL_HAJMI = 100 * 1024 * 1024  # 100 MB

# Xabarlar matni
XABARLAR = {
    "start": "Sizning matn...",
    ...
}
```

## 🆚 Python-telegram-bot vs Aiogram

| Xususiyat | python-telegram-bot | Aiogram 3.x |
|-----------|---------------------|-------------|
| Tezlik | Yaxshi | Juda tez ⚡ |
| Sintaksis | Oddiy | Zamonaviy |
| FSM | Qo'shimcha kutubxona | O'rnatilgan |
| Async | Ha | Ha (majburiy) |
| O'rganish | Oson | O'rtacha |
| Dokumentatsiya | Juda yaxshi | Yaxshi |

## ❓ Tez-tez So'raladigan Savollar

**S: Qaysi versiya yaxshiroq?**
J: Aiogram 3.x tezroq va zamonaviyroq. Katta botlar uchun tavsiya etiladi.

**S: Eski versiyadan o'tish qiyin emasmikan?**
J: Men ikkalasini ham yozdim. Faqat `bot.py` ishga tushiring.

**S: /stats ishlamayapti?**
J: `bot_config.py` da `ADMIN_ID` ni o'z ID ingizga o'zgartiring.

**S: FSM nima?**
J: Finite State Machine - foydalanuvchi holatini saqlaydi. Masalan: "havola kutilmoqda" holati.

## 🚀 Deploy Qilish

### Heroku
```bash
echo "web: python bot.py" > Procfile
git push heroku main
```

### VPS (Ubuntu)
```bash
# Screen ochish
screen -S video_bot

# Botni ishga tushirish
python3 bot.py

# Screen'dan chiqish: Ctrl+A, D
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

Omad! 🎉