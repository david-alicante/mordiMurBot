# importing google_images_download module
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords": "churros",
             "limit": 100,
             "print_urls": True,
             "chromedriver": "C:\\Users\\rdort\\Downloads\\chromedriver_win64\\chromedriver.exe"}

paths = response.download(arguments)

print(paths)

