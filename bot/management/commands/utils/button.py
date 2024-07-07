from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def get_subscription_buttons(not_subscribed):
    buttons = [InlineKeyboardButton(text=f"{idx+1}-kanal", url=f"https://t.me/{channel}") for idx, channel in enumerate(not_subscribed)]
    buttons.append(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check_subscriptions"))
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def delete_message():
    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(
        InlineKeyboardButton(text="❌", callback_data="delete")
    )
    return buttons



def create_movie_buttons():
    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(
        InlineKeyboardButton(text="♻️ Do'stlarga ulashish", switch_inline_query=""),
        InlineKeyboardButton(text="❌", callback_data="delete")
    )
    return buttons

DOWNLOAD_MOVIES = "⏳ Yuklab olish"
SEARCH = "🔍 Kinolarni Qidirish"
MY_MOVIES = "🍿 Mening kinolarim"
SETTINGS = "⚙️ So'zlamalar"
MOVIES_LIST = "📔 Kinolar Ro'yhati"





MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=DOWNLOAD_MOVIES)
        ],
        [
            KeyboardButton(text=SEARCH),
            KeyboardButton(text=MOVIES_LIST),
        ],
    ],
    resize_keyboard=True
)


BACK_TEXT = '⬅️ Ortga'


BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BACK_TEXT)
        ]
    ],
    resize_keyboard=True
)


do = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='test', callback_data='down_')
        ],
    ],
)