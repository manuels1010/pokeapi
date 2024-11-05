# API de Pokémon

Esta API permite acceder a información sobre Pokémon, como sus tipos, obtener un Pokémon aleatorio de un tipo específico y encontrar el Pokémon con el nombre más largo dentro de cada tipo. La API también incluye autenticación JWT para asegurar el acceso a ciertos endpoints.

## Funcionalidades principales

- **Consulta de tipos de Pokémon**: Obtén el tipo de un Pokémon por su nombre.
- **Pokémon aleatorio por tipo**: Obtén un Pokémon aleatorio dentro de un tipo específico.
- **Pokémon con el nombre más largo por tipo**: Encuentra el Pokémon con el nombre más largo de un tipo dado.
- **Autenticación y registro de usuarios**: Protege los endpoints con autenticación JWT.

# Tabla de Contenido

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
  - [Endpoints](#endpoints)
  - [Autenticación](#autenticación)


## Descripción

La Pokémon API es una API RESTful desarrollada en Flask que permite consultar información sobre Pokémon y gestionar usuarios mediante un sistema de autenticación basado en tokens JWT. La API incluye endpoints para consultar el tipo de un Pokémon, obtener un Pokémon aleatorio por tipo, y autenticar usuarios.

## Instalación

### Requisitos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas con las versiones mínimas recomendadas, para realizar pruebas completas y explorar los datos, el proyecto utiliza:

- **Python** >= 3.10
- **Postman** (para pruebas de API) - cualquier versión reciente
- **SQLite** (opcional, para ver usuarios creados en la BD) - cualquier versión reciente
- **Docker** >= 20.10 (para ejecutar la aplicación en un contenedor)

## Configuración 

Clona este repositorio en tu máquina local:
```sh
git clone https://github.com/manuels1010/pokeapi.git
```
Desde la terminal posicionate en la carpeta descargada
```sh
cd pokeapi
```
Instala los requisitos desde el archivo requirements.txt
```sh
pip install -r requirements.txtdocker-compose.yaml
```
Construir las imágenes
```sh
docker-compose build
```
Desplegar los contenedores
```sh
docker-compose up
```
## uso
Esta API de Pokémon permite acceder a diferentes datos sobre los Pokémon mediante diversos endpoints, algunos de los cuales requieren autenticación para asegurar el acceso. Una vez que la API está en funcionamiento, puedes utilizar herramientas como Postman o tu navegador para interactuar con los endpoints y realizar consultas específicas sobre tipos de Pokémon, obtener un Pokémon aleatorio de un tipo o descubrir el Pokémon con el nombre más largo en una categoría específica.

**Consulta la documentación de Endpoints**:
```sh
http://127.0.0.1:5000/documentation
```
**Registrar un Usuario** (Desde la aplicación Postman):
```sh
http://127.0.0.1:5000/auth/register
```
**Iniciar Sesión y Obtener un Token** (Desde la aplicación Postman):
```sh
http://127.0.0.1:5000/auth/login
```
**Hacer una Solicitud a un Endpoint Protegido**: (Desde la aplicación Postman):
En Postman, selecciona el endpoint que deseas probar (por ejemplo, `GET http://127.0.0.1:5000/pokemon/pikachu/type`).
   - Agrega el token en el encabezado de la solicitud:
     ```
     Authorization: Bearer <tu_token>
     ```
**Ejemplo de Solicitudes**:
   - **Obtener el tipo de un Pokémon**: `GET http://127.0.0.1:5000/pokemon/pikachu/type`
   - **Obtener un Pokémon aleatorio por tipo**: `GET http://127.0.0.1:5000/pokemon/random/fire`
   - **Obtener el Pokémon con el nombre más largo por tipo**: `GET http://127.0.0.1:5000/pokemon/longest-name/grass`

## Endpoints

### 1. Inicio
- **URL**: `http://127.0.0.1:5000/`
- **Método**: GET
- **Descripción**: Direcciona al endpoint de documentación.

### 2. Documentación de la API
- **URL**: `http://127.0.0.1:5000/documentation`
- **Método**: GET
- **Descripción**: Muestra la documentación completa de los endpoints de la API.

### 3. Registro de un nuevo usuario
- **URL**: `http://127.0.0.1:5000/auth/register`
- **Método**: POST
- **Descripción**: Permite registrar un nuevo usuario para acceder a los endpoints protegidos de la API.
- **Ejemplo de uso**:
  ```sh
    {
    "username": "nuevo_usuario",
    "password": "password123"
    }
  ```
Respuesta: {"message": "Usuario registrado exitosamente"}

### 4. Inicio de sesión y obtención de token JWT
- **URL**: `http://127.0.0.1:5000/auth/login`
- **Método**: POST
- **Descripción**: Permite a un usuario iniciar sesión y obtener un token JWT para acceder a los endpoints protegidos.
- **Ejemplo de uso**:
  ```sh
    {
    "username": "nuevo_usuario",
    "password": "password123"
    }
  ```
Respuesta: {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}

### 5. Obtener el tipo de un Pokémon
- **URL**: `http://127.0.0.1:5000/pokemon/<nombre_pokemon>/type`
- **Método**: GET
- **Autenticación**: Requiere token de autenticación
- **Descripción**: Devuelve el tipo o tipos de un Pokémon específico, dado su nombre.
- **Ejemplo de uso**:
  ```http
  GET /pokemon/pikachu/type
  Respuesta: {"pokemon": "pikachu", "types": ["electric"]}

### 6. Obtener un Pokémon aleatorio de un tipo específico
- **URL**: `http://127.0.0.1:5000/pokemon/random/<tipo_pokemon>`
- **Método**: GET
- **Autenticación**: Requiere token de autenticación
- **Descripción**: Devuelve un Pokémon aleatorio dentro del tipo especificado.
- **Ejemplo de uso**:
  ```http
  GET /pokemon/random/fire
Respuesta: {"pokemon": "charmander"}

### 7. Obtener el Pokémon con el nombre más largo de un tipo específico
- **URL**: `http://127.0.0.1:5000/pokemon/longest-name/<tipo_pokemon>`
- **Método**: GET
- **Autenticación**: Requiere token de autenticación
- **Descripción**: Encuentra y devuelve el Pokémon con el nombre más largo dentro del tipo especificado.
- **Ejemplo de uso**:
  ```http
  GET /pokemon/longest-name/water
Respuesta: {"Nombre más largo": "blastoise-mega", "Tipo de Pokémon": "water"}

## Autenticación

Esta API utiliza autenticación basada en tokens JWT (JSON Web Tokens) para asegurar el acceso a ciertos endpoints. Solo los usuarios autenticados pueden acceder a los endpoints protegidos.

1. **Registrar un Usuario**
   - Antes de poder iniciar sesión, debes registrar un nuevo usuario.
   - En Postman, selecciona el método `POST`, luego elige **Body** > **raw** y selecciona **JSON** en el menú desplegable.
   - Envía la solicitud a `http://127.0.0.1:5000/auth/register` con el siguiente cuerpo en JSON:
     ```json
     {
       "username": "tu_usuario",
       "password": "tu_contraseña"
     }
     ```
   - Esto creará un nuevo usuario en la base de datos y devolverá un mensaje de confirmación.

2. **Iniciar Sesión y Obtener un Token JWT**
   - Para obtener el token JWT, repite el proceso en Postman: selecciona el método `POST`, luego **Body** > **raw** y **JSON**.
   - Envía la solicitud a `http://127.0.0.1:5000/auth/login` con el cuerpo en JSON:
     ```json
     {
       "username": "tu_usuario",
       "password": "tu_contraseña"
     }
     ```
   - Si las credenciales son correctas, recibirás una respuesta con un token JWT, que se verá algo así:
     ```json
     {
       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
     }
     ```
   - **Nota**: Este token JWT es válido solo por un tiempo limitado. Después de su expiración, deberás iniciar sesión nuevamente para obtener un nuevo token.

3. **Usar el Token JWT en Endpoints Protegidos**
   - Para acceder a los endpoints que requieren autenticación, debes incluir el token en los encabezados de la solicitud.
   - En cada solicitud, agrega un encabezado llamado `Authorization` con el valor `Bearer <tu_token>`. Por ejemplo:
     ```
     Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
     ```

### Ejemplo Completo de Uso en Postman

1. **Registro**:
   - Realiza un `POST` a `http://127.0.0.1:5000/auth/register` con el cuerpo JSON que incluya un nombre de usuario y una contraseña. No olvides seleccionar **Body** > **raw** > **JSON**.

2. **Iniciar Sesión y Obtener el Token**:
   - Realiza un `POST` a `http://127.0.0.1:5000/auth/login` usando las credenciales registradas, y copia el token JWT de la respuesta.

3. **Solicitar un Endpoint Protegido**:
   - Selecciona un endpoint protegido y agrega el token en el encabezado `Authorization` de Postman.
   - Ejemplo de solicitud:
     ```
     GET http://127.0.0.1:5000/pokemon/pikachu/type
     ```
   - **Encabezado**:
     ```
     Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
     ```