import random
import json
import re
import consts
import photos
import poles
import logger
from unicodedata import normalize
from telegram_bot import TelegramBot

logger.bot = bot = TelegramBot()


def remove_diacritics(text):
    text = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", text), 0, re.I
    )
    return normalize('NFC', text.lower())


def message_received(message):
    if "text" not in message['message']:
        logger.info("NOT a chat message: " + json.dumps(message, indent=4, sort_keys=True))
    else:
        logger.info("A chat message: " + json.dumps(message, indent=4, sort_keys=True))
        chat_id = message['message']['chat']['id']
        chat_type = message['message']['chat']['type']
        text = message['message']['text']
        message_id = message['message']['message_id']
        user = f"@{message['message']['from']['username']}"
        user_id = message['message']['from']['id']
        norm_text = remove_diacritics(text)

        if norm_text == "/start":
            start(chat_id)
        elif norm_text == "/help" or text == "/ayuda" or text == "/aiura":
            ayuda(chat_id)
        elif norm_text == "hola":
            hola(chat_id, user)
        elif norm_text == "buenos dias":
            buenos_dias(chat_id, user)
        elif norm_text == "buenas tardes":
            buenas_tardes(chat_id, user)
        elif norm_text == "buenas noches":
            buenas_noches(chat_id, user)
        elif norm_text == "gatos":
            gatos(chat_id)
        elif norm_text == "gatos gif":
            gatos(chat_id, True)
        elif norm_text == "perros":
            perros(chat_id)
        elif norm_text == "brocoli":
            brocoli(chat_id)
        elif norm_text == "churros":
            churros(chat_id)
        elif norm_text == "cafe":
            cafe(chat_id)

        elif norm_text.startswith("elige"):
            elige(chat_id, text)
        elif norm_text == "click":
            click(chat_id, user_id)
        elif norm_text == "pole" or norm_text == "oro" \
                or norm_text == "subpole" or norm_text == "plata" \
                or norm_text == "fail" or norm_text == "bronce":
            pole(chat_id, chat_type, user_id, user, norm_text)


def start(chat_id):
    res = bot.send_message(chat_id, consts.START)
    logger.info(res)


def ayuda(chat_id):
    res = bot.send_message(chat_id, consts.AYUDA)
    logger.info(res)


def hola(chat_id, user):
    res = bot.send_message(chat_id, f"Hola, {user}, ¿qué tal estás?")
    logger.info(res)


def buenos_dias(chat_id, user):
    res = bot.send_message(chat_id, f"Buenos días, {user}, ¿has dormido bien?")
    logger.info(res)


def buenas_tardes(chat_id, user):
    res = bot.send_message(chat_id, f"Buenas tardes, {user}, ¿nos hacemos unas estrellas en la terracica 🍻?")
    logger.info(res)


def buenas_noches(chat_id, user):
    res = bot.send_message(chat_id, f"Buenas noches, {user}, descansa")
    logger.info(res)


def gatos(chat_id, is_gif=False):
    photo = photos.get_cats(is_gif)
    if photo is not None:
        if is_gif:
            res = bot.send_video(chat_id, photo)
        else:
            res = bot.send_photo(chat_id, photo)
    logger.info(res)


def perros(chat_id):
    is_video, file_url = photos.get_dogs()
    if file_url is not None:
        if is_video:
            res = bot.send_video_url(chat_id, file_url)
        else:
            res = bot.send_photo_url(chat_id, file_url)
    logger.info(res)


def cafe(chat_id):
    photo = photos.get_coffee()
    if photo is not None:
        res = bot.send_photo(chat_id, photo)
    logger.info(res)


def brocoli(chat_id):
    brocoli_url = photos.get_pixabay("broccoli")
    res = bot.send_photo_url(chat_id, brocoli_url)
    logger.info(res)


def churros(chat_id):
    photo = photos.get_churros()
    res = bot.send_photo(chat_id, photo)
    logger.info(res)


def elige(chat_id, text):
    first_word = text.split(" ")[0]
    text = text.replace(first_word, "")
    options = text.split(" o ")
    first_res = random.choice(consts.ELIGE_LIST)
    chosen = random.choice(options).strip()
    res = bot.send_message(chat_id, f"{first_res} {chosen}")
    logger.info(res)


def click(chat_id, user_id):
    num = random.randint(1, 6)
    if num != 1:
        bot.send_message(chat_id, "😅☁️🔫 click")
    else:
        bot.send_message(chat_id, "😵💥🔫 ¡BANG!")
        bot.ban_chat_member(chat_id, user_id)


def pole(chat_id, chat_type, user_id, user, norm_text):
    message = poles.message(chat_id, chat_type, user_id, user, norm_text)
    bot.send_message(chat_id, message)

