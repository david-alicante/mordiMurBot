import time


bold = "\033[1m"
reset = "\033[0m"


def logger(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print("{} | {}\n".format(timestamp, text))


def info(text):
    text = f"[{bold}{fore(0, 255, 0)}[INFO]{reset} - {text}"
    logger(text)


def warning(text):
    text = f"[{bold}{fore(255, 140, 0)}[WARN]{reset} - {text}"
    logger(text)


def error(text):
    text = f"[{bold}{fore(255, 0, 0)}[ERROR]{reset} - {text}"
    logger(text)


def fore(r, g, b):
    return "\033[38;2;%d;%d;%dm" % (r, g, b)
