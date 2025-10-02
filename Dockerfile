# -----------------------------------------
# Materia: Administración de Infraestructura Virtualizada II
# Profesor: Froylán Alonso Pérez Alanís
# Alumno: Mario Eduardo Núñez Zapata
# -----------------------------------------

# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt requirements.txt
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
