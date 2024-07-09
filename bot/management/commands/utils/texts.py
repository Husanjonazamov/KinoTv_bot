MAIN_MENU = \
"""
<b>Asosiy menyu</b>
"""

START_USER = \
"""
<b>
👋 Assalomu alaykum. KinoTv botga xush kelibsiz!
</b>
"""

DOWNLOAD_MOVIES_HANDLER = \
"""
<b>
✍🏻 kino kodini yuboring!
</b>
"""

CHANNEL_REQUEST = \
"""
<b>
Iltimos, quyidagi kanallarga obuna bo'ling 👇
</b>
"""

CHANNEL_CHECK = \
"""
<b>
👋 Assalomu alaykum. KinoTv botga xush kelibsiz!
</b>
"""

CHANNEL_ERROR = \
"""
<b>
❌ Siz hali hamma kanallarga obuna bo'lmadingiz. Iltimos, quyidagi kanallarga obuna bo'ling
</b>
"""

KOD_IS_NOT = \
"""
<b>
❌ Siz mavjud bo'lmagan kodni yubordingiz!
</b>
"""

def MOVIES_SEND(**kwargs):
    movies_send = ""

    movies_send += f"<b>🎬 Nomi: #{kwargs['title']}</b>\n\n"
    movies_send += f"<b>📅 Yili: {kwargs['year']}</b>\n"
    movies_send += f"<b>🌐 Tili: {kwargs['language']}</b>\n"
    movies_send += f"<b>📀 sifati: {kwargs['quality']}</b>\n"
    movies_send += f"<b>🏳️ Davlati: {kwargs['country']}</b>\n"
    movies_send += f"<b>🎭 Janri: {kwargs['genre']}</b>\n"
    movies_send += f"<b>📥 Yuklash: <a href='https://t.me/TVkino_uzbot'>{kwargs['download_count']}</a></b>\n\n"
    movies_send += f"<b>🤖 Bizning bot:  @TVkino_uzbot</b>\n"


    return movies_send

def MOVIES_LIST_SEND(title, code):
    return f"<b>🎬 [{title}] -- kod: ({code})</b>\n\n"

MOVIES_SEARCH = \
"""
<b>
✍🏻 Iltimos, qidiruv so'rovini kiriting:
</b>
"""

SEARCH_NOT_FOUND = \
"""
<b>
Afsuski hech narsa topilmadi 😔
</b>
"""

CATEGORY_SELECT = \
"""
<b>Kategoriyani tanlang:</b>
"""

CATEGORY_ERROR = \
"""
<b>Kategoriyalar topilmadi.</b>
"""

CATEGORY_MOVIES = \
"""
<b>kategoriyasidagi filmlar:</b>
"""

CATEGORY_NOT_MOVIES  = \
"""
<b>kategoriyasida filmlar topilmadi. 😔</b>
"""
