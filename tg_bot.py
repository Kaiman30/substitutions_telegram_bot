from parsing import parse_table, parse_day, parse_practice, parse_duty
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
    with open("subs.txt", "r") as file:
        subs = file.readlines()
        new_subs = [item.strip() for item in subs]     
    # Создаем пустой список, в котором будут храниться все списки по 4 элемента
    result = []

    # Разделяем исходный список на списки по 5 элементов
    for i in range(0, len(new_subs), 5):
        sublist = new_subs[i:i+5]
        result.append(sublist)
    
    return resultimport
    

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
    await message.answer(f"<b>{parse_day()}</b>")


@dp.message()
async def sendsubs(message: Message):
    """Отправка замен"""
    if message.text.islower():
        await message.answer("Неверный формат группы");
        
    else:
        groupnumber = message.text
        foundsubs = False
        result = work_with_subs()
        
        for sublist in result:
            if sublist[0] == groupnumber:
                foundsubs = True
                subsinfo = f"<b>{parse_day()}</b>\nдля группы <b>{sublist[0]}:</b>\n\n{sublist[1]}\n{sublist[2]}\n{sublist[3]}\n{sublist[4]}"
                await message.answer(subsinfo)
                
        if not foundsubs:
            await message.answer("Замен на эту группу нет")


async def update_subs_periodically():
    while True:
        work_with_subs()
        print(f"Замены успешно обновлены! текущий день: {parse_day()}")
        await asyncio.sleep(900)


async def main():
    """Старт бота"""
    await bot.delete_webhook(drop_pending_updates=True) # Скипает обновления
    await dp.start_polling(bot)

    asyncio.create_task(update_subs_periodically())
    
    
if __name__ == "__main__":
    asyncio.run(main())