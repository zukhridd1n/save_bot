# downloader.py
# STREAMING VERSIYA - Vaqtinchalik fayllar

import os
import tempfile
from pathlib import Path
import yt_dlp


class VideoYuklovchi:
    """Streaming yuklovchi"""

    def __init__(self):
        # Vaqtinchalik papka
        self.temp_dir = tempfile.gettempdir()

    def video_stream_yuklash(self, url, sifat='standart'):
        """
        Video stream yuklash - to'g'ri yuborish uchun
        """
        # Sifatga qarab format
        if sifat == 'mobil':
            format_str = 'best[height<=360][ext=mp4]/best[height<=480][ext=mp4]/worst[ext=mp4]'
        elif sifat == 'hd':
            format_str = 'best[height<=720][ext=mp4]/best[ext=mp4]'
        else:
            format_str = 'best[height<=480][ext=mp4]/best[height<=720][ext=mp4]/best[ext=mp4]'

        # Vaqtinchalik fayl
        temp_file = os.path.join(self.temp_dir, '%(id)s.%(ext)s')

        sozlamalar = {
            'format': format_str,
            'outtmpl': temp_file,

            # STREAMING OPTIMIZATSIYA
            'concurrent_fragment_downloads': 16,  # Maksimal parallel
            'http_chunk_size': 10485760,  # 10MB chunk
            'buffersize': 16384,  # Buffer
            'retries': 1,  # Minimal retry
            'socket_timeout': 15,

            # No-cache
            'nocheckcertificate': True,
            'prefer_insecure': True,

            'quiet': True,
            'no_warnings': True,
        }

        try:
            with yt_dlp.YoutubeDL(sozlamalar) as ydl:
                info = ydl.extract_info(url, download=True)
                fayl = ydl.prepare_filename(info)

                return {
                    "muvaffaqiyat": True,
                    "fayl": fayl,
                    "nomi": info.get('title', 'Video')[:50]
                }
        except Exception as e:
            print(f"Stream video xato: {e}")
            return {"muvaffaqiyat": False}

    def audio_stream_yuklash(self, url):
        """
        Audio stream yuklash - to'g'ri yuborish uchun
        """
        # Vaqtinchalik fayl
        temp_file = os.path.join(self.temp_dir, '%(id)s.%(ext)s')

        sozlamalar = {
            'format': 'bestaudio[ext=m4a]/bestaudio/worstaudio',
            'outtmpl': temp_file,

            # MP3 konvertatsiya
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '96',
            }],

            # STREAMING OPTIMIZATSIYA
            'concurrent_fragment_downloads': 16,
            'http_chunk_size': 10485760,
            'buffersize': 16384,
            'retries': 1,
            'socket_timeout': 15,

            'quiet': True,
            'no_warnings': True,
        }

        try:
            with yt_dlp.YoutubeDL(sozlamalar) as ydl:
                info = ydl.extract_info(url, download=True)
                fayl_asosi = ydl.prepare_filename(info)
                audio_fayl = os.path.splitext(fayl_asosi)[0] + '.mp3'

                return {
                    "muvaffaqiyat": True,
                    "fayl": audio_fayl,
                    "nomi": info.get('title', 'Audio')[:50]
                }
        except Exception as e:
            print(f"Stream audio xato: {e}")
            return {"muvaffaqiyat": False}