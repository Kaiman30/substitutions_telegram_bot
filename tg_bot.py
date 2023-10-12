from parsing import (parse_table, 
                     parse_day, 
                     parse_practice, 
                     parse_duty,
                     parse_modifyDate)
import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
import asyncio
import keyboards


# Инициализация переменных
TOKEN = "6428011950:AAHFDpileIsy7fVH12_nwl0vcgCcZLtW85E"
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()


def work_with_subs():
    """Работа с заменами"""
    parse_table()
    parse_day()
    parse_duty()
    parse_practice()
    parse_modifyDate()
    with open("subs.txt", "r") as file:
        subs = file.readlines()
        new_subs = [item.strip() for item in subs]     
    # Создаем пустой список, в котором будут храниться все списки по 4 элемента
    result = []

    # Разделяем исходный список на списки по 5 элементов
    for i in range(0, len(new_subs), 5):
        sublist = new_subs[i:i+5]
        result.append(sublist)
    
    return result
    

@dp.message(Command("start"))
async def start(message: Message):
    """Команда /start"""
    await message.answer(f'Привет! \n<b>Я</b> - бот, написанный @qqwln, по всем вопросам, пиши ему.\nЧтобы получше узнать мой функционал, пиши "Помощь"\nДля твоего удобства я вывел клавиатуру',
                         reply_markup=keyboards.main_kb)


@dp.message(F.text.lower() == "помощь")
async def help(message: Message):
    """Команда /help"""
    await message.answer("Для того, чтобы получить замены на свою группу, напиши номер своей группы. \nНапример: <b>323С, 341Кп.</b>\n\nТакже доступен другой функционал, который выписан в клавиатуре")


@dp.message(F.text.lower() == "практика")
async def practice(message: Message):
    """Команда /practice"""
    await message.answer(f"На практике сейчас: <b>{parse_practice().replace('– практика', '')}</b>")
    

@dp.message(F.text.lower() == "дежурство")
async def duty(message: Message):
    """Команда /duty"""
    await message.answer(f"На дежурстве сейчас: <b>{parse_duty().replace('- дежурная', '')}</b>")


@dp.message(F.text.lower() == "контакты")
async def contacts(message: Message):
    """Команда /contacts"""
    await message.answer("Мои контакты:\ntg: @qqwln\nvk: https://vk.com/garem_05\nКанал о разработке: @qqwlndev")


@dp.message(F.text.lower() == "день замен")
async def day(message: Message):
    """Команда /day"""
    await message.answer(f"<b>{parse_day()}</b>\n\n{parse_modifyDate().strip()}")


################ На будущее для бесед
# @dp.message(Command("sendsubs"))
# async def send_subs(message: Message):
#     """Команда /sendsubs"""
#     try:
#         groupnumber = message.text.split()[1]
#     except IndexError:
#         await message.answer("Please provide a group number.")
#         return

#     if groupnumber is None:
#         await message.answer("Invalid group number.")
#         return

#     groupnumber_lower = groupnumber.lower()

#     if sublist is not None and sublist[0] is not None and sublist[0].lower() == groupnumber_lower:
#         # Send substitutions
#         substitutions = get_substitutions(groupnumber_lower)
#         await message.answer(substitutions)
#     else:
#         await message.answer("Invalid group number.")

# def get_substitutions(groupnumber):

#     return "Substitutions for the group."


@dp.message()
async def sendsubs(message: Message):
    """Отправка замен"""
    groupnumber = message.text # получаем номер группы от пользователя
    foundsubs = False
    result = work_with_subs()
    
    if groupnumber is None:
        await message.answer("Укажите номер группы")
        return
    lower_groupnumber = groupnumber.lower()
    
    for sublist in result:
        if sublist is not None and sublist[0] is not None and sublist[0].lower() == lower_groupnumber:
            foundsubs = True
            subsinfo = f"<b>{parse_day()}</b>\nдля группы <b>{sublist[0]}:</b>\n\n{sublist[1]}\n{sublist[2]}\n{sublist[3]}\n{sublist[4]}"
            await message.answer(subsinfo)
                
    if not foundsubs:
        await message.answer("Замен на эту группу нет")


async def update_subs_periodically():
    """Обновление замен каждые 15 минут"""
    while True:
        work_with_subs()
        print(f"Замены успешно обновлены! текущий день: {parse_day()}")
        await asyncio.sleep(900)


async def main():
    asyncio.create_task(update_subs_periodically()) # Обновление замен при запуске
    """Старт бота"""
    await bot.delete_webhook(drop_pending_updates=True) # Скипает обновления
    await dp.start_polling(bot)

    
    
    
if __name__ == "__main__":
    asyncio.run(main())