from flask import Flask
from .config import config
from .services.pokemon_services import get_pokemon_type, get_random_pokemon_by_type, get_longest_name_pokemon_by_type
from .auth.auth import auth_bp  # Importa el blueprint de autenticación
from .auth.auth_services import token_required  # Importa el decorador de autenticación
from flask import send_from_directory
from .models import db  # Importar db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #inicia la Base de datos para el registro y autenticación de usuarios.
    db.init_app(app) 

   # Crear las tablas si no existen
    with app.app_context():
        db.create_all()

    # Registrar el blueprint de autenticación
    app.register_blueprint(auth_bp, url_prefix="/auth")


    #Endpoint de prueba
    @app.route('/')
    def index():
        return "¡Bienvenido a la API Pokémon!"
    
    #Endpoint para obtener el tipo de un Pokémon (fuego, agua, tierra, aire, etc) según su nombre
    @app.route('/pokemon/<string:pokemon_name>/type', methods=['GET'])
    @token_required
    def pokemon_type(pokemon_name):
        return get_pokemon_type(pokemon_name)
    
    #Endpoint para obtener un Pokémon al azar de un tipo en específico.
    @app.route('/pokemon/random/<string:pokemon_type>', methods=['GET'])
    @token_required
    def random_pokemon_by_type(pokemon_type):
        return get_random_pokemon_by_type(pokemon_type)
    
    #Endpoint para obtener el nombre más largo de un  Pokémon según su tipo.
    @app.route('/pokemon/longest-name/<string:pokemon_type>', methods=['GET'])
    @token_required
    def longest_name_pokemon_by_type(pokemon_type):
        return get_longest_name_pokemon_by_type(pokemon_type)


    return app

# Ejecución de  la aplicación
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


