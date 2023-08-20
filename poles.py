from datetime import datetime
from zoneinfo import ZoneInfo
import consts
import logger

pole_types = consts.pole_types
pole_score = {}


def message(chat_id, chat_type, user_id, user, norm_text):
    if chat_type == "group" or chat_type == "supergroup":
        now = datetime.now(tz=ZoneInfo("Europe/Madrid"))
        pole_type = None
        for key in pole_types.keys():
            if now.hour == pole_types[key]["hour"] and now.minute == pole_types[key]["minutes"]:
                pole_type = key

        mes = "Ach@, ¿Qué pole ni que pola?"
        if pole_type is not None:
            mes = pole(chat_id, user_id, user, norm_text, pole_type)
    else:
        mes = "Las poles solo funcionan en grupos y supergrupos"
    return mes


def pole(chat_id, user_id, user, norm_text, pole_type):
    premio = None
    if norm_text == "pole" or norm_text == "oro" and chat_id not in pole_score:
        pole_score[chat_id] = {"pole_type": pole_type, "oro": user_id}
        premio = "el oro"
    elif norm_text == "subpole" or norm_text == "plata" and chat_id in pole_score \
            and "plata" not in pole_score[chat_id] \
            and user_id != pole_score["chat_id"]["oro"]:
        pole_score[chat_id]["plata"] = user_id
        premio = "la plata"
    elif norm_text == "fail" or norm_text == "bronce" and chat_id in pole_score \
            and "plata" in pole_score[chat_id] \
            and "bronce" not in pole_score[chat_id] \
            and user_id != pole_score["chat_id"]["oro"] \
            and user_id != pole_score["chat_id"]["plata"]:
        pole_score[chat_id]["bronce"] = user_id
        premio = "el bronce"
    mes = None
    if premio is not None:
        mes = f"El usuario {user} ha conseguido {premio}"
    else:
        mes = "Sin resultado en pole"
    logger.info(mes + "pole_score: " + str(pole_score))
    return mes
