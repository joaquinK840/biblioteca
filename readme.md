# 1. Crear el entorno virtual
python -m venv venv 

# 2. Activar el entorno
-- En Windows:
venv\Scripts\activate
-- En Linux/Mac o bash:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el servidor
uvicorn app.main:app --reload

