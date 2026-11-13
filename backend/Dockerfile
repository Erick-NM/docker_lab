# Imagen base ligera de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Evitar generación de bytecode .pyc y habilitar salida de logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias primero para optimizar la caché de capas de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación
COPY app.py .

# Exponer el puerto del backend Flask
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
