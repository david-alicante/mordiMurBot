import requests
import os
import random
import json


def get_cats(is_gif):
    url = "https://cataas.com/cat"
    if is_gif:
        url += "/gif"
    cat_res = requests.get(url)
    if cat_res.status_code == 200:
        return cat_res.content


def get_dogs():
    url = "https://random.dog/woof.json"
    dog_res = requests.get(url)
    if dog_res.status_code == 200:
        dog_url = json.loads(dog_res.text)["url"]
        ext = dog_url.split(".")[-1]
        if ext == "mp4" or ext == "gif":
            return True, dog_url
        else:
            return False, dog_url

def get_coffee():
    url = "https://coffee.alexflipnote.dev/random"
    coffee_res = requests.get(url)
    if coffee_res.status_code == 200:
        return coffee_res.content

def get_pixabay(q):
    url = "https://pixabay.com/api"
    data = {"key": os.environ["PIXABAY_KEY"], "q": q, "image_type": "photo"}
    res = requests.get(url, data)
    if res.status_code == 200:
        pages = json.loads(res.text)["totalHits"] / 20
        if pages.is_integer():
            page = random.randint(1, pages)
        else:
            pages = int(pages) + 1
            page = random.randint(1, pages)
        data["page"] = page
        res = requests.get(url, data)
        hits = json.loads(res.text)["hits"]
        hit_num = random.randint(0, len(hits) - 1)
        return hits[hit_num]["webformatURL"]


def get_churros():
    churros_dir = "./imgs/churros"
    file_name = random.choice(os.listdir(churros_dir))
    return open(f"{churros_dir}/{file_name}", "rb")

