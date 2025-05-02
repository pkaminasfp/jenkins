# Imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Ejecutar pruebas al construir la imagen
CMD ["python", "-m", "unittest", "test_calculadora.py"]