
from app.schemas.estanterias_optimas_schema import (EstanteriaOptima,
                                                    EstanteriasOptimasResponse)


# Adapter: convert algorithm result into API response schemas
def adaptar_estanterias_optimas(resultado_algo):
    """Adapter: converts the shelf algorithm output into the response schema.

    Function:
    - adaptar_estanterias_optimas(resultado_algo)
      - Receives:
        * resultado_algo: dict with key "resultado" containing a list of dicts with keys:
          - "estanteria", "libros", "peso_total", "precio_total"
      - Returns:
        * EstanteriasOptimasResponse instance with a list of EstanteriaOptima objects.
      - Requires:
        * Schemas EstanteriaOptima and EstanteriasOptimasResponse to be importable.
    """
    estanterias = []  # List of EstanteriaOptima objects for the response

    for est in resultado_algo["resultado"]:
        # Build EstanteriaOptima from the algorithm's dict
        estanterias.append(
            EstanteriaOptima(
                estanteria=est["estanteria"],
                libros=est["libros"],
                peso_total=est["peso_total"],
                precio_total=est["precio_total"]
            )
        )

    # Wrap the list in the response schema
    return EstanteriasOptimasResponse(resultado=estanterias)
