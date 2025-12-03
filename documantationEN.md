// ...existing code...
# Complete Project Documentation

Brief Summary
- FastAPI API for managing books, loans, reservations, and users.
- Data persisted in CSV in `app/db/data/`.
- Logic separated in layers: routes → controllers → services → models → utils.

Table of Contents
1. Installation and execution
2. Project structure (file list)
3. Models and schemas (books)
4. Services (books)
5. Controllers (validations and exceptions for books and shelves)
6. Routes / Endpoints (how they receive parameters and return data for books and shelves)
7. Utilities and algorithms (explanation of each module)
8. CSV data (format)
9. Request/response examples for book CRUDs
10. Operational notes
11. Users, loans, and reservations

---

1) Installation and Execution
- Follow instructions in [readme.md](readme.md).
- Essential commands:
  - Create environment: `python -m venv venv`
  - Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
  - Install dependencies: `pip install -r requirements.txt` — [requirements.txt](requirements.txt)
  - Run server: `uvicorn app.main:app --reload` — [app/main.py](app/main.py)

2) Project Structure (Files)
- Root files:
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
    - books:
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

3) Models and Schemas
- Book Model:
  - Class: [`Libro`](app/models/libro_model.py) — represents CSV record with fields (per CSV and service use): `isbn`, `titulo`, `autor`, `peso`, `valor`, `stock`, `paginas`, `editorial`, `idioma`.
  - Alternative/transformation: [`libro2_model.py`](app/models/libro2_model.py) and utilities in [app/utils/libros/convert_libro2.py](app/utils/libros/convert_libro2.py).
- Shelves:
  - [`Estanteria`](app/models/estanteria_model.py) and [`EstanteriaOptima`](app/models/estanteria_optima_model.py) — structures used by shelving algorithms.
- Loans / Reservations / Users:
  - Models: [`Prestamo`](app/models/prestamo_model.py), [`Reserva`](app/models/reserva_model.py), [`User`](app/models/user_model.py).
- Pydantic Schemas:
  - Book CRUD: [`LibroCreate`](app/schemas/libro_schema.py), [`LibroUpdate`](app/schemas/libro_schema.py), [`LibroOut`](app/schemas/libro_schema.py).
  - Shelf responses: [`EstanteriaResponse`](app/schemas/estanteria_schema.py), [`EstanteriasOptimasResponse`](app/schemas/estanteria2_schema.py), etc.
  - Other schemas for loans/reservations/users in [app/schemas/](app/schemas/).

4) Services (core logic)
- Main file: [app/services/libro_service.py](app/services/libro_service.py)
  - [`LibroService.load_books`](app/services/libro_service.py)
    - Reads `CSV_PATH` (`app/db/data/libros.csv`) with `csv.DictReader`.
    - Returns list of [`Libro`](app/models/libro_model.py).
  - [`LibroService.save_books`](app/services/libro_service.py)
    - Writes list of `Libro` to CSV. Uses fieldnames: `["isbn","titulo","autor","peso","valor","stock","paginas","editorial","idioma"]`.
  - [`LibroService.get_by_isbn`](app/services/libro_service.py)
    - Returns first book matching `isbn` or `None`.
  - [`LibroService.create`](app/services/libro_service.py)
    - Receives a `Libro` instance, avoids duplicates by `isbn`, adds and persists. Returns created book or `None` if ISBN exists.
  - [`LibroService.update`](app/services/libro_service.py)
    - Replaces entry by `isbn`, persists, and returns updated object or `None`.
  - [`LibroService.delete`](app/services/libro_service.py)
    - Deletes by `isbn` and persists. Returns `True` if deleted, `False` if not found.
  - [`LibroService.sort_by_isbn`](app/services/libro_service.py)
    - Uses [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py). Returns sorted list.
  - [`LibroService.get_by_price`](app/services/libro_service.py)
    - Uses [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py).
  - [`LibroService.deficient_shelf`](app/services/libro_service.py)
    - Brute-force logic: [`estanterias_fuerzaBruta`](app/utils/libros/estanterias_fuerzaBruta.py).
  - [`LibroService.optimal_shelf`](app/services/libro_service.py)
    - Uses backtracking: [`estanteria_backtracking`](app/utils/libros/estanteria_backtracking.py) and adapts with [`adaptar_estanterias_optimas`](app/utils/libros/adaptador_estanteria.py).
  - Calculations by author:
    - [`LibroService.total_value_by_author`](app/services/libro_service.py)
      - Filters books by author and calls [`valor_total_recursivo_con_libros`](app/utils/libros/recursion_pila.py).
      - Returns dict: `{"total_value": total, "books": [titles...]}` or `None` if no books by author.
    - [`LibroService.average_weight_by_author`](app/services/libro_service.py)
      - Filters books by author and calls [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py).
      - Returns dict: `{"average_weight": avg, "books": [titles...]}` or `None`.

