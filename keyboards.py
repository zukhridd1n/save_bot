# keyboards.py
# Klaviaturalar

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def tanlov_klaviatura():
    """Audio yoki Video"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🎵 Audio", callback_data="audio"),
            InlineKeyboardButton(text="🎬 Video", callback_data="video")
        ],
        [
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor")
        ]
    ])
    return keyboard


def video_sifat_klaviatura():
    """Video sifati"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Mobil (360p)", callback_data="video_mobil")
        ],
        [
            InlineKeyboardButton(text="⚡ Standart (480p)", callback_data="video_standart")
        ],
        [
            InlineKeyboardButton(text="🎬 HD (720p)", callback_data="video_hd")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="bekor")
        ]
    ])
    return keyboard