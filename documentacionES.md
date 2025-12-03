// ...existing code...
# Documentación completa del proyecto

Resumen breve
- API en FastAPI para gestión de libros, préstamos, reservas y usuarios.
- Datos persistidos en CSV en `app/db/data/`.
- Lógica separada en capas: routes → controllers → services → models → utils.

Índice
1. Instalación y ejecución
2. Estructura del proyecto (lista de archivos)
3. Modelos y esquemas (libros)
4. Servicios (libros)
5. Controladores (validaciones y excepciones de libros y estanterias)
6. Rutas / Endpoints (cómo reciben parámetros y qué devuelven libros y estanterias)
7. Utilidades y algoritmos (explicación de cada módulo)
8. Datos CSV (formato)
9. Ejemplos de requests/responses para cruds de libros
10. Notas operativas
11.susarios, prestamos y reservas

1) Instalación y ejecución
- Seguir instrucciones en [readme.md](readme.md).
- Comandos esenciales:
  - Crear entorno: `python -m venv venv`
  - Activar: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac)
  - Instalar dependencias: `pip install -r requirements.txt` — [requirements.txt](requirements.txt)
  - Ejecutar servidor: `uvicorn app.main:app --reload` — [app/main.py](app/main.py)

2) Estructura del proyecto (archivos)
- Archivos raíz:
  - [.env](.env)
  - [.gitignore](.gitignore)
  - [documentacionES.md](documentacionES.md)
  - [readme.md](readme.md)
  - [requirements.txt](requirements.txt)
- app/
  - [app/main.py](app/main.py)
  - Controllers:
    - [app/controllers/crudLibros.py](app/controllers/crudLibros.py)
    - [app/controllers/crudPrestamos.py](app/controllers/crudPrestamos.py)
    - [app/controllers/crudReservas.py](app/controllers/crudReservas.py)
    - [app/controllers/crudUser.py](app/controllers/crudUser.py)
  - DB:
    - [app/db/data/libros.csv](app/db/data/libros.csv)
    - [app/db/data/prestamos.csv](app/db/data/prestamos.csv)
    - [app/db/data/reservas.csv](app/db/data/reservas.csv)
    - [app/db/data/usuarios.csv](app/db/data/usuarios.csv)
  - Models:
    - [app/models/estanteria_model.py](app/models/estanteria_model.py)
    - [app/models/estanteria_optima_model.py](app/models/estanteria_optima_model.py)
    - [app/models/libro_model.py](app/models/libro_model.py)
    - [app/models/libro2_model.py](app/models/libro2_model.py)
    - [app/models/prestamo_model.py](app/models/prestamo_model.py)
    - [app/models/reserva_model.py](app/models/reserva_model.py)
    - [app/models/user_model.py](app/models/user_model.py)
  - Routes:
    - [app/routes/libro_routes.py](app/routes/libro_routes.py)
    - [app/routes/prestamos_routes.py](app/routes/prestamos_routes.py)
    - [app/routes/reservas_routes.py](app/routes/reservas_routes.py)
    - [app/routes/user_routes.py](app/routes/user_routes.py)
  - Schemas:
    - [app/schemas/estanteria_schema.py](app/schemas/estanteria_schema.py)
    - [app/schemas/estanteria2_schema.py](app/schemas/estanteria2_schema.py)
    - [app/schemas/estanterias_optimas_schema.py](app/schemas/estanterias_optimas_schema.py)
    - [app/schemas/libro_schema.py](app/schemas/libro_schema.py)
    - [app/schemas/libro2_schema.py](app/schemas/libro2_schema.py)
    - [app/schemas/prestamo_schema.py](app/schemas/prestamo_schema.py)
    - [app/schemas/reserva_schema.py](app/schemas/reserva_schema.py)
    - [app/schemas/user_schema.py](app/schemas/user_schema.py)
  - Services:
    - [app/services/libro_service.py](app/services/libro_service.py)
    - [app/services/prestamo_service.py](app/services/prestamo_service.py)
    - [app/services/reserva_service.py](app/services/reserva_service.py)
    - [app/services/user_service.py](app/services/user_service.py)
  - Utils:
    - libros:
      - [app/utils/libros/adaptador_estanteria.py](app/utils/libros/adaptador_estanteria.py)
      - [app/utils/libros/convert_libro2.py](app/utils/libros/convert_libro2.py)
      - [app/utils/libros/estanteria_backtracking.py](app/utils/libros/estanteria_backtracking.py)
      - [app/utils/libros/estanterias_fuerzaBruta.py](app/utils/libros/estanterias_fuerzaBruta.py)
      - [app/utils/libros/librosOrdenados.py](app/utils/libros/librosOrdenados.py)
      - [app/utils/libros/libroSort.py](app/utils/libros/libroSort.py)
      - [app/utils/libros/recursion_cola.py](app/utils/libros/recursion_cola.py)
      - [app/utils/libros/recursion_pila.py](app/utils/libros/recursion_pila.py)
    - structures:
      - [app/utils/structures/cola.py](app/utils/structures/cola.py)
      - [app/utils/structures/pila.py](app/utils/structures/pila.py)

