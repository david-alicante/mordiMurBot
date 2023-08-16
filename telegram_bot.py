import requests
import json
import os


class TelegramBot:
    def __init__(self):
        self.__token = os.environ["TELEGRAM_API_TOKEN"]
        self.__api_url = os.environ["TELEGRAM_API_URL"]

    def get_me(self):
        url = f"{self.__api_url}{self.__token}/getMe"
        res = requests.get(url)
        return json.loads(res.text)

    def send_message(self, chat_id, text, parse_mode="HTML"):
        url = f"{self.__api_url}{self.__token}/sendMessage"
        data = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
        res = requests.post(url, data)
        return json.loads(res.text)

    def send_photo(self, chat_id, photo, caption=""):
        url = f"{self.__api_url}{self.__token}/sendPhoto"
        data = {"chat_id": chat_id, "caption": caption}
        files = {"photo": photo}
        res = requests.post(url, data, files=files)
        return json.loads(res.text)

    def send_photo_url(self, chat_id, photo_url, caption=""):
        url = f"{self.__api_url}{self.__token}/sendPhoto"
        data = {"chat_id": chat_id, "caption": caption, "photo": photo_url}
        res = requests.post(url, data)
        return json.loads(res.text)

    def send_video(self, chat_id, video, caption=""):
        url = f"{self.__api_url}{self.__token}/sendVideo"
        data = {"chat_id": chat_id, "caption": caption}
        files = {"video": video}
        res = requests.post(url, data, files=files)
        return json.loads(res.text)

    def send_video_url(self, chat_id, video_url, caption=""):
        url = f"{self.__api_url}{self.__token}/sendVideo"
        data = {"chat_id": chat_id, "caption": caption, "video": video_url}
        res = requests.post(url, data)
        return json.loads(res.text)

    def get_updates(self, chat_id):
        url = f"{self.__api_url}{self.__token}/getUpdates"
        data = {"chat_id": chat_id}
        res = requests.post(url, data)
        return json.loads(res.text)

    def ban_chat_member(self, chat_id, user_id):
        url = f"{self.__api_url}{self.__token}/banChatMember"
        data = {"chat_id": chat_id, "user_id": user_id}
        res = requests.post(url, data)
        return json.loads(res.text)

