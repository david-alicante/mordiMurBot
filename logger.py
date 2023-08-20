import datetime


def logger(text):
    timestamp = datetime.now.strftime("%Y-%m-%d %H:%M:%S")
    print("{} | {}\n".format(timestamp, text))


def info(text):
    text = f"[INFO] - {text}"
    logger(text)


def warning(text):
    text = f"[WARNING] - {text}"
    logger(text)


def error(text):
    text = f"[ERROR] - {text}"
    logger(text)

