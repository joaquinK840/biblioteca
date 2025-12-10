
from app.schemas.estanterias_optimas_schema import (EstanteriaOptima,
                                                    EstanteriasOptimasResponse)


# Convierte el resultado del algoritmo a los schemas de respuesta
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
    estanterias = []  # Lista de objetos EstanteriaOptima para la respuesta

    for est in resultado_algo["resultado"]:
        # Crear el objeto de estantería óptima a partir del dict del algoritmo
        estanterias.append(
            EstanteriaOptima(
                estanteria=est["estanteria"],
                libros=est["libros"],
                peso_total=est["peso_total"],
                precio_total=est["precio_total"]
            )
        )

      # Envolver la lista en el schema de respuesta
      return EstanteriasOptimasResponse(resultado=estanterias)