5) Controllers
- Main book controller: [app/controllers/crudLibros.py](app/controllers/crudLibros.py)
  - Methods and mapping:
    - `list_books()` → calls [`LibroService.load_books`](app/services/libro_service.py).
    - `get_book(isbn)` → calls [`LibroService.get_by_isbn`](app/services/libro_service.py); raises `HTTPException(404)` if not found.
    - `create_book(data: LibroCreate)` → constructs `Libro(**data.dict())` and calls [`LibroService.create`](app/services/libro_service.py); raises `HTTPException(400)` if duplicate ISBN.
    - `update_book(isbn, data: LibroUpdate)` → creates `Libro(isbn=isbn, **data.dict())` and calls [`LibroService.update`](app/services/libro_service.py); raises `HTTPException(404)` if not found.
    - `delete_book(isbn)` → calls [`LibroService.delete`](app/services/libro_service.py); raises `HTTPException(404)` if not found.
    - Auxiliary endpoints: `books_sorted_by_isbn`, `books_sorted_by_price`, `deficient_shelf`, `optimal_shelf`, `total_value_author`, `average_weight_author` — all delegate to services and raise 404 if applicable.

6) Routes / Endpoints (input/output)
- File: [app/routes/libro_routes.py](app/routes/libro_routes.py)
- Prefix: `/books` (tag "Books")
- Main endpoints:
  - GET /books/
    - Calls [`LibroController.list_books`](app/controllers/crudLibros.py)
    - Response model: `List[LibroOut]`
  - GET /books/{isbn}
    - Path param: `isbn: str`
    - Response model: `LibroOut`
    - 404 if not found
  - POST /books/
    - Body: `LibroCreate` (JSON)
    - Response: `LibroOut` created
    - 400 if duplicate ISBN
  - PUT /books/{isbn}
    - Path param: `isbn: str`
    - Body: `LibroUpdate`
    - Response: `LibroOut` updated or 404
  - DELETE /books/{isbn}
    - Response: `{ "message": "Book deleted" }` or 404
  - GET /books/sorted/isbn
    - Returns `List[LibroOut]` sorted by ISBN
  - GET /books/sorted/price
    - Returns `List[LibroOut]` sorted by price
  - GET /books/shelf/deficient
    - Returns `List[EstanteriaResponse]`
  - GET /books/shelf/optimal
    - Returns `EstanteriasOptimasResponse`
  - GET /books/author/{author}/total-value
    - Path param: `author: str`
    - Returns `{"author": <author>, "total_value": <float>, "books": [titles...]}` or 404
  - GET /books/author/{author}/average-weight
    - Path param: `author: str`
    - Returns `{"author": <author>, "average_weight": <float>, "books": [titles...]}` or 404

7) Utilities and Algorithms (detailed explanation)
- ISBN sorting
  - [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py)
  - Receives list of `Libro`, returns new list sorted by `isbn`
- Sorting by price
  - [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py)
  - Sorts list by `valor` (float)
- Shelving (two approaches)
  - Brute force: [`estanterias_fuerzaBruta`](app/utils/libros/estanterias_fuerzaBruta.py)
    - Generates all combinations/partitions (exponential cost), returns shelves with defect indicators
  - Backtracking: [`estanteria_backtracking`](app/utils/libros/estanteria_backtracking.py)
    - Finds optimal solution with pruning; returns structure transformed by [`adaptar_estanterias_optimas`](app/utils/libros/adaptador_estanteria.py)
