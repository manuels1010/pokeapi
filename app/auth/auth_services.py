import jwt
import datetime
from flask import jsonify, request
from functools import wraps
from ..config import config

#Generación del Token en JWT con expiración de 1 hora.
def generate_token(username):
    try:
        payload = {
            "username": username,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        return jsonify({"error": f"Error al generar el token: {e}"}), 500
    
#Validación del Token JWT
def validate_token(token):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None #Expiración del token.
    except jwt.InvalidTokenError:
        return None #El token no es válido.
    
    
# Decorador para proteger los endpoints que requieren autenticación
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verificar que el token esté en los headers de la solicitud
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({"message": "Token es requerido"}), 401

        try:
            # Decodificar el token
            data = validate_token(token)
            if data is None:
                return jsonify({"message": "Token inválido o expirado"}), 401
        except Exception as e:
            return jsonify({"message": f"Ocurrió un error: {str(e)}"}), 500

        return f(*args, **kwargs)

    return decorated