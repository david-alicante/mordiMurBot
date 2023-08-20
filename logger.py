from datetime import datetime
from zoneinfo import ZoneInfo


admin_chat_id = 7551427
bot = None


def logger(*args):
    timestamp = datetime.now(tz=ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d %H:%M:%S")
    args = (f"{timestamp} |",) + args
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


def info(*args):
    args = ("[INFO] -",) + args
    logger(args)


def warning(*args):
    args = ("[INFO] -",) + args
    logger(args)


def error(*args):
    args = ("[INFO] -",) + args
    logger(args)

