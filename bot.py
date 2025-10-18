# bot.py
# STREAMING VERSIYA - Botga yuklamasdan to'g'ri yuborish!

import asyncio
import logging
import os
import tempfile
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, BufferedInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from bot_config import BOT_TOKEN, MAX_FAYL_HAJMI
from keyboards import tanlov_klaviatura, video_sifat_klaviatura
from downloader import VideoYuklovchi
from utils import hajmni_formatlash

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
yuklovchi = VideoYuklovchi()


# FSM States
class Yuklash(StatesGroup):
    havola_kutish = State()
    tanlov_kutish = State()
    yuklanmoqda = State()


@router.message(Command("start"))
async def start(msg: Message, state: FSMContext):
    """Start"""
    await state.clear()
    await msg.answer(
        "⚡ **SUPER TEZ VIDEO BOT**\n\n"
        "📎 Video havolasini yuboring:\n\n"
        "✅ YouTube\n"
        "✅ Instagram\n\n"
        "🚀 Streaming - Juda tez!"
    )


@router.message(F.text.regexp(r'https?://'))
async def havola_qabul(msg: Message, state: FSMContext):
    """Havola qabul qilish"""
    url = msg.text.strip()

    # Havolani saqlash
    await state.update_data(url=url)
    await state.set_state(Yuklash.tanlov_kutish)

    # Tanlov klaviaturasi
    await msg.answer(
        "✅ Havola qabul qilindi!\n\n"
        "📥 Nima yuklamoqchisiz?",
        reply_markup=tanlov_klaviatura()
    )


@router.callback_query(F.data == "audio")
async def audio_tanlandi(callback: CallbackQuery, state: FSMContext):
    """Audio tanlandi - STREAMING"""
    await callback.answer()

    data = await state.get_data()
    url = data.get("url")

    if not url:
        await callback.message.edit_text("❌ Havola topilmadi")
        return

    await state.set_state(Yuklash.yuklanmoqda)
    await callback.message.edit_text("🎵 Audio yuklanmoqda...")

    try:
        # STREAMING - to'g'ridan-to'g'ri yuklash
        result = await asyncio.to_thread(
            yuklovchi.audio_stream_yuklash,
            url
        )

        if result.get("muvaffaqiyat"):
            file_path = result["fayl"]
            nomi = result["nomi"]
            hajm = os.path.getsize(file_path)

            if hajm < MAX_FAYL_HAJMI:
                await callback.message.edit_text(
                    f"✅ Audio tayyor!\n\n"
                    f"🎵 {nomi}\n"
                    f"💾 {hajmni_formatlash(hajm)}\n\n"
                    f"📤 Yuborilmoqda..."
                )

                # TO'G'RIDAN-TO'G'RI YUBORISH
                audio_file = FSInputFile(file_path)
                await callback.message.answer_audio(
                    audio=audio_file,
                    title=nomi
                )

                # Faylni darhol o'chirish
                try:
                    os.remove(file_path)
                except:
                    pass

                await callback.message.delete()
                logger.info(f"✅ Audio stream: {callback.from_user.full_name}")
            else:
                await callback.message.edit_text(
                    f"⚠️ Audio katta: {hajmni_formatlash(hajm)}"
                )
                try:
                    os.remove(file_path)
                except:
                    pass
        else:
            await callback.message.edit_text("❌ Audio yuklanmadi")

    except Exception as e:
        logger.error(f"Audio xato: {e}")
        await callback.message.edit_text("❌ Xatolik yuz berdi")

    finally:
        await state.clear()


@router.callback_query(F.data == "video")
async def video_tanlandi(callback: CallbackQuery, state: FSMContext):
    """Video tanlandi - Sifat tanlasin"""
    await callback.answer()

    await callback.message.edit_text(
        "📊 Video sifatini tanlang:\n\n"
        "📱 **Mobil** - 360p (tez)\n"
        "⚡ **Standart** - 480p (tavsiya)\n"
        "🎬 **HD** - 720p (sifatli)",
        reply_markup=video_sifat_klaviatura()
    )


