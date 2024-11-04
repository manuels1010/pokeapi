from flask import Flask
from .config import config
from .services.pokemon_services import get_pokemon_type

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #Endpoint de prueba
    @app.route('/')
    def index():
        return "¡Bienvenido a la API Pokémon!"
    
    #Endpoint para obtener el tipo de un Pokémon (fuego, agua, tierra, aire, etc) según su nombre
    @app.route('/pokemon/<string:pokemon_name>/type', methods=['GET'])
    def pokemon_type(pokemon_name):
        return get_pokemon_type(pokemon_name)
    

    return app

# Ejecución de  la aplicación
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


