from flask import Blueprint, request, jsonify
from .auth_services import generate_token
from ..models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

#Endpoint para el registro de usuarios para el consumo de los endpoint de Pokémon
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username y password son requeridos"}), 400
    
 # Verificación usuario existe en la BD
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El usuario ya existe en la Base de datos"}), 400
   
    # Crear el nuevo usuario con la contraseña hasheada
    new_user = User(username=username)
    new_user.password_hash = generate_password_hash(password)  # Hasheamos la contraseña
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201 

# Endpoint para autenticar un usuario y devolver un token
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username y password son requeridos"}), 400

    # Verificación usurio y contraseña
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):  # Validar la contraseña
        # Generar y devolver el token
        token = generate_token(username)
        return jsonify({"token": token}), 200

    return jsonify({"error": "Credenciales incorrectas"}), 401