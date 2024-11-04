import os
from  dotenv import load_dotenv

#cargar las variables de entorno desde el archivo .env
load_dotenv ()

class config:

    #URL base de la API (PokéAPI) de Pokémon
    POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")

    #Secreto para firmar y validar tokens, y proteger datos sensibles
    SECRET_KEY = os.getenv("SECRET_KEY")