3) Modelos y esquemas
- Modelo Libro:
  - Clase: [`Libro`](app/models/libro_model.py) — representa registro CSV con campos (según CSV y uso en service): `isbn`, `titulo`, `autor`, `peso`, `valor`, `stock`, `paginas`, `editorial`, `idioma`.
  - Alternativa/transformación: [`libro2_model.py`](app/models/libro2_model.py) y utilitarios en [app/utils/libros/convert_libro2.py](app/utils/libros/convert_libro2.py).
- Estanterías:
  - [`Estanteria`](app/models/estanteria_model.py) y [`EstanteriaOptima`](app/models/estanteria_optima_model.py) — estructuras usadas por los algoritmos de estantería.
- Prestamos / Reservas / Usuarios:
  - Modelos: [`Prestamo`](app/models/prestamo_model.py), [`Reserva`](app/models/reserva_model.py), [`User`](app/models/user_model.py).
- Schemas Pydantic:
  - CRUD libros: [`LibroCreate`](app/schemas/libro_schema.py), [`LibroUpdate`](app/schemas/libro_schema.py), [`LibroOut`](app/schemas/libro_schema.py).
  - Estantería respuestas: [`EstanteriaResponse`](app/schemas/estanteria_schema.py), [`EstanteriasOptimasResponse`](app/schemas/estanteria2_schema.py), etc.
  - Otros schemas para prestamos/reservas/usuarios en [app/schemas/](app/schemas/).

4) Servicios (lógica central)
- Archivo principal: [app/services/libro_service.py](app/services/libro_service.py)
  - [`LibroService.cargar_libros`](app/services/libro_service.py)
    - Lee `CSV_PATH` (`app/db/data/libros.csv`) con `csv.DictReader`.
    - Devuelve lista de [`Libro`](app/models/libro_model.py).
  - [`LibroService.guardar_libros`](app/services/libro_service.py)
    - Escribe lista de `Libro` en CSV. Usa fieldnames: `["isbn","titulo","autor","peso","valor","stock","paginas","editorial","idioma"]`.
  - [`LibroService.obtener_por_isbn`](app/services/libro_service.py)
    - Busca primer libro con `isbn` igual y devuelve `Libro` o `None`.
  - [`LibroService.crear`](app/services/libro_service.py)
    - Recibe instancia `Libro`, evita duplicado por `isbn`, agrega y persiste. Devuelve el libro creado o `None` si ISBN existe.
  - [`LibroService.actualizar`](app/services/libro_service.py)
    - Reemplaza entrada por `isbn`, persiste y devuelve objeto actualizado o `None`.
  - [`LibroService.eliminar`](app/services/libro_service.py)
    - Elimina por `isbn` y persiste. Devuelve `True` si se eliminó, `False` si no existía.
  - [`LibroService.ordernar_por_isbn`](app/services/libro_service.py)
    - Usa [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py). Devuelve lista ordenada.
  - [`LibroService.obtener_por_precio`](app/services/libro_service.py)
    - Usa [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py).
  - [`LibroService.estanteria_deficiente`](app/services/libro_service.py)
    - Lógica de fuerza bruta: [`estanterias_fuerzaBruta`](app/utils/libros/estanterias_fuerzaBruta.py).
  - [`LibroService.estanteria_optima`](app/services/libro_service.py)
    - Usa backtracking: [`estanteria_backtracking`](app/utils/libros/estanteria_backtracking.py) y adapta con [`adaptar_estanterias_optimas`](app/utils/libros/adaptador_estanteria.py).
  - Cálculos por autor:
    - [`LibroService.valor_total_por_autor`](app/services/libro_service.py)
      - Filtra libros por autor y llama a [`valor_total_recursivo_con_libros`](app/utils/libros/recursion_pila.py).
      - Devuelve dict: `{"valor_total": total, "libros": [titulos...]}` o `None` si no hay libros del autor.
    - [`LibroService.peso_promedio_por_autor`](app/services/libro_service.py)
      - Filtra libros por autor y llama a [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py).
      - Devuelve dict: `{"peso_promedio": promedio, "libros": [titulos...]}` o `None`.

