from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from database import add_expense, get_today_expenses

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Salom! Men yuk mashina haydovchilariga yordam beruvchi botman. 🚚\n\nXarajat qo'shish uchun masalan: \"solarkaga 1500 rubl quydim\" deb yozing.")

@router.message(F.text)
async def handle_expense(message: Message):
    text = message.text.lower()
    user_id = message.from_user.id
    
    if "solarka" in text or "dizel" in text:
        # Simple parsing logic (can be improved with NLP)
        await message.answer("✅ Tushundim. Yoqilg'i kategoriyasiga qo'shaylikmi? Miqdor va valyutani tasdiqlang.")
        # In real version, parse amount and currency
    else:
        await message.answer("Tushundim, lekin hozircha xarajat qo'shish funksiyasi faol. \"solarkaga 1000 rubl\" deb sinab ko'ring.")


def register_handlers(dp):
    dp.include_router(router)