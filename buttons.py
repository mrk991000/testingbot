from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BUTTONS_ALL = [
    ("Choose AI Model", "model_choice"),
    ("Image Settings", "pic_setup"),
    ("Actions with context", "context_work"),
    ("Voice replies", "voice_answer_work"),
    ("System role", "system_value_work"),
    ("Info", "info"),
]

inline_buttons = [
    InlineKeyboardButton(text=text, callback_data=data) for text, data in BUTTONS_ALL
]

keyboard = InlineKeyboardMarkup(inline_keyboard=[[button] for button in inline_buttons])

pic_buttons = [
    ("SD", "set_sd"),
    ("HD", "set_hd"),
    ("1024x1024", "set_1024x1024"),
    ("1024x1792", "set_1024x1792"),
    ("1792x1024", "set_1792x1024"),
    ("Back to menu", "back_menu"),
]

inline_buttons_pic = [
    InlineKeyboardButton(text=text, callback_data=data) for text, data in pic_buttons
]

keyboard_pic = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in inline_buttons_pic]
)

BUTTONS_MODEL = [
    ("4o mini", "gpt_4o_mini"),
    ("4o", "gpt_4_o"),
    ("o1 mini", "gpt_o1_mini"),
    ("o1 preview", "gpt_o1_preview"),
    ("o3 mini", "o3-mini"),
    ("DALL·E 3", "dall_e_3"),
    ("ASSISTANT", "assistant"),
    ("Back to menu", "back_menu"),
]

inline_buttons_model = [
    InlineKeyboardButton(text=text, callback_data=data) for text, data in BUTTONS_MODEL
]

keyboard_model = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in inline_buttons_model]
)

BUTTONS_CONTEXT = [
    ("Show context", "context"),
    ("Clear context", "clear"),
    ("Back to menu", "back_menu"),
]

inline_buttons_context = [
    InlineKeyboardButton(text=text, callback_data=data)
    for text, data in BUTTONS_CONTEXT
]

keyboard_context = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in inline_buttons_context]
)

BUTTONS_VOICE = [
    ("Enable audio response", "voice_answer_add"),
    ("Disable audio response", "voice_answer_del"),
    ("Back to menu", "back_menu"),
]

inline_buttons_voice = [
    InlineKeyboardButton(text=text, callback_data=data) for text, data in BUTTONS_VOICE
]

keyboard_voice = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in inline_buttons_voice]
)

BUTTONS_VALUE_WORK = [
    ("Assign a system role", "change_value"),
    ("Remove system role", "delete_value"),
    ("Back to menu", "back_menu"),
]

inline_buttons_value_work = [
    InlineKeyboardButton(text=text, callback_data=data)
    for text, data in BUTTONS_VALUE_WORK
]

keyboard_value_work = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in inline_buttons_value_work]
)
