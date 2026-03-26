from .auto_data import autos_disponibles, costo_alquiler


def obtener_autos_disponibles():
    """
    Obtiene la lista de todos los autos disponibles para alquilar.

    Returns:
        list: Lista con los nombres de todos los modelos de autos disponibles.

    Example:
        >>> autos = obtener_autos_disponibles()
        >>> print(autos)
        ['Toyota Corolla', 'Hyundai Tucson', 'Kia Rio', 'Nissan Versa', 'Suzuki Swift']
    """
    return list(autos_disponibles.keys())


def obtener_costo_alquiler(modelo_auto):
    """
    Obtiene el costo diario de alquiler de un modelo específico de auto.

    Args:
        modelo_auto (str): Nombre del modelo de auto.

    Returns:
        int or None: Costo diario de alquiler si el auto existe, None si no existe.

    Example:
        >>> costo = obtener_costo_alquiler("Toyota Corolla")
        >>> print(costo)
        45
    """
    return costo_alquiler.get(modelo_auto)


def auto_existe(modelo_auto):
    """
    Verifica si un modelo de auto existe en el sistema.

    Args:
        modelo_auto (str): Nombre del modelo de auto a verificar.

    Returns:
        bool: True si el auto existe, False en caso contrario.

    Example:
        >>> existe = auto_existe("Toyota Corolla")
        >>> print(existe)
        True
    """
    return modelo_auto in autos_disponibles


def obtener_cantidad_total_autos():
    """
    Calcula la cantidad total de autos que tiene la empresa.

    Returns:
        int: Suma total de todas las unidades disponibles.

    Example:
        >>> total = obtener_cantidad_total_autos()
        >>> print(total)
        25
    """
    return sum(autos_disponibles.values())
