
from app.schemas.estanterias_optimas_schema import (EstanteriaOptima,
                                                    EstanteriasOptimasResponse)


def adaptar_estanterias_optimas(resultado_algo):
    """Adaptador: convierte la salida del algoritmo de estanterías al schema de respuesta.
    
    Función:
    - adaptar_estanterias_optimas(resultado_algo)
      - Recibe:
        * resultado_algo: dict con clave "resultado" conteniendo lista de dicts con claves:
          - "estanteria", "libros", "peso_total", "precio_total"
      - Devuelve:
        * Instancia de EstanteriasOptimasResponse (schema) con la lista de EstanteriaOptima.
      - Requiere:
        * Que los schemas EstanteriaOptima y EstanteriasOptimasResponse estén disponibles e importables.
    """
    estanterias = []

    for est in resultado_algo["resultado"]:
        estanterias.append(
            EstanteriaOptima(
                estanteria=est["estanteria"],
                libros=est["libros"],
                peso_total=est["peso_total"],
                precio_total=est["precio_total"]
            )
        )

    return EstanteriasOptimasResponse(resultado=estanterias)
