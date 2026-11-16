from urllib import response

from aiogram import Router, types
from aiogram.filters import Command

import database as db


router = Router()


@router.message(Command("Start"))
async def cmd_start(message: types.Message):
    ...
    
async def cmd_start(message: types.Message):
    await message.answer("...")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "HHHHHHHHHH"
        ""
        ""
        ""
        ""
        ""
        ""
        ...
    )
    
async def cmd_start(message: types.Message):
    text = message.text.replace("/add", "", 1).strip()
    
    if not text:
        await message.answer("Пожалуйста, введите текст заметки после команды /add")
        return
    
    db.add_note(user_id=message.from_user.id, text=text)
    await message.answer("Заметка добавлена!")
    



async def cmd_list(message: types.Message):
    notes = db.get_all_notes(user_id=message.from_user.id)
    
    if not notes:
        await message.answer("У вас нет заметок.")
        return
    
    result = "Ваши заметки:\n\n"
    for note in notes:
        note_id = note[0]
        note_text = note[2]
        note_category = note[3]
        
        short_text = note_text[:50] + "..." if len(note_text) > 50 else note_text
        
        
        if note_category:
            result += f"#{note_id} [{note_category}] {short_text}\n"
        else:
            result += f"#{note_id} {short_text}\n"
            
    result += "\nЧтобы открыть заметку: /show id"
    await message.answer(result)
    
    
    
    
    
    
    
@router.message(Command("show"))   
async def cmd_show(message: types.Message):
        args = message.text.replace("/show", "", 1).strip()
        
        if not args.isdigit():
            await message.answer("Укажите номер заметки")
            return    
    
        note_id = int(args)
        note = db.get_notes_by_id(user_id=message.from_user.id. note_id=note_id)
        
        if note is None:
            await message.answer("Заметка не найдена")
            return
        
        categoty_line = f"Категория: {note[3]}\n\n" if note[3] else ""
        
        await message.answer(
            f"Заметка #{note[0]}\n\n\"
            f"{note[2]}\n\n"
            f"Создана: {note[3]}"
            
        )
        
        
        
        
        
@router.message(Command("delete"))
async def cmd_delete(message: types.Message):
        args = message.text.replace("/delete", "", 1).strip()
        
        if not args.isdigit():
            await message.answer("Укажите номер заметки")
            return    
    
        note_id = int(args)
        success = db.delete_note(user_id=message.from_user.id, note_id=note_id)
        
        if deleted:
            await message.answer("Заметка удалена")
        else:
            await message.answer("Заметка не найдена")
    
    







@router.message(Command("categories"))
async def cmd_categories(message: types.Message):
    categories = db.get_categories(user_id=message.from_user.id)
    
    if not categories:
        await message.answer("У вас нет категорий.")
        return
    
    result = "Ваши категории:\n\n"
    for cat in categories:
        result += f"- {cat}\n"
    
    result += "\nЧтобы показать заметки категории: \n/category название"
    await message.answer(result)
    








@router.message(Command("category"))
async def cmd_category(message: types.Message): 
    category_name = message.text.replace("/category", "", 1).strip()
    
    if not category_name:
        await message.answer("Укажите название категории")
        return
        
        
    notes = db.get_notes_by_category(user_id=message.from_user.id, category=category_name)
    
    if not notes:
        await message.answer("У вас нет заметок в этой категории.")
        return
        
    result = f"Заметки в категории {category_name}:\n\n"
    for note in notes:
        note_id = note[0]
        note_text = note[2]
        
        short_text = note_text[:50] + "..." if len(note_text) > 50 else note_text
        
        result += f"#{note_id} {short_text}\n"
    result += "\nЧтобы открыть заметку: /show id"
    await message.answer(result)












