-- DB/schema.sql
-- Esquema de la base de datos para el Sistema de Gestión de Bibliotecas (SGB)
-- Ejecutar con: psql -h <host> -p <port> -U <user> -d <db> -f DB/schema.sql

-- ===========================
-- Tabla: usuarios
-- ===========================
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE,
    telefono VARCHAR(50),
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ===========================
-- Tabla: libros
-- ===========================
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR(32) NOT NULL UNIQUE,
    titulo TEXT NOT NULL,
    autor VARCHAR(200) NOT NULL,
    peso NUMERIC(8,3) NOT NULL,            -- Kg, ejemplo 1.250
    valor NUMERIC(14,2) NOT NULL,          -- Pesos colombianos
    stock INTEGER DEFAULT 1 NOT NULL,      -- Cantidad disponible
    paginas INTEGER,
    editorial VARCHAR(200),
    idioma VARCHAR(50),
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_libros_isbn ON libros(isbn);
CREATE INDEX IF NOT EXISTS idx_libros_autor ON libros(autor);

-- ===========================
-- Tabla: prestamos
-- Representa cada operación de préstamo.
-- Se usa para historial (stack) por usuario.
-- ===========================
CREATE TABLE IF NOT EXISTS prestamos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    libro_id INTEGER NOT NULL REFERENCES libros(id) ON DELETE RESTRICT,
    isbn_snapshot VARCHAR(32) NOT NULL,          -- guarda ISBN por redundancia
    fecha_prestamo TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    fecha_devolucion TIMESTAMP WITH TIME ZONE,    -- NULL si no devuelto
    devuelto BOOLEAN DEFAULT FALSE,
    observaciones TEXT
);

CREATE INDEX IF NOT EXISTS idx_prestamos_usuario ON prestamos(usuario_id);
CREATE INDEX IF NOT EXISTS idx_prestamos_libro ON prestamos(libro_id);

-- ===========================
-- Tabla: reservas
-- Representa la cola FIFO de reservas por libro cuando stock = 0
-- ===========================
CREATE TABLE IF NOT EXISTS reservas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    libro_id INTEGER NOT NULL REFERENCES libros(id) ON DELETE CASCADE,
    fecha_reserva TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    atendida BOOLEAN DEFAULT FALSE,
    atendida_en TIMESTAMP WITH TIME ZONE,
    notas TEXT
);

CREATE INDEX IF NOT EXISTS idx_reservas_libro_fecha ON reservas(libro_id, fecha_reserva);

-- ===========================
-- Tabla: estantes
-- Representa estantes físicos o virtuales
-- ===========================
CREATE TABLE IF NOT EXISTS estantes (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    capacidad_kg NUMERIC(8,3) DEFAULT 8.000, -- por requerimiento 8 Kg
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ===========================
-- Tabla: asignaciones_estante
-- Asignación de libros a estantes (muchos a muchos con metadatos)
-- ===========================
CREATE TABLE IF NOT EXISTS asignaciones_estante (
    id SERIAL PRIMARY KEY,
    estante_id INTEGER NOT NULL REFERENCES estantes(id) ON DELETE CASCADE,
    libro_id INTEGER NOT NULL REFERENCES libros(id) ON DELETE CASCADE,
    posicion VARCHAR(50),         -- posición lógica dentro del estante (opcional)
    peso_kg NUMERIC(8,3) NOT NULL,
    valor_snapshot NUMERIC(14,2) NOT NULL, -- valor en el momento de la asignación
    asignado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_asignaciones_estante ON asignaciones_estante(estante_id, libro_id);

-- ===========================
-- Tabla: metadata (opcional)
-- Para guardar conteos, reportes precalculados o settings
-- ===========================
CREATE TABLE IF NOT EXISTS metadata (
    clave VARCHAR(200) PRIMARY KEY,
    valor TEXT,
    actualizado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ===========================
-- FIN del script
-- ===========================
