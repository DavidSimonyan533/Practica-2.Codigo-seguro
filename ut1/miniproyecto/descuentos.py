"""PPS UT1 · Mini-proyecto para la práctica de pruebas y cobertura (PPS-E2).

INCIDENCIA #17 (reportada por soporte): un cliente aplicó un cupón del 150 %
y la tienda le devolvió un precio NEGATIVO (le "regalamos" dinero).
Tu trabajo: escribir primero el TEST DE REGRESIÓN que reproduce el fallo,
verlo en rojo, corregir el código y verlo en verde.
"""


import math


def aplicar_descuento(precio: float, pct: float) -> float:
    if not math.isfinite(precio):
        raise ValueError("el precio debe ser finito")

    if not math.isfinite(pct):
        raise ValueError("el descuento debe ser finito")

    if precio < 0:
        raise ValueError("precio negativo")

    if not 0 <= pct <= 100:
        raise ValueError("descuento fuera de rango")

    resultado = round(precio * (1 - pct / 100), 2)

    if not math.isfinite(resultado) or resultado < 0:
        raise ValueError("el resultado no es válido")

    return resultado


def resultado_valido(precio, resultado):
    return (
        math.isfinite(precio)
        and precio >= 0
        and math.isfinite(resultado)
        and resultado >= 0
        and resultado <= round(precio, 2)
    )

def test_regresion_valores_no_finitos():
    import pytest

    valores_no_finitos = [
        float("nan"),
        float("inf"),
        float("-inf"),
    ]

    for valor in valores_no_finitos:
        with pytest.raises(ValueError):
            aplicar_descuento(valor, 10)

        with pytest.raises(ValueError):
            aplicar_descuento(100, valor)
