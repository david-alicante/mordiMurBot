from datetime import datetime
from zoneinfo import ZoneInfo
import time
import sys
import consts

pole_types = consts.pole_types
pole_score = {}


def logger(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    sys.stdout.write("{} | {}\n".format(timestamp, text))


def message(chat_id, chat_type, user_id, user, norm_text):
    if chat_type == "group" or chat_type == "supergroup":
        now = datetime.now(tz=ZoneInfo("Europe/Madrid"))
        print(now)
        pole_type = None
        for key in pole_types.keys():
            if now.hour == pole_types[key]["hour"] and now.minute == pole_types[key]["minutes"]:
                pole_type = key

        mes = "Ach@, ¿Qué pole ni que pola? " + str(now)
        if pole_type is not None:
            mes = pole(chat_id, user_id, user, norm_text, pole_type)
    else:
        mes = "Las poles solo funcionan en grupos y supergrupos"
    return mes


def pole(chat_id, user_id, user, norm_text, pole_type):
    premio = None
    if chat_id not in pole_score:
        if norm_text == "pole" or norm_text == "oro":
            pole_score[chat_id] = {pole_type: {"oro": {"user_id": user_id}}}
            premio = "el oro"
    else:
        if norm_text == "subpole" or norm_text == "plata" and "plata" not in pole_score[chat_id][pole_type]:
            pole_score[chat_id][pole_type]["plata"] = {"user_id": user_id}
            premio = "la plata"
        elif norm_text == "fail" or norm_text == "bronce" and "bronce" not in pole_score[chat_id][pole_type]:
            pole_score[chat_id][pole_type]["bronce"] = {"user_id": user_id}
            premio = "el bronce"
    mes = None
    if premio is not None:
        mes = f"El usuario {user} ha conseguido {premio}"
    logger(pole_score)
    return mes
