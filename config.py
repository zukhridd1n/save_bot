# config.py
# Minimal sozlamalar - FAQAT TEZLIK

import os

YUKLAB_OLISH_PAPKA = "yuklab_olinganlar"

# ENG KICHIK FORMATLAR = ENG TEZ
VIDEO_FORMAT = 'worst[ext=mp4]/worst'
AUDIO_FORMAT = 'worstaudio/worst'

AUDIO_CODEC = 'mp3'
AUDIO_SIFAT = '320'

FAYL_NOMI_FORMAT = '%(title)s.%(ext)s'

RUXSAT_BERILGAN_SAYTLAR = {
    'youtube': r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+',
    'instagram': r'(https?://)?(www\.)?instagram\.com/.+'
}

MAX_FAYL_HAJMI = 50 * 1024 * 1024