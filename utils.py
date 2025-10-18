# utils.py

import re

def url_tekshir(url):
    """URL tekshirish"""
    return bool(re.search(r'(youtube\.com|youtu\.be|instagram\.com)', url))

def hajmni_formatlash(bayt):
    """Hajm formatlash"""
    if not bayt:
        return "?"
    for birlik in ['B', 'KB', 'MB', 'GB']:
        if bayt < 1024:
            return f"{bayt:.0f} {birlik}"
        bayt /= 1024
    return f"{bayt:.1f} GB"

def vaqtni_formatlash(soniyalar):
    """Vaqt formatlash"""
    if not soniyalar:
        return "?"
    daqiqa = int(soniyalar // 60)
    soniya = int(soniyalar % 60)
    return f"{daqiqa}:{soniya:02d}" if daqiqa > 0 else f"0:{soniya:02d}"

def xatolik_xabari(xato):
    """Xatolik xabari"""
    xato_str = str(xato).lower()
    if 'network' in xato_str:
        return "❌ Internet xatolik"
    elif 'private' in xato_str:
        return "❌ Video ochiq emas"
    elif 'copyright' in xato_str:
        return "❌ Copyright himoya"
    return "❌ Xatolik"