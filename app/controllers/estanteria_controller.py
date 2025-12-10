from fastapi import HTTPException
from app.services.libro_service import LibroService
from app.algorithms.estanterias import combinaciones_peligrosas, estanteria_optima

# Controlador del módulo estanterías: fuerza bruta y backtracking
class EstanteriaController:

    @staticmethod
    # Devuelve combinaciones de 4 libros con peso > 8 kg (fuerza bruta)
    def estanteria_deficiente():
        libros = LibroService.cargar_libros()

        if len(libros) < 4:
            raise HTTPException(
                status_code=400,
                detail="Se necesitan al menos 4 libros para analizar combinaciones."
            )

        resultado = combinaciones_peligrosas(libros)

        return {
            "total_combinaciones_encontradas": len(resultado),
            "combinaciones": [
                {
                    "peso_total": combo["peso_total"],
                    "libros": [
                        {
                            "isbn": l.isbn,
                            "titulo": l.titulo,
                            "peso": l.peso,
                            "valor": l.valor
                        }
                        for l in combo["libros"]
                    ]
                }
                for combo in resultado
            ]
        }

    @staticmethod
    # Devuelve la combinación óptima por valor sin exceder 8 kg (backtracking)
    def estanteria_optima():
        libros = LibroService.cargar_libros()

        resultado = estanteria_optima(libros)

        return {
            "mejor_valor": resultado["mejor_valor"],
            "mejor_combinacion": [
                {
                    "isbn": l.isbn,
                    "titulo": l.titulo,
                    "peso": l.peso,
                    "valor": l.valor
                }
                for l in resultado["mejor_combinacion"]
            ],
            "exploracion": resultado["exploracion"]  # puedes ocultarlo si quieres
        }
