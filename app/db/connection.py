# DB/connection.py
"""
Conexión a la base de datos PostgreSQL para el proyecto SGB.

- Carga variables desde .env (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS).
- Crea engine SQLAlchemy, SessionLocal y Base.
- Provee `init_db(schema_path)` para ejecutar un archivo SQL que cree las tablas.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # lee .env en la raíz del proyecto

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "biblioteca_db")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine y sesión
engine = create_engine(DATABASE_URL, future=True)  # future=True usa API 2.0
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

# Base para los modelos ORM (si luego defines modelos en Python)
Base = declarative_base()


def get_db():
    """
    Dependencia de FastAPI: yield una sesión y la cierra al finalizar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db(schema_path: str = "DB/schema.sql"):
    """
    Ejecuta un archivo SQL (schema_path) sobre la base de datos conectada.
    Útil para crear tablas definidas en DB/schema.sql desde Python.

    Ejemplo:
        from DB.connection import init_db
        init_db("DB/schema.sql")
    """
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"El archivo de schema no existe: {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as f:
        sql = f.read()

    # Ejecutar SQL en transacción
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            # dividir por ; puede ayudar si hay múltiples statements
            # usamos exec_driver_sql para pasar SQL crudo
            conn.exec_driver_sql(sql)
            trans.commit()
            print(f"Schema ejecutado correctamente desde: {schema_path}")
        except Exception:
            trans.rollback()
            raise

