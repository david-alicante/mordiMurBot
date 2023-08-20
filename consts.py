TELEGRAM_API_URL = "https://api.telegram.org/bot"



START = """
Bot para el canal de La Mordaza Social
Si quieres saber que acciones puedes realizar, escribe /help, /ayuda o /aiura 😅
"""

AYUDA = """
📄LISTADO DE COMANDOS📄
    
◼Ayuda (este mensaje)
▫/help o /ayuda o /aiura
        
◼Saludos:
▫hola
▫buenos días
▫buenas tardes
▫buenas noches
    
◼Fotos:
▫gatos  - Imagen random de gatos
▫gatos gif  - Gif random de gatos
▫perros  - Imagen o gif random de perros
▫brocoli  - Imagen random de brocoli
▫churros  - Imagen random de churros
▫cafe  - Imagen random de café
    
◼Juegos:
▫elige  - Elige entre varias opciones separadas por o
Ejemplo: Elige carne o pescado o verduras o setas 
▫click  - Juego de la ruleta rusa, si pierdes y el bot es admin serás baneado 
"""

ELIGE_LIST = ["Evidentemente", "Por supuesto", "Sin duda", "Naturalmente"]


pole_types = {
    "pole": {"hour": 0, "minutes": 0},
    "pole canaria": {"hour": 1, "minutes": 0},
    "pole mañanera": {"hour": 7, "minutes": 0},
    "pole andaluza": {"hour": 12, "minutes": 0},
    "pole patitos": {"hour": 22, "minutes": 22},
    "pole prueba": {"hour": 10, "minutes": 32},

}

