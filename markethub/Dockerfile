# Utiliza la imagen oficial de Python 3.11 slim como imagen base
FROM python:3.11-slim

# Establece un directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias necesarias desde el archivo de requerimientos
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación en el directorio de trabajo
COPY . .

# Expone el puerto 8501 que es el predeterminado para Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "login.py"]