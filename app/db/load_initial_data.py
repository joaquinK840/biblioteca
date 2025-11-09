import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# =====================================
# Carga de variables de entorno (.env)
# =====================================
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "biblioteca_db")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "pucho123")

# =====================================
# Crear motor de conexión SQLAlchemy
# =====================================
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# =====================================
# Ruta del archivo CSV
# =====================================
CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "libros_initial.csv")

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"No se encontró el archivo: {CSV_PATH}")

# =====================================
# Leer el CSV con pandas
# =====================================
df = pd.read_csv(CSV_PATH)

print(f"📚 Cargando {len(df)} libros en la base de datos...")

# =====================================
# Insertar los datos
# =====================================
with engine.begin() as connection:
    # Limpiamos la tabla antes de insertar (opcional)
    connection.execute(text("TRUNCATE TABLE libros RESTART IDENTITY CASCADE;"))

    # Insertamos fila por fila
    for _, row in df.iterrows():
        connection.execute(
            text("""
                INSERT INTO libros (isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma)
                VALUES (:isbn, :titulo, :autor, :peso, :valor, :stock, :paginas, :editorial, :idioma)
            """),
            {
                "isbn": row["isbn"],
                "titulo": row["titulo"],
                "autor": row["autor"],
                "peso": float(row["peso"]),
                "valor": float(row["valor"]),
                "stock": int(row["stock"]),
                "paginas": int(row["paginas"]) if not pd.isna(row["paginas"]) else None,
                "editorial": row.get("editorial", None),
                "idioma": row.get("idioma", None)
            }
        )

print("✅ Libros cargados correctamente en la tabla 'libros'.")
