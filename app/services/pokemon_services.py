import requests
from flask import jsonify
from ..config import config

def get_pokemon_type(pokemon_name):

    #Contrucción de la URL para obtener los datos del Pokémon desde PokéAPI
    url = f"{config.POKEAPI_BASE_URL}/{pokemon_name.lower()}"

    try:
        #Solicitud de datos a la API PokéAPI   
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        #Extraer los datos de "types" para obtener el tipo de Pokémon
        types = [type_info['type']['name'] for type_info in data['types']]

        #Retorna respuesta en formato JSON del nombre y tipo de Pókemon
        return jsonify({"Nombre del Pokémon": pokemon_name, "Tipo de Pokémon": types })

    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"Error al obtener el Pokémon: {http_err}"}), 404
    except Exception as e:
        return jsonify({"error": f"Ocurrio un error: {http_err}"}), 500