import requests
import random
from flask import jsonify
from ..config import config

#Función para obtener el tipo de un Pokémon según su nombre
def get_pokemon_type(pokemon_name):

    #Contrucción de la URL para obtener los datos del Pokémon desde PokéAPI
    url = f"{config.POKEAPI_BASE_URL}/{pokemon_name.lower()}"

    try:
        #Solicitud de datos a la API PokéAPI para obtener el nombre del Pokémon
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
    
#función para obtener aleatoriamente el nombre del Pokémon según el tipo
def get_random_pokemon_by_type(pokemon_type):

    #Construcción de la URL para obtener los datos del tipo de Pokémon
    url = f"{config.POKEAPI_TYPE_URL}/{pokemon_type.lower()}"

    try:
        #Solicitud de datos a la API PokéAPI para obtener el tipo de Pokémon
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Obtener todos los Pokémon de ese tipo
        pokemon_list = data['pokemon']
        
        # Seleccionar un Pokémon al azar
        random_pokemon = random.choice(pokemon_list)['pokemon']['name']
        
        # Retorn respuesta con el  nombre del Pokémon aleatorio en formato JSON
        return jsonify({"random_pokemon": random_pokemon, "type": pokemon_type})
    
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"Error al obtener Pokémon del tipo {pokemon_type}: {http_err}"}), 404
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error: {e}"}), 500   