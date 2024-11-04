import os
from  dotenv import load_dotenv

#cargar las variables de entorno desde el archivo .env
load_dotenv ()

class config:

    #URL base de la API (PokéAPI) de Pokémon para obtener el nombre del pokémon
    POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")

    #URL de la API (PokéAPI) de Pokémon para obtener el tipo del pokémon
    POKEAPI_TYPE_URL = os.getenv("POKEAPI_TYPE_URL")

    #URL de la API (PokéAPI) de Pokémon para obtener el nombre más largo de un Pokémon de cierto tipo
    POKEAPI_LONGEST_URL = os.getenv("POKEAPI_LONGEST_URL")

    #Secreto para firmar y validar tokens, y proteger datos sensibles
    SECRET_KEY = os.getenv("SECRET_KEY")

    # URI de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

    # Desactiva las notificaciones de seguimiento de cambios
    SQLALCHEMY_TRACK_MODIFICATIONS = False  