5) Controladores
- Principales controladores para libros: [app/controllers/crudLibros.py](app/controllers/crudLibros.py)
  - Métodos y mapeo:
    - `listar_libros()` → llama a [`LibroService.cargar_libros`](app/services/libro_service.py).
    - `obtener_libro(isbn)` → llama a [`LibroService.obtener_por_isbn`](app/services/libro_service.py); lanza `HTTPException(404)` si no existe.
    - `crear_libro(data: LibroCreate)` → construye `Libro(**data.dict())` y llama a [`LibroService.crear`](app/services/libro_service.py); lanza `HTTPException(400)` si ISBN duplicado.
    - `actualizar_libro(isbn, data: LibroUpdate)` → crea `Libro(isbn=isbn, **data.dict())` y llama a [`LibroService.actualizar`](app/services/libro_service.py); lanza `HTTPException(404)` si no existe.
    - `eliminar_libro(isbn)` → llama a [`LibroService.eliminar`](app/services/libro_service.py); lanza `HTTPException(404)` si no existe.
    - Endpoints auxiliares: `libros_ordenados_isbn`, `libros_ordenados_precio`, `estanteria_deficiente`, `estanteria_optima`, `valor_total_autor`, `peso_promedio_autor` — todos delegan a los servicios y lanzan 404 cuando corresponde.

6) Rutas / Endpoints (entrada/salida)
- Archivo: [app/routes/libro_routes.py](app/routes/libro_routes.py)
- Prefijo: `/libros` (tag "Libros")
- Endpoints principales (cómo reciben y devuelven):
  - GET /libros/
    - Llama a [`LibroController.listar_libros`](app/controllers/crudLibros.py).
    - Response model: `List[LibroOut]` — schema en [app/schemas/libro_schema.py](app/schemas/libro_schema.py).
  - GET /libros/{isbn}
    - Parámetro path: `isbn: str`
    - Response model: `LibroOut`
    - Errores: 404 si no existe.
  - POST /libros/
    - Body: `LibroCreate` (JSON) — [app/schemas/libro_schema.py](app/schemas/libro_schema.py).
    - Response: `LibroOut` del libro creado.
    - Errores: 400 si ISBN duplicado.
  - PUT /libros/{isbn}
    - Parámetro path: `isbn: str`
    - Body: `LibroUpdate`
    - Response: `LibroOut` actualizado o 404.
  - DELETE /libros/{isbn}
    - Parámetro path: `isbn: str`
    - Response: `{ "message": "Libro eliminado" }` o 404.
  - GET /libros/ordenados/isbn
    - Devuelve `List[LibroOut]` ordenado por ISBN.
  - GET /libros/ordenados/precio
    - Devuelve `List[LibroOut]` ordenado por precio.
  - GET /libros/estanteria/deficiente
    - Devuelve `List[EstanteriaResponse]` — [app/schemas/estanteria_schema.py](app/schemas/estanteria_schema.py).
  - GET /libros/estanteria/optima
    - Devuelve `EstanteriasOptimasResponse` — [app/schemas/estanteria2_schema.py](app/schemas/estanteria2_schema.py).
  - GET /libros/autor/{autor}/valor-total
    - Parámetro path: `autor: str`
    - Devuelve `{"autor": <autor>, "valor_total": <float>, "libros": [titulos...]}` o 404.
  - GET /libros/autor/{autor}/peso-promedio
    - Parámetro path: `autor: str`
    - Devuelve `{"autor": <autor>, "peso_promedio": <float>, "libros": [titulos...]}` o 404.

7) Utilidades y algoritmos (explicación detallada)
- Ordenamiento ISBN
  - [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py)
  - Recibe lista de `Libro` y retorna nueva lista ordenada por `isbn`.
- Ordenamiento por precio
  - [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py)
  - Recibe lista y ordena según `valor` (float).
- Estanterías (dos aproximaciones)
  - Fuerza bruta: [`estanterias_fuerzaBruta`](app/utils/libros/estanterias_fuerzaBruta.py)
    - Genera combinaciones/explora todas las particiones (coste exponencial), devuelve estanterías con indicadores de defecto.
  - Backtracking: [`estanteria_backtracking`](app/utils/libros/estanteria_backtracking.py)
    - Busca solución óptima con poda; retorna estructura que luego transforma [`adaptar_estanterias_optimas`](app/utils/libros/adaptador_estanteria.py).
- Recursiones (ejemplos didácticos)
  - `recursion_pila.py` — función [`valor_total_recursivo_con_libros`](app/utils/libros/recursion_pila.py)
    - Recursión de pila: firma `valor_total_recursivo_con_libros(libros, index)`; caso base `index < 0` devuelve `(0, [])`. En la vuelta de la pila acumula `valor` y añade `titulo` a lista.
  - `recursion_cola.py` — función [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py)
    - Recursión de cola (tail recursion style): firma `peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None)`. Al final devuelve `(promedio, titulos)`. Se utiliza para calcular peso promedio de una lista de libros y retornar los títulos procesados; imprime trazas por consola.

8) Datos CSV (formato)
- Ubicación: [app/db/data/libros.csv](app/db/data/libros.csv)
- Campos (cabecera escrita por `guardar_libros` en [app/services/libro_service.py](app/services/libro_service.py)):
  - `isbn`, `titulo`, `autor`, `peso`, `valor`, `stock`, `paginas`, `editorial`, `idioma`
