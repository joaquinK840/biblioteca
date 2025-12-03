from app.schemas.estanterias_optimas_schema import (
    EstanteriaOptima,
    EstanteriasOptimasResponse
)

def adaptar_estanterias_optimas(resultado_algo):
    """
    Convierte el resultado del algoritmo de backtracking
    al schema EstanteriasOptimasResponse.
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
