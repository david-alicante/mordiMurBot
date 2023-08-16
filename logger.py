import time


# def logger(text):
#     timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
#     print("{} | {}\n".format(timestamp, text))

def logger(text):
    print(text)

def info(text):
    text = f"[INFO] - {text}"
    logger(text)


def warning(text):
    text = f"[WARNING] - {text}"
    logger(text)


def error(text):
    text = f"[ERROR] - {text}"
    logger(text)