- Otros CSV:
  - [app/db/data/prestamos.csv](app/db/data/prestamos.csv)
  - [app/db/data/reservas.csv](app/db/data/reservas.csv)
  - [app/db/data/usuarios.csv](app/db/data/usuarios.csv)

9) Ejemplos de requests / responses (libros)
- GET /libros/
  - Request: sin body
  - Response 200: `[ { "isbn": "123", "titulo":"X", "autor":"Y", "peso": "0.5", "valor":"10.0", "stock":"2", "paginas":"100", "editorial":"E", "idioma":"es" }, ... ]`
  - Modelo: [`LibroOut`](app/schemas/libro_schema.py)
- GET /libros/{isbn}
  - Request: path `isbn=123`
  - Response 200: `{ ... LibroOut ... }`
  - Response 404: `{ "detail": "Libro no encontrado" }`
- POST /libros/
  - Body (ejemplo `LibroCreate`):
    {
      "isbn": "9781234567897",
      "titulo": "Mi Libro",
      "autor": "Autor Ej",
      "peso": "0.5",
      "valor": "15.5",
      "stock": "3",
      "paginas": "200",
      "editorial": "Editorial S.A.",
      "idioma": "es"
    }
  - Response 200: el recurso creado (LibroOut).
  - Response 400: `{ "detail": "El ISBN ya existe" }`
- PUT /libros/{isbn}
  - Body (`LibroUpdate`) con campos modificables (sin `isbn` en body).
  - Response 200: libro actualizado.
  - Response 404: `{ "detail": "Libro no encontrado" }`
- DELETE /libros/{isbn}
  - Response 200: `{ "message": "Libro eliminado" }` o 404.

10) Notas operativas y consideraciones
- Todos los servicios de lectura/escritura usan CSV y reescriben el fichero completo en cada operación de persistencia (ver [`LibroService.guardar_libros`](app/services/libro_service.py)). Esto es sencillo pero no es concurrente ni transaccional: evitar uso concurrente en producción.
- Validación: gran parte de la validación de entrada debería definirse en los schemas Pydantic en [app/schemas/](app/schemas/). Revisar tipos y límites allí.
- Rendimiento:
  - Operaciones como `estanterias_fuerzaBruta` son costosas; evitar con muchos libros.
  - `cargar_libros()` lee todo el CSV en cada llamada; cachear en memoria para altas tasas de lectura.
- Pruebas: no se encuentran tests; se recomienda añadir tests unitarios para:
  - CRUD de `LibroService`
  - Algoritmos de estantería (casos pequeños y grandes)
  - Funciones de utilidades recursivas
- Logging: las funciones recursivas imprimen trazas con `print` (p. ej. [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py)). Cambiar a logging para control de niveles.

Referencias directas a funciones/clases mencionadas (por archivo)
- Servicios y funciones usadas en controladores:
  - [`LibroService.cargar_libros`](app/services/libro_service.py)
  - [`LibroService.guardar_libros`](app/services/libro_service.py)
  - [`LibroService.obtener_por_isbn`](app/services/libro_service.py)
  - [`LibroService.crear`](app/services/libro_service.py)
  - [`LibroService.actualizar`](app/services/libro_service.py)
  - [`LibroService.eliminar`](app/services/libro_service.py)
  - [`LibroService.ordernar_por_isbn`](app/services/libro_service.py)
  - [`LibroService.obtener_por_precio`](app/services/libro_service.py)
  - [`LibroService.estanteria_deficiente`](app/services/libro_service.py)
  - [`LibroService.estanteria_optima`](app/services/libro_service.py)
  - [`LibroService.valor_total_por_autor`](app/services/libro_service.py)
  - [`LibroService.peso_promedio_por_autor`](app/services/libro_service.py)
- Controlador de libros:
  - [`LibroController.listar_libros`](app/controllers/crudLibros.py)
  - [`LibroController.obtener_libro`](app/controllers/crudLibros.py)
  - [`LibroController.crear_libro`](app/controllers/crudLibros.py)
  - [`LibroController.actualizar_libro`](app/controllers/crudLibros.py)
  - [`LibroController.eliminar_libro`](app/controllers/crudLibros.py)
  - [`LibroController.libros_ordenados_isbn`](app/controllers/crudLibros.py)
  - [`LibroController.libros_ordenados_precio`](app/controllers/crudLibros.py)
  - [`LibroController.estanteria_deficiente`](app/controllers/crudLibros.py)
  - [`LibroController.estanteria_optima`](app/controllers/crudLibros.py)
  - [`LibroController.valor_total_autor`](app/controllers/crudLibros.py)
  - [`LibroController.peso_promedio_autor`](app/controllers/crudLibros.py)
- Utilidades:
  - [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py)
  - [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py)
  - [`estanterias_fuerzaBruta`](app/utils/libros/estanterias_fuerzaBruta.py)
  - [`estanteria_backtracking`](app/utils/libros/estanteria_backtracking.py)
  - [`adaptar_estanterias_optimas`](app/utils/libros/adaptador_estanteria.py)
  - [`valor_total_recursivo_con_libros`](app/utils/libros/recursion_pila.py)
  - [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py)


