import types

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dishka import FromDishka
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from typing import Optional
from aiogram.filters.callback_data import CallbackData

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


@router.message(F.text == "💼 Новые вакансии")
async def cmd_inline_url(
        message: Message,
        api_gateway: FromDishka[ApiGateway],
):
    builder = InlineKeyboardBuilder()
    vacancies_page = await api_gateway.get_pending_vacancies()

    if not vacancies_page.vacancies:
        await message.answer("Нет новых вакансий")
        return

    for vacancy in vacancies_page.vacancies:
        builder.row(
            InlineKeyboardButton(
                text=vacancy.title,
                callback_data=VacancyCallbackFactory(
                    vacancy_id=vacancy.id
                ).pack()
            ),

        )

    await message.answer("Выберите действие по вакансиям:", reply_markup=builder.as_markup())


class VacancyCallbackFactory(CallbackData, prefix="vacancy-show"):
    vacancy_id: int


class VacancyApproveCallbackFactory(CallbackData, prefix="vacancy-approve"):
    vacancy_id: int


class VacancyRejectCallbackFactory(CallbackData, prefix="vacancy-reject"):
    vacancy_id: int


@router.callback_query(VacancyCallbackFactory.filter())
async def process_vacancy_action(
        callback: CallbackQuery,
        callback_data: VacancyCallbackFactory,
        api_gateway: FromDishka[ApiGateway],
):
    vacancy_id = callback_data.vacancy_id
    vacancy = await api_gateway.get_vacancy_by_id(vacancy_id)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(
            text='✅ Одобрить',
            callback_data=VacancyApproveCallbackFactory(
                vacancy_id=vacancy.id
            ).pack()
        ),
        InlineKeyboardButton(
            text='❌ Отклонить',
            callback_data=VacancyRejectCallbackFactory(
                vacancy_id=vacancy.id
            ).pack()
        ),
    )
    await callback.message.answer(
        f'{vacancy.title}\n'
        f'{vacancy.description[:100]}...\n'
        f'{vacancy.organization_name}',
        reply_markup=keyboard.as_markup()
    )
