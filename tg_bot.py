from parsing import parse_table, parse_day, parse_practice
import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message


#Инициализация переменных
TOKEN = "6428011950:AAHFDpileIsy7fVH12_nwl0vcgCcZLtW85E"
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()


def work_with_subs():
    """Работа с заменами"""
    parse_table()
    parse_day()
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
    await message.answer(f"Привет! \n<b>Я</b> - бот, написанный @qqwln, по всем вопросам, пиши ему.\nЧтобы получше узнать мой функционал, пиши /help")
    

@dp.message(Command("help"))
async def help(message: Message):
    """Команда /help"""
    await message.answer("Для того, чтобы получить замены на свою группу, напиши номер своей группы с буквами. \nНапример: <b>323С, 341Кп.</b>\n\nТакже можно узнать какие группы сейчас на практике - /practice")


@dp.message(Command("practice"))
async def practice(message: Message):
    """Команда /practice"""
    await message.answer(f"На практике сейчас: {parse_practice().replace('– практика', '')}")


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
                subsinfo = f"{parse_day()}\nдля группы {sublist[0]}:\n\n{sublist[1]}\n{sublist[2]}\n{sublist[3]}\n{sublist[4]}"
                await message.answer(subsinfo)
                
        if not foundsubs:
            await message.answer("Замен на эту группу нет")


async def main():
    """Старт бота"""
    await bot.delete_webhook(drop_pending_updates=True) # Скипает обновления
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())