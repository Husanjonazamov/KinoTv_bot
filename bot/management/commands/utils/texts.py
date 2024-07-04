
MAIN_MENU = \
"""
Asosiy menyu
"""


START_USER = \
"""
<b>
👋 Assalomu alaykum. KinoTv botga xush kelibsiz!
</b>
"""


DOWNLOAD_MOVIES_HANDLER = \
"""
<i>
✍🏻 kino kodini yuboring!
</i>
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

    movies_send += f"🎬<b>Nomi: #{kwargs['title']}\n\n"
    movies_send += f"📅 Yili: {kwargs['year']}\n"
    movies_send += f"🌐 Tili: {kwargs['language']}\n"
    movies_send += f"📀 sifati: {kwargs['quality']}\n"
    movies_send += f"🏳️ Davlati: {kwargs['country']}\n"
    movies_send += f"🎭 Janri: {kwargs['genre']}</b>\n"

    return movies_send



def MOVIES_LIST_SEND(title, code):
    return f"<b>🎬 [{title}] -- kod: ({code}</b>)\n\n"


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
Kategoriyani tanlang:
"""

CATEGORY_ERROR = \
"""
Kategoriyalar topilmadi.
"""

CATEGORY_MOVIES = \
"""
kategoriyasidagi filmlar:
"""

CATEGORY_NOT_MOVIES  = \
"""
kategoriyasida filmlar topilmadi. 😔
"""