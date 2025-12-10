# Proyecto Biblioteca (CSV Library API)

Pequeña guía rápida para correr y entender el proyecto.

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

app/
├── models/ → Clases POO (Libro, Usuario, Prestamo, Reserva)
├── schemas/ → Validación Pydantic
├── controllers/ → Lógica de control
├── services/ → Lógica de negocio
├── routes/ → Endpoints API
├── utils/
│ ├── structures/ → Pila y Cola
│ └── libros/ → Algoritmos (búsquedas, ordenamientos, backtracking, recursión)
├── algorithms/ → Algoritmos adicionales
└── db/data/ → Archivos CSV

## Qué hace cada parte

- `app/main.py`: Configura FastAPI, CORS, estáticos y templates; registra routers.
- `routes/`: Define endpoints (libros, usuarios, préstamos, reservas, estanterías).
- `controllers/`: Orquesta servicios y maneja errores HTTP (404/400).
- `services/`: Acceso a CSV y lógica de negocio (CRUD, algoritmos).
- `schemas/`: Modelos de entrada/salida Pydantic para validar datos.
- `models/`: Clases del dominio (Libro, Usuario, Prestamo, Reserva).
- `utils/structures/`: Estructuras de datos (Pila LIFO, Cola FIFO).
- `utils/libros/`: Algoritmos (insertion sort por ISBN, merge sort por precio, búsqueda lineal/binaria, backtracking ≤8kg, recursión).
- `db/data/`: Datos en CSV (libros, usuarios, préstamos, reservas).

## Endpoints útiles

- `GET /libros`: Lista libros.
- `GET /libros/buscar?q=...`: Búsqueda lineal por título/autor.
- `GET /libros/ordenados/isbn`: Ordenar por ISBN (Insertion Sort).
- `GET /libros/ordenados/precio`: Ordenar por precio (Merge Sort).
- `GET /libros/estanteria/deficiente`: Combinaciones > 8 kg (fuerza bruta).
- `GET /libros/estanteria/optima`: Estantería óptima (Backtracking).
- `GET /libros/autor/{autor}/valor-total`: Recursión de pila.
- `GET /libros/autor/{autor}/peso-promedio`: Recursión de cola.
- `GET /prestamos`, `POST /prestamos`, `PUT /prestamos/devolver/{id}`: CRUD + devoluciones.
- `GET /reservas`, `POST /reservas`, `GET /reservas/cola/{isbn}`: CRUD + cola FIFO.
- `GET /usuarios`: Gestión de usuarios.


