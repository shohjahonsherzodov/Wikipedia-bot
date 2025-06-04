from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
import wikipedia
import asyncio
wikipedia.set_lang("uz")
API_TOKEN="7931954185:AAGdVaLL14iMkE0I7pZY1HR6egEpcmfU5RQ"
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"Salom {hbold(message.from_user.first_name)} men wikipediani izlab sizga\nkerakli ma'lumotlarni topib beraman🔎🔎🔎"
    )
@dp.message(Command("admin"))
async def admin_panel(message: Message):
    await message.answer(
        f"<a href='https://t.me/shohjahon2011_blog'>@shohjahon2011_blog (lichkaga yozish)</a>",
        parse_mode="HTML"
    )
@dp.message()
async def wiki_handler(message: Message):
    """Foydalanuvchi kiritgan matnni wikipediadan izlab topib beruvchi funksiya"""
    qidiruv = message.text
    try:
        result = wikipedia.summary(qidiruv)  # Wikipedia'dan qisqacha matn
        await message.answer(result)

    except wikipedia.exceptions.DisambiguationError as e:
        # Bir nechta ma'noli maqolalar topilsa
        variants = "\n".join(e.options[:5])
        await message.answer(
            f"Bu so‘z bir nechta ma'noga ega:\n{variants}\n\n"
            "Iltimos, mavzuni aniqroq yozing. 🔍"
        )

    except wikipedia.exceptions.PageError:
        # Maqola topilmasa
        await message.answer("Kechirasiz, bu mavzu bo‘yicha hech narsa topilmadi. ❌")

    except Exception as err:
        # Kutilmagan xatoliklar
        await message.answer(f"Xatolik yuz berdi: {err}")

async def main():
    """
    Botni ishga tushiruvchi asosiy funksiya
    """
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)
if __name__ == "__main__":  
    asyncio.run(main())