@router.callback_query(F.data.in_(["video_mobil", "video_standart", "video_hd"]))
async def video_yuklash(callback: CallbackQuery, state: FSMContext):
    """Video yuklash - STREAMING"""
    await callback.answer()

    data = await state.get_data()
    url = data.get("url")

    if not url:
        await callback.message.edit_text("❌ Havola topilmadi")
        return

    # Sifatni aniqlash
    sifat_map = {
        "video_mobil": ("mobil", "📱 Mobil (360p)"),
        "video_standart": ("standart", "⚡ Standart (480p)"),
        "video_hd": ("hd", "🎬 HD (720p)")
    }

    sifat, sifat_text = sifat_map.get(callback.data, ("standart", "⚡ Standart"))

    await state.set_state(Yuklash.yuklanmoqda)
    await callback.message.edit_text(
        f"🎬 Video yuklanmoqda...\n\n"
        f"📊 {sifat_text}\n"
        f"⏳ Streaming..."
    )

    try:
        # STREAMING - to'g'ridan-to'g'ri yuklash
        result = await asyncio.to_thread(
            yuklovchi.video_stream_yuklash,
            url,
            sifat=sifat
        )

        if result.get("muvaffaqiyat"):
            file_path = result["fayl"]
            nomi = result["nomi"]
            hajm = os.path.getsize(file_path)

            if hajm < MAX_FAYL_HAJMI:
                await callback.message.edit_text(
                    f"✅ Video tayyor!\n\n"
                    f"🎬 {nomi}\n"
                    f"📊 {sifat_text}\n"
                    f"💾 {hajmni_formatlash(hajm)}\n\n"
                    f"📤 Yuborilmoqda..."
                )

                # TO'G'RIDAN-TO'G'RI YUBORISH
                video_file = FSInputFile(file_path)
                await callback.message.answer_video(
                    video=video_file,
                    caption=f"🎬 {nomi}\n📊 {sifat_text}",
                    supports_streaming=True
                )

                # Faylni darhol o'chirish
                try:
                    os.remove(file_path)
                except:
                    pass

                await callback.message.delete()
                logger.info(f"✅ Video stream ({sifat}): {callback.from_user.full_name}")
            else:
                await callback.message.edit_text(
                    f"⚠️ Video katta: {hajmni_formatlash(hajm)}\n\n"
                    f"💡 Kichikroq sifat tanlang"
                )
                try:
                    os.remove(file_path)
                except:
                    pass
        else:
            await callback.message.edit_text("❌ Video yuklanmadi")

    except Exception as e:
        logger.error(f"Video xato: {e}")
        await callback.message.edit_text("❌ Xatolik yuz berdi")

    finally:
        await state.clear()


@router.callback_query(F.data == "bekor")
async def bekor_qilish(callback: CallbackQuery, state: FSMContext):
    """Bekor qilish"""
    await state.clear()
    await callback.message.edit_text("❌ Bekor qilindi")
    await callback.answer()


@router.message()
async def boshqa(msg: Message):
    """Boshqa xabarlar"""
    await msg.answer("📎 Menga video havolasini yuboring!")


async def main():
    """Bot ishga tushirish"""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ bot_config.py da BOT_TOKEN ni kiriting!")
        return

    dp.include_router(router)

    print("\n" + "=" * 50)
    print("🚀 STREAMING BOT ISHGA TUSHDI!")
    print("=" * 50)
    me = await bot.get_me()
    print(f"👤 @{me.username}")
    print(f"🆔 {me.id}")
    print("=" * 50)
    print("⚡ Streaming - Juda tez!")
    print("📱 Telegram'da /start bosing")
    print("🛑 To'xtatish: Ctrl+C")
    print("=" * 50 + "\n")

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Bot to'xtatildi")