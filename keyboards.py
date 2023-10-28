from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Помощь")
        ],
        [
            KeyboardButton(text="Практика"),
            KeyboardButton(text="Дежурство")
        ],
        [
            KeyboardButton(text="День замен"),
            KeyboardButton(text="Контакты")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)