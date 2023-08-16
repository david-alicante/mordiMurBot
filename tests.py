from dotenv import load_dotenv

import pole

load_dotenv()
import photos
import json
import messages

#messages.cats(7551427)
#messages.dogs(7551427)
#messages.coffee(7551427)


pole.message("1234", "mañanera", "5678", "pepito", "oro")
print(pole.pole_score)

