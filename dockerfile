# Usa una imagen base de Python
FROM python:3.10

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto a la imagen
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá Flask
EXPOSE 5000

# Configura el comando para correr la aplicación
CMD ["python", "-m", "app.main"]