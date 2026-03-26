def min_max(data):
   
    if not data:
        print("No se puede normalizar una lista vacía")

    if len(data) == 1:
        return [0.0]

    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val

    if range_val == 0:
        print("Todos los valores son iguales, no se puede normalizar")

    return [(x - min_val) / range_val for x in data]


def z_score(data, mean=None, std=None):
    
    if not data:
        print("No se puede estandarizar una lista vacía")

    # Calcular media si no se proporciona
    if mean is None:
        mean = sum(data) / len(data)

    if std == 0:
        print("La desviación estándar es cero, no se puede estandarizar")

    return [(x - mean) / std for x in data]