- Recursion examples
  - `recursion_pila.py` — [`valor_total_recursivo_con_libros`](app/utils/libros/recursion_pila.py)
    - Stack recursion: `valor_total_recursivo_con_libros(books, index)`; base case `index < 0` returns `(0, [])`. Accumulates value and titles on stack unwind.
  - `recursion_cola.py` — [`peso_promedio_tail_con_libros`](app/utils/libros/recursion_cola.py)
    - Tail recursion style; calculates average weight of books list and returns titles; prints trace to console.

8) CSV Data (Format)
- Location: [app/db/data/libros.csv](app/db/data/libros.csv)
- Fields (header written by `save_books`):
  - `isbn`, `titulo`, `autor`, `peso`, `valor`, `stock`, `paginas`, `editorial`, `idioma`
- Other CSVs:
  - prestamos.csv, reservas.csv, usuarios.csv

9) Request/Response Examples (Books)
- GET /books/
  - Response: `[ { "isbn": "123", "titulo":"X", "autor":"Y", "peso": "0.5", "valor":"10.0", "stock":"2", "paginas":"100", "editorial":"E", "idioma":"es" }, ... ]`
- GET /books/{isbn}
  - Response 200: `{ ...LibroOut... }`
  - Response 404: `{ "detail": "Book not found" }`
- POST /books/
  - Body example:
    ```json
    {
      "isbn": "9781234567897",
      "titulo": "My Book",
      "autor": "Author Ex",
      "peso": "0.5",
      "valor": "15.5",
      "stock": "3",
      "paginas": "200",
      "editorial": "Editorial S.A.",
      "idioma": "es"
    }
    ```
  - Response: created resource
  - 400 if ISBN exists
- PUT /books/{isbn}
  - Response: updated book or 404
- DELETE /books/{isbn}
  - Response: `{ "message": "Book deleted" }` or 404

10) Operational Notes
- All read/write services use CSV and rewrite full file per operation (not concurrent/transactional).
- Validation should be defined in Pydantic schemas.
- Performance considerations: `estanterias_fuerzaBruta` costly; `load_books()` reads CSV every call.
- Tests recommended for CRUD, shelving algorithms, recursive utilities.
- Logging: recursive functions print traces, should use proper logging.

---

11) Loans, Reservations, and Users — Complete Documentation

General Summary
- These three areas follow the same architecture as Books: routes → controllers → services → models → schemas → CSV persistence.
- Documentation covers module purpose, parameters, return values, and usage examples.

A. Loans (Prestamos)
1. Model and schema
- Model `Loan`:
  - Fields: id, isbn, user_id, loan_date, return_date (optional), status (e.g., "active", "returned")
- Schemas:
  - `LoanCreate`, `LoanUpdate`, `LoanOut`

2. Service
- load_loans(), save_loans(list)
- create_loan(data)
  - Validates book existence (isbn) and user existence (user_id)
  - Checks stock and decrements if successful
  - Generates unique id, persists, returns Loan
- update_loan(id, changes)
  - Applies changes (e.g., mark returned) and persists
- delete_loan(id)
  - Deletes record by id and persists

3. Controller — HTTP contracts
- GET /loans/
- GET /loans/{id}
- POST /loans/
- PUT /loans/{id}
- DELETE /loans/{id}

4. CSV
- Header example: id,isbn,user_id,loan_date,return_date,status

5. Examples
- Create loan, mark returned, etc.

B. Reservations (Reservas)
- Model `Reservation`: id, isbn, user_id, reservation_date, status
- Schemas: `ReservationCreate`, `ReservationUpdate`, `ReservationOut`
- Service: load_reservations(), save_reservations(list), create/update/convert_to_loan
- Controller: GET/POST/PUT/DELETE
- CSV header: id,isbn,user_id,reservation_date,status
- Examples: create reservation

C. Users (Usuarios)
- Model `User`: id, name, email, phone?, address?, registration_date
- Schemas: `UserCreate`, `UserUpdate`, `UserOut`
- Service: load_users(), save_users(), create/get/update/delete
- Controller: GET/POST/PUT/DELETE
- CSV header: id,name,email,phone,address,registration_date
- Examples: create userHere’s the full translation of your documentation into English:

