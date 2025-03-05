from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router(name='start_command_handler')

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👥 Пользователи")],
        [KeyboardButton(text="📅 Новые мероприятия"), KeyboardButton(text="💼 Новые вакансии")],
    ],
    resize_keyboard=True,
)

@router.message(
    F.text == '/start',
)
async def on_start(message: Message):
    await message.answer("Привет! Бот запущен.", reply_markup=main_menu)


@router.message(
    F.text == "👥 Пользователи",
)
async def show_users(message: Message):
    await message.answer("Ты нажал на `👥 Пользователи`")

@router.message(
    F.text == "📅 Новые мероприятия",
)
async def show_users(message: Message):
    await message.answer("Ты нажал на `📅 Новые мероприятия`")

@router.message(
    F.text == "💼 Новые вакансии",
)
async def show_users(message: Message):
    await message.answer("Ты нажал на `💼 Новые вакансии`")

@router.message(
    F.text
)
async def echo_message(message: Message):
    await message.answer(f"Ты написал: {message.text}")