from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dishka import FromDishka

from services.api_gateway import ApiGateway

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
async def on_start(
        message: Message,
):
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
async def show_users(
        message: Message,
        api_gateway: FromDishka[ApiGateway],
):
    vacancies_page = await api_gateway.get_pending_vacancies()
    lines: list[str] = ['Новые вакансии:']
    for vacancy in vacancies_page.vacancies:
        lines.append(vacancy.title)
    await message.answer('\n'.join(lines))


@router.message(
    F.text
)
async def echo_message(message: Message):
    await message.answer(f"Ты написал: {message.text}")