11) Préstamos, Reservas y Usuarios — documentación completa

Resumen general
- Estas tres áreas siguen la misma arquitectura que Libros: routes → controllers → services → models → schemas → persistencia en CSV.
- Se documenta a continuación qué hace cada módulo, cómo recibe parámetros, qué devuelve y ejemplos de uso.

A. Préstamos (app/controllers/crudPrestamos.py, app/services/prestamo_service.py, app/models/prestamo_model.py, app/schemas/prestamo_schema.py, app/db/data/prestamos.csv, app/routes/prestamos_routes.py)

1. Modelo y schema
- Modelo (Prestamo):
  - Representa un registro de préstamo. Campos típicos (ver app/models/prestamo_model.py para confirmar): id, isbn, usuario_id, fecha_prestamo, fecha_devolucion (opcional), estado (ej. "activo", "devuelto").
- Schemas Pydantic (app/schemas/prestamo_schema.py):
  - PrestamoCreate: body requerido para crear un préstamo (isbn, usuario_id, fecha_prestamo opcional → default now).
  - PrestamoUpdate: campos permitidos para actualizar (fecha_devolucion, estado).
  - PrestamoOut: schema de salida (todos los campos, id asignado).

2. Servicio (app/services/prestamo_service.py)
- Cargar_prestamos():
  - Lee CSV prestamos.csv y devuelve lista de modelos Prestamo.
- Guardar_prestamos(lista):
  - Persiste lista completa en CSV (reescribe).
- crear_prestamo(prestamo_data):
  - Valida existencia de libro (por isbn) y existencia de usuario (por usuario_id) llamando a LibroService y UserService.
  - Comprueba stock: reduce stock en LibroService si el préstamo se realiza correctamente.
  - Genera id único (p. ej. incremental) y guarda.
  - Devuelve Prestamo creado o lanza/retorna error si inválido.
- actualizar_prestamo(id, cambios):
  - Aplica cambios (p. ej. marcar devuelto) y persiste. Si se marca devuelto, incrementa stock del libro.
- eliminar_prestamo(id):
  - Elimina registro por id y persiste.

3. Controlador (app/controllers/crudPrestamos.py) — contratos HTTP
- GET /prestamos/ — lista todos los préstamos. Respuesta 200: List[PrestamoOut].
- GET /prestamos/{id} — path param id (int/str según implementación). 200: PrestamoOut, 404 si no existe.
- POST /prestamos/ — body PrestamoCreate. 201/200: PrestamoOut recién creado. Errores: 400 si libro no disponible, 404 si libro o usuario no existe.
- PUT /prestamos/{id} — body PrestamoUpdate. 200: PrestamoOut actualizado o 404.
- DELETE /prestamos/{id} — elimina préstamo. 200: { "message": "Prestamo eliminado" } o 404.

4. CSV (app/db/data/prestamos.csv)
- Cabecera esperada (ejemplo): id,isbn,usuario_id,fecha_prestamo,fecha_devolucion,estado
- Nota: confirmar formato de fecha (ISO 8601 recomendado: YYYY-MM-DDTHH:MM:SS).

5. Ejemplos
- Crear préstamo (POST /prestamos/)
  Request body:
  {
    "isbn": "9781234567897",
    "usuario_id": "u123"
  }
  Response 200/201:
  {
    "id": "p456",
    "isbn": "9781234567897",
    "usuario_id": "u123",
    "fecha_prestamo": "2025-12-03T10:00:00",
    "fecha_devolucion": null,
    "estado": "activo"
  }
- Marcar devuelto (PUT /prestamos/{id})
  Body:
  {
    "fecha_devolucion": "2025-12-10T12:00:00",
    "estado": "devuelto"
  }

B. Reservas (app/controllers/crudReservas.py, app/services/reserva_service.py, app/models/reserva_model.py, app/schemas/reserva_schema.py, app/db/data/reservas.csv, app/routes/reservas_routes.py)

1. Modelo y schema
- Modelo Reserva:
  - Campos típicos: id, isbn, usuario_id, fecha_reserva, estado (ej. "activa", "cancelada", "convertida_en_prestamo").
- Schemas:
  - ReservaCreate: isbn, usuario_id, fecha_reserva opcional.
  - ReservaUpdate: campos modificables (estado).
  - ReservaOut: todos los campos.

2. Servicio (app/services/reserva_service.py)
- cargar_reservas(), guardar_reservas(lista).
- crear_reserva(reserva_data):
  - Verifica que el usuario existe y que no haya reserva duplicada para el mismo libro/usuario.
  - Añade reserva al CSV.
- actualizar_reserva(id, cambios):
  - Cambios de estado (p. ej. cancelar), persiste.
