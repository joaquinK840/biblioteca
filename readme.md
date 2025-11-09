# 1. Crear el entorno virtual
python -m venv venv 

# 2. Activar el entorno
-- En Windows:
venv\Scripts\activate
-- En Linux/Mac o bash:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. crear base de datos
-- En la terminal psql (o pgAdmin)
CREATE DATABASE biblioteca_db;
-- o desde shell:
psql -U postgres (e ingresas la contraseña)
CREATE USER admin WITH PASSWORD '1234'; (si es que el usuario admin no esta creado)
CREATE DATABASE biblioteca_db OWNER admin;
GRANT ALL PRIVILEGES ON DATABASE biblioteca_db TO admin;
# 5. ejecutar sql
psql -h localhost -p 5432 -U admin -d biblioteca_db -f app/db/schemas.sql

# 6. ejecutar los datos por defecto
python app/db/load_initial_data.py

# 7. Ejecutar el servidor
uvicorn app.main:app --reload


comando para ver las tablas

# 1 entrar a la db
psql -h localhost -p 5432 -U admin -d biblioteca_db
# 2 ajustar el tipado
\encoding UTF8
# 3 hacer el select (en este caso libros)
SELECT * FROM libros;
