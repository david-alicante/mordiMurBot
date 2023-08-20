from datetime import datetime


admin_chat_id = 7551427
bot = None


def logger(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = "{} | {}\n".format(timestamp, text)
    print(log)
    bot.send_message(admin_chat_id, admin_chat_id, log)


def info(text):
    text = f"[INFO] - {text}"
    logger(text)


def warning(text):
    text = f"[WARNING] - {text}"
    logger(text)


def error(text):
    text = f"[ERROR] - {text}"
    logger(text)