```markdown
// ...existing code...
# Complete Project Documentation

Brief Summary
- FastAPI API for managing books, loans, reservations, and users.
- Data persisted in CSV files under `app/db/data/`.
- Logic separated in layers: routes → controllers → services → models → utils.

Table of Contents
1. Installation and Execution
2. Project Structure (file list)
3. Models and Schemas (books)
4. Services (books)
5. Controllers (validations and exceptions for books and shelves)
6. Routes / Endpoints (how they receive parameters and return data for books and shelves)
7. Utilities and Algorithms (module explanations)
8. CSV Data (format)
9. Request/Response Examples for book CRUDs
10. Operational Notes
11. Users, Loans, and Reservations

---

1) Installation and Execution
- Follow instructions in [readme.md](readme.md).
- Essential commands:
  - Create environment: `python -m venv venv`
  - Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
  - Install dependencies: `pip install -r requirements.txt` — [requirements.txt](requirements.txt)
  - Run server: `uvicorn app.main:app --reload` — [app/main.py](app/main.py)

2) Project Structure (Files)
- Root files:
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
    - books:
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

3) Models and Schemas
- Book Model:
  - Class: [`Libro`](app/models/libro_model.py) — represents CSV record with fields: `isbn`, `titulo`, `autor`, `peso`, `valor`, `stock`, `paginas`, `editorial`, `idioma`.
  - Alternative/Transformation: [`libro2_model.py`](app/models/libro2_model.py) with utilities in [convert_libro2.py](app/utils/libros/convert_libro2.py).
- Shelves:
  - [`Estanteria`](app/models/estanteria_model.py) and [`EstanteriaOptima`](app/models/estanteria_optima_model.py) — structures used by shelf algorithms.
- Loans / Reservations / Users:
  - Models: [`Prestamo`](app/models/prestamo_model.py), [`Reserva`](app/models/reserva_model.py), [`User`](app/models/user_model.py).
- Pydantic Schemas:
  - Book CRUD: [`LibroCreate`](app/schemas/libro_schema.py), [`LibroUpdate`](app/schemas/libro_schema.py), [`LibroOut`](app/schemas/libro_schema.py).
  - Shelf responses: [`EstanteriaResponse`](app/schemas/estanteria_schema.py), [`EstanteriasOptimasResponse`](app/schemas/estanteria2_schema.py), etc.
  - Other schemas for loans/reservations/users in [app/schemas/](app/schemas/).

4) Services (Core Logic)
- Main file: [libro_service.py](app/services/libro_service.py)
  - [`LibroService.cargar_libros`](app/services/libro_service.py): Reads CSV_PATH (`libros.csv`) and returns a list of `Libro`.
  - [`LibroService.guardar_libros`](app/services/libro_service.py): Writes list of `Libro` to CSV.
  - [`LibroService.obtener_por_isbn`](app/services/libro_service.py): Returns first book with given `isbn` or `None`.
  - [`LibroService.crear`](app/services/libro_service.py): Creates book if ISBN not duplicated.
  - [`LibroService.actualizar`](app/services/libro_service.py): Updates book by ISBN.
  - [`LibroService.eliminar`](app/services/libro_service.py): Deletes book by ISBN.
  - [`LibroService.ordernar_por_isbn`](app/services/libro_service.py): Sorts books by ISBN.
  - [`LibroService.obtener_por_precio`](app/services/libro_service.py): Sorts books by price.
  - [`LibroService.estanteria_deficiente`](app/services/libro_service.py): Brute-force shelf algorithm.
  - [`LibroService.estanteria_optima`](app/services/libro_service.py): Backtracking optimal shelf.
  - Calculations by author:
    - [`valor_total_por_autor`](app/services/libro_service.py): Recursive total value per author.
    - [`peso_promedio_por_autor`](app/services/libro_service.py): Recursive average weight per author.

5) Controllers
- Main book controller: [crudLibros.py](app/controllers/crudLibros.py)
  - Methods: list_books(), get_book(), create_book(), update_book(), delete_book(), sorted_by_isbn(), sorted_by_price(), deficient_shelf(), optimal_shelf(), total_value_by_author(), average_weight_by_author()

6) Routes / Endpoints
- Prefix: `/libros` (tag: "Books")
- GET /libros/ → list all books
- GET /libros/{isbn} → get book by ISBN
- POST /libros/ → create book
- PUT /libros/{isbn} → update book
- DELETE /libros/{isbn} → delete book
- GET /libros/ordenados/isbn → books sorted by ISBN
- GET /libros/ordenados/precio → books sorted by price
- GET /libros/estanteria/deficiente → deficient shelves
- GET /libros/estanteria/optima → optimal shelves
- GET /libros/autor/{autor}/valor-total → total value by author
- GET /libros/autor/{autor}/peso-promedio → average weight by author

7) Utilities and Algorithms
- ISBN sorting: [`libros_ordenados_isbn`](app/utils/libros/librosOrdenados.py)
- Price sorting: [`ordenar_libros_por_precio`](app/utils/libros/libroSort.py)
- Shelves: brute-force and backtracking
- Recursive calculations: total value and average weight

8) CSV Data
- Location: [libros.csv](app/db/data/libros.csv)
- Fields: isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma
- Other CSVs: prestamos.csv, reservas.csv, usuarios.csv

9) Request/Response Examples
- GET /libros/ → List of books
- GET /libros/{isbn} → Book details
- POST /libros/ → Create book
- PUT /libros/{isbn} → Update book
- DELETE /libros/{isbn} → Delete book

10) Operational Notes
- CSV persistence is not concurrent or transactional.
- Validate inputs in Pydantic schemas.
- Heavy operations (brute-force shelves) may be costly.
- Recursive functions print traces; consider using logging.

11) Loans, Reservations, and Users — Full Documentation

General Summary
- Same architecture as books: routes → controllers → services → models → schemas → CSV persistence.
- Documentation includes module behavior, parameters, return values, and usage examples.

A. Loans
- Model: Prestamo (id, isbn, user_id, loan_date, return_date, status)
- Schemas: PrestamoCreate, PrestamoUpdate, PrestamoOut
- Service: load_loans(), save_loans(), create_loan(), update_loan(), delete_loan()
- Controller: GET /loans/, GET /loans/{id}, POST /loans/, PUT /loans/{id}, DELETE /loans/{id}
- CSV header: id,isbn,user_id,loan_date,return_date,status
- Examples: creating loan, marking returned

B. Reservations
- Model: Reserva (id, isbn, user_id, reservation_date, status)
- Schemas: ReservaCreate, ReservaUpdate, ReservaOut
- Service: load_reservations(), save_reservations(), create_reservation(), update_reservation(), convert_to_loan()
- Controller: GET /reservations/, GET /reservations/{id}, POST /reservations/, PUT /reservations/{id}, DELETE /reservations/{id}
- CSV header: id,isbn,user_id,reservation_date,status
- Examples: creating reservation

C. Users
- Model: User (id, name, email, phone, address, registration_date)
- Schemas: UserCreate, UserUpdate, UserOut
- Service: load_users(), save_users(), create_user(), get_user_by_id(), get_user_by_email(), update_user(), delete_user()
- Controller: GET /users/, GET /users/{id}, POST /users/, PUT /users/{id}, DELETE /users/{id}
- CSV header: id,name,email,phone,address,registration_date
- Examples: creating user

D. Module Integration — Rules and Flows
- Cross-validation: check existence, stock, duplicates
- Atomicity and concurrency: CSV is not atomic/concurrent; handle at application level
- ID handling: use unique IDs (UUID or incremental)

E. HTTP Contracts and Status Codes
- 200 OK: successful GET/PUT
- 201 Created: successful POST
- 204 No Content: successful DELETE
- 400 Bad Request: input validation errors
- 404 Not Found: resource not found
- 409 Conflict: state conflicts (optional)

F. Recommended Tests
- Unit tests for create/update/delete users, reservations, loans
- Integrated flows: reservation → loan, loan → returned
- Error cases: loan without stock, duplicate reservation, delete user with associated resources

G. Practical Next Steps
1. Verify model and schema field names
2. Add Pydantic validations (dates, emails)
3. Implement logging instead of print
4. Add unit tests for services and controllers

End of Loans, Reservations, and Users Documentation