- convertir_a_prestamo(id):
  - Si el libro pasa a estar disponible, convertir la reserva en préstamo: crea préstamo mediante PrestamoService y elimina/actualiza reserva.

3. Controlador (app/controllers/crudReservas.py)
- GET /reservas/ — lista.
- GET /reservas/{id} — detalle.
- POST /reservas/ — crear (body ReservaCreate). Errores: 400 si duplicada, 404 si usuario/libro no existen.
- PUT /reservas/{id} — actualizar.
- DELETE /reservas/{id} — eliminar.

4. CSV (app/db/data/reservas.csv)
- Cabecera ejemplo: id,isbn,usuario_id,fecha_reserva,estado

5. Ejemplos
- Crear reserva:
  Request:
  {
    "isbn": "9781234567897",
    "usuario_id": "u123"
  }
  Response:
  {
    "id": "r789",
    "isbn": "9781234567897",
    "usuario_id": "u123",
    "fecha_reserva": "2025-12-03T11:00:00",
    "estado": "activa"
  }

C. Usuarios (app/controllers/crudUser.py, app/services/user_service.py, app/models/user_model.py, app/schemas/user_schema.py, app/db/data/usuarios.csv, app/routes/user_routes.py)

1. Modelo y schema
- Modelo User / Usuario:
  - Campos comunes: id, nombre, email, telefono (opcional), direccion (opcional), fecha_registro.
- Schemas:
  - UserCreate: nombre, email, telefono?, direccion?
  - UserUpdate: campos actualizables.
  - UserOut: datos devueltos (sin contraseñas si las hubiera).

2. Servicio (app/services/user_service.py)
- cargar_usuarios(), guardar_usuarios(lista).
- crear_usuario(user_data):
  - Valida unicidad de email/id, genera id, persiste.
- obtener_usuario_por_id(id), obtener_por_email(email)
- actualizar_usuario(id, cambios)
- eliminar_usuario(id):
  - Considerar integridad: al eliminar usuario, gestionar prestamos/reservas pendientes (opcional: rechazar la eliminación si existen préstamos activos).

3. Controlador (app/controllers/crudUser.py)
- GET /usuarios/ — lista usuarios.
- GET /usuarios/{id} — detalle.
- POST /usuarios/ — crear (UserCreate). 201: UserOut.
- PUT /usuarios/{id} — actualizar.
- DELETE /usuarios/{id} — eliminar (considerar 400/409 si hay recursos asociados).

4. CSV (app/db/data/usuarios.csv)
- Cabecera ejemplo: id,nombre,email,telefono,direccion,fecha_registro

5. Ejemplos
- Crear usuario (POST /usuarios/)
  Body:
  {
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "555-1234"
  }
  Response:
  {
    "id": "u123",
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "555-1234",
    "direccion": null,
    "fecha_registro": "2025-12-03T11:30:00"
  }

D. Integración entre módulos — reglas y flujos importantes
- Validaciones cruzadas:
  - Al crear préstamo se debe comprobar usuario y libro existentes y stock disponible.
  - Al devolver un libro (actualizar préstamo a "devuelto") se debe incrementar stock del libro.
  - Al crear reserva se comprueba duplicados y existencia de usuario/libro.
  - Converting reserva → préstamo debe respetar reglas de stock y eliminar/actualizar la reserva.
- Atomicidad y concurrencia:
  - Persistencia en CSV no es atómica ni concurrente; realizar verificaciones y bloqueos a nivel de aplicación si se requiere concurrencia.
- Manejo de ids:
  - Recomendar usar ids únicos (UUID o incremental persistente). Ver implementación en services para detalles.

E. Contratos HTTP y códigos de estado recomendados
- 200 OK: respuestas GET, PUT exitosas.
- 201 Created: POST que crea el recurso.
- 204 No Content: DELETE exitoso (opcional).
- 400 Bad Request: validaciones de entrada (ej. libro no disponible, campos faltantes).
- 404 Not Found: recurso no existe (usuario, libro, préstamo, reserva).
- 409 Conflict: conflictos de estado (ej. eliminar usuario con préstamos activos) — opcional según implementación.

F. Pruebas recomendadas
- Unit tests para:
  - Crear/actualizar/eliminar usuarios, reservas y préstamos en el service layer (simulando CSV con fixtures).
  - Flujos integrados: crear reserva y luego convertir a préstamo; crear préstamo y marcar devuelto (ver cambio en stock).
  - Casos de error: préstamo de libro sin stock, reserva duplicada, eliminar usuario con recursos asociados.

