import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

API_TOKEN = "7714281959:AAHTSmm_LhYs7ZlZ6FybXq3gE14DdVq8cMQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Пути к файлам
VIDEO_PATH = "/Users/egor/pos/kru"
VIDEO_1 = f"{VIDEO_PATH}/video1.mp4"
VIDEO_2 = f"{VIDEO_PATH}/video2.mp4"
VIDEO_3 = f"{VIDEO_PATH}/video3.mp4"
IMAGE_CLUB = f"{VIDEO_PATH}/club.png"

# Сообщения
MESSAGE_1 = (
    "Настало время узнать правду, возможно, горькую, но правду.<br><br>"
    "Перед тем, как ты прочтешь статью, постарайся настроиться на то, чтобы быть не предвзятой, а рассматривать ситуацию с нескольких сторон.<br><br>"
    "Представь, что ты стоишь недалеко от вашей пары и спокойно наблюдаешь за развитием событий.<br><br>"
    "Представила?<br><br>"
    "Тогда ты готова читать статью.<br><br>"
    '<a href="https://teletype.in/@taro_venger/681h3YQO3Cg">Читать статью</a>'
)

bot.send_message(chat_id, MESSAGE_1, parse_mode="HTML")

MESSAGE_2 = (
    "В клубе тебя ждет не только расклады таро и поддерживающее окружение, но и полный доступ ко всем возможностям моего авторского бота с метафорическими картами.\n\n"
    "Что такое метафорические карты и как с ними работать ты узнаешь внутри.\n\n"
    "Также с помощью бота ты можешь ответить на многие свои вопросы касаемо твоих отношений.\n\n"
    "С помощью карт ты можешь вытащить всю правду из своего подсознания.\n\n"
    "Предлагаю тебе познакомится с ним прямо сейчас. @YourMetaphorical_Bot"
)

MESSAGE_3 = "Чтобы вступить в клуб, переходи сюда:"
JOIN_BUTTON = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ВСТУПИТЬ", url="https://t.me/+QUlp1i600mVlZjhi")]
])

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    
    try:
        # Отправка первого кружка
        await bot.send_video_note(chat_id, FSInputFile(VIDEO_1))
        await asyncio.sleep(30)
        
        # Отправка первого сообщения
        await message.answer(MESSAGE_1)
        await asyncio.sleep(120)
        
        # Отправка второго кружка
        await bot.send_video_note(chat_id, FSInputFile(VIDEO_2))
        await asyncio.sleep(30)
        
        # Отправка второго сообщения
        await message.answer(MESSAGE_2)
        await asyncio.sleep(120)
        
        # Отправка третьего кружка
        await bot.send_video_note(chat_id, FSInputFile(VIDEO_3))
        await asyncio.sleep(30)
        
        # Отправка изображения клуба
        await asyncio.sleep(60)
        await bot.send_photo(chat_id, FSInputFile(IMAGE_CLUB), caption=MESSAGE_3, reply_markup=JOIN_BUTTON)
        
        # Отправка финального сообщения с кнопкой
        await message.answer(MESSAGE_3, reply_markup=JOIN_BUTTON)
    
    except Exception as e:
        await message.answer("Ошибка отправки файлов. Проверь путь к файлам.")
        print(f"Ошибка: {e}")

async def main():
    dp = Dispatcher()
    dp.message.register(send_welcome)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
