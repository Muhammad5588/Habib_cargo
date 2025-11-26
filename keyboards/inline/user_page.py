from aiogram.utils.keyboard import InlineKeyboardBuilder

back = InlineKeyboardBuilder()
back.button(text = "Orqaga ↪", callback_data = "back")


def edit_keyboard(user_id: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Ismni tahrirlash 📝", callback_data=f"edit_name:{user_id}")
    keyboard.button(text="Telefon tahrirlash 📝", callback_data=f"edit_phone:{user_id}")
    keyboard.button(text="Passport tahrirlash 📝", callback_data=f"edit_passport_number:{user_id}")
    keyboard.button(text="Tug'ilgan sanani tahrirlash 📝", callback_data=f"edit_birthdate:{user_id}")
    keyboard.button(text="PINFL tahrirlash 📝", callback_data=f"edit_pinfl:{user_id}")
    keyboard.button(text="Manzil tahrirlash 📝", callback_data=f"edit_address:{user_id}")
    keyboard.button(text="Orqaga ↪", callback_data=f"back:{user_id}")
    keyboard.adjust(1, 1)
    return keyboard

def delete_keyboard(user_id: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Ha ❌", callback_data=f"confirm_delete:{user_id}")
    keyboard.button(text="Yo'q ↪", callback_data=f"back:{user_id}")
    keyboard.adjust(1, 1)
    return keyboard







