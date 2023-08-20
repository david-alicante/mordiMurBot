from datetime import datetime
from zoneinfo import ZoneInfo


admin_chat_id = 7551427
bot = None


def logger(*args):
    timestamp = datetime.now(tz=ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d %H:%M:%S")
    args = (f"{timestamp} | ",) + args
    print(args)
    log = ""
    for arg in args:
        if type(arg) == str:
            log += arg
        else:
            log += str(arg)
        log += " "
    log = log.strip()
    bot.send_message(admin_chat_id, log)


def info(text):
    text = f"[INFO] - {text}"
    logger(text)


def warning(text):
    text = f"[WARNING] - {text}"
    logger(text)


def error(text):
    text = f"[ERROR] - {text}"
    logger(text)