G. Siguientes pasos prácticos (prioridad)
1. Revisar app/models/* y app/schemas/* para confirmar los nombres de campos exactos y adaptar la documentación (actualizar CSV header si difiere).
2. Añadir validaciones Pydantic en schemas (formatos de fecha, email).
3. Implementar logging en services (reemplazar print).
4. Añadir tests unitarios para servicios y controladores.

Fin de la ampliación: Préstamos, Reservas y Usuarios.

{ changed code }
// ...existing code...
````// filepath: c:\Users\joesh\OneDrive\Escritorio\Tecnicas prog\proyecto\documentacionES.md
// ...existing code...
{ changed code }

11) Préstamos, Reservas y Usuarios — documentación completa

Resumen general
- Estas tres áreas siguen la misma arquitectura que Libros: routes → controllers → services → models → schemas → persistencia en CSV.
- Se documenta a continuación qué hace cada módulo, cómo recibe parámetros, qué devuelve y ejemplos de uso.

A. Préstamos (app/controllers/crudPrestamos.py, app/services/prestamo_service.py, app/models/prestamo_model.py, app/schemas/prestamo_schema.py, app/db/data/prestamos.csv, app/routes/prestamos_routes.py)

1. Modelo y schema
- Modelo (Prestamo):
  - Representa un registro de préstamo. Campos típicos (ver app/models/prestamo_model.py para confirmar): id, isbn, usuario_id, fecha_prestamo, fecha_devolucion (opcional), estado (ej. "activo", "devuelto").
- Schemas Pydantic (app/schemas/prestamo_schema.py):
  - PrestamoCreate: body requerido para crear un préstamo (isbn, usuario_id, fecha_prestamo opcional → default now).
  - PrestamoUpdate: campos permitidos para actualizar (fecha_devolucion, estado).
  - PrestamoOut: schema de salida (todos los campos, id asignado).

2. Servicio (app/services/prestamo_service.py)
- Cargar_prestamos():
  - Lee CSV prestamos.csv y devuelve lista de modelos Prestamo.
- Guardar_prestamos(lista):
  - Persiste lista completa en CSV (reescribe).
- crear_prestamo(prestamo_data):
  - Valida existencia de libro (por isbn) y existencia de usuario (por usuario_id) llamando a LibroService y UserService.
  - Comprueba stock: reduce stock en LibroService si el préstamo se realiza correctamente.
  - Genera id único (p. ej. incremental) y guarda.
  - Devuelve Prestamo creado o lanza/retorna error si inválido.
- actualizar_prestamo(id, cambios):
  - Aplica cambios (p. ej. marcar devuelto) y persiste. Si se marca devuelto, incrementa stock del libro.
- eliminar_prestamo(id):
  - Elimina registro por id y persiste.

3. Controlador (app/controllers/crudPrestamos.py) — contratos HTTP
- GET /prestamos/ — lista todos los préstamos. Respuesta 200: List[PrestamoOut].
- GET /prestamos/{id} — path param id (int/str según implementación). 200: PrestamoOut, 404 si no existe.
- POST /prestamos/ — body PrestamoCreate. 201/200: PrestamoOut recién creado. Errores: 400 si libro no disponible, 404 si libro o usuario no existe.
- PUT /prestamos/{id} — body PrestamoUpdate. 200: PrestamoOut actualizado o 404.
- DELETE /prestamos/{id} — elimina préstamo. 200: { "message": "Prestamo eliminado" } o 404.

4. CSV (app/db/data/prestamos.csv)
- Cabecera esperada (ejemplo): id,isbn,usuario_id,fecha_prestamo,fecha_devolucion,estado
- Nota: confirmar formato de fecha (ISO 8601 recomendado: YYYY-MM-DDTHH:MM:SS).

5. Ejemplos
- Crear préstamo (POST /prestamos/)
  Request body:
  {
    "isbn": "9781234567897",
    "usuario_id": "u123"
  }
  Response 200/201:
  {
    "id": "p456",
    "isbn": "9781234567897",
    "usuario_id": "u123",
    "fecha_prestamo": "2025-12-03T10:00:00",
    "fecha_devolucion": null,
    "estado": "activo"
  }
- Marcar devuelto (PUT /prestamos/{id})
  Body:
  {
    "fecha_devolucion": "2025-12-10T12:00:00",
    "estado": "devuelto"
  }

B. Reservas (app/controllers/crudReservas.py, app/services/reserva_service.py, app/models/reserva_model.py, app/schemas/reserva_schema.py, app/db/data/reservas.csv, app/routes/reservas_routes.py)

1. Modelo y schema
- Modelo Reserva:
  - Campos típicos: id, isbn, usuario_id, fecha_reserva, estado (ej. "activa", "cancelada", "convertida_en_prestamo").
- Schemas:
  - ReservaCreate: isbn, usuario_id, fecha_reserva opcional.
  - ReservaUpdate: campos modificables (estado).
  - ReservaOut: todos los campos.

2. Servicio (app/services/reserva_service.py)
- cargar_reservas(), guardar_reservas(lista).
- crear_reserva(reserva_data):
  - Verifica que el usuario existe y que no haya reserva duplicada para el mismo libro/usuario.
  - Añade reserva al CSV.
- actualizar_reserva(id, cambios):
  - Cambios de estado (p. ej. cancelar), persiste.
- convertir_a_prestamo(id):
  - Si el libro pasa a estar disponible, convertir la reserva en préstamo: crea préstamo mediante PrestamoService y elimina/actualiza reserva.

3. Controlador (app/controllers/crudReservas.py)
- GET /reservas/ — lista.
- GET /reservas/{id} — detalle.
- POST /reservas/ — crear (body ReservaCreate). Errores: 400 si duplicada, 404 si usuario/libro no existen.
- PUT /reservas/{id} — actualizar.
- DELETE /reservas/{id} — eliminar.

4. CSV (app/db/data/reservas.csv)
- Cabecera ejemplo: id,isbn,usuario_id,fecha_reserva,estado

5. Ejemplos
- Crear reserva:
  Request:
  {
    "isbn": "9781234567897",
    "usuario_id": "u123"
  }
  Response:
  {
    "id": "r789",
    "isbn": "9781234567897",
    "usuario_id": "u123",
    "fecha_reserva": "2025-12-03T11:00:00",
    "estado": "activa"
  }

C. Usuarios (app/controllers/crudUser.py, app/services/user_service.py, app/models/user_model.py, app/schemas/user_schema.py, app/db/data/usuarios.csv, app/routes/user_routes.py)

1. Modelo y schema
- Modelo User / Usuario:
  - Campos comunes: id, nombre, email, telefono (opcional), direccion (opcional), fecha_registro.
- Schemas:
  - UserCreate: nombre, email, telefono?, direccion?
  - UserUpdate: campos actualizables.
  - UserOut: datos devueltos (sin contraseñas si las hubiera).

2. Servicio (app/services/user_service.py)
- cargar_usuarios(), guardar_usuarios(lista).
- crear_usuario(user_data):
  - Valida unicidad de email/id, genera id, persiste.
- obtener_usuario_por_id(id), obtener_por_email(email)
- actualizar_usuario(id, cambios)
- eliminar_usuario(id):
  - Considerar integridad: al eliminar usuario, gestionar prestamos/reservas pendientes (opcional: rechazar la eliminación si existen préstamos activos).

3. Controlador (app/controllers/crudUser.py)
- GET /usuarios/ — lista usuarios.
- GET /usuarios/{id} — detalle.
- POST /usuarios/ — crear (UserCreate). 201: UserOut.
- PUT /usuarios/{id} — actualizar.
- DELETE /usuarios/{id} — eliminar (considerar 400/409 si hay recursos asociados).

4. CSV (app/db/data/usuarios.csv)
- Cabecera ejemplo: id,nombre,email,telefono,direccion,fecha_registro

5. Ejemplos
- Crear usuario (POST /usuarios/)
  Body:
  {
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "555-1234"
  }
  Response:
  {
    "id": "u123",
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "555-1234",
    "direccion": null,
    "fecha_registro": "2025-12-03T11:30:00"
  }

D. Integración entre módulos — reglas y flujos importantes
- Validaciones cruzadas:
  - Al crear préstamo se debe comprobar usuario y libro existentes y stock disponible.
  - Al devolver un libro (actualizar préstamo a "devuelto") se debe incrementar stock del libro.
  - Al crear reserva se comprueba duplicados y existencia de usuario/libro.
  - Converting reserva → préstamo debe respetar reglas de stock y eliminar/actualizar la reserva.
- Atomicidad y concurrencia:
  - Persistencia en CSV no es atómica ni concurrente; realizar verificaciones y bloqueos a nivel de aplicación si se requiere concurrencia.
- Manejo de ids:
  - Recomendar usar ids únicos (UUID o incremental persistente). Ver implementación en services para detalles.

E. Contratos HTTP y códigos de estado recomendados
- 200 OK: respuestas GET, PUT exitosas.
- 201 Created: POST que crea el recurso.
- 204 No Content: DELETE exitoso (opcional).
- 400 Bad Request: validaciones de entrada (ej. libro no disponible, campos faltantes).
- 404 Not Found: recurso no existe (usuario, libro, préstamo, reserva).
- 409 Conflict: conflictos de estado (ej. eliminar usuario con préstamos activos) — opcional según implementación.

F. Pruebas recomendadas
- Unit tests para:
  - Crear/actualizar/eliminar usuarios, reservas y préstamos en el service layer (simulando CSV con fixtures).
  - Flujos integrados: crear reserva y luego convertir a préstamo; crear préstamo y marcar devuelto (ver cambio en stock).
  - Casos de error: préstamo de libro sin stock, reserva duplicada, eliminar usuario con recursos asociados.

G. Siguientes pasos prácticos (prioridad)
1. Revisar app/models/* y app/schemas/* para confirmar los nombres de campos exactos y adaptar la documentación (actualizar CSV header si difiere).
2. Añadir validaciones Pydantic en schemas (formatos de fecha, email).
3. Implementar logging en services (reemplazar print).
4. Añadir tests unitarios para servicios y controladores.

Fin de la ampliación: Préstamos, Reservas y Usuarios.