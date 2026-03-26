def remove_nulls(data):
    
    if not isinstance(data, list):
        print("El parámetro debe ser una lista")

    return [x for x in data if x is not None]


def replace_missing_values(data, replacement_value):
    
    if not isinstance(data, list):
        print("El parámetro debe ser una lista")

    return [replacement_value if x is None else x for x in data]




def replace_missing_with_mean(data):
    
    if not isinstance(data, list):
        print("El parámetro debe ser una lista")

    # Filtrar valores no nulos
    non_null_values = [x for x in data if x is not None]

    if not non_null_values:
        raise ValueError("No hay valores no nulos para calcular la media")

    # Calcular la media de valores no nulos
    mean_value = sum(non_null_values) / len(non_null_values)

    # Reemplazar nulos con la media
    return [mean_value if x is None else x for x in data]


def remove_duplicates(data, keep_order=True):
    
    if not isinstance(data, list):
        print("El parámetro debe ser una lista")

    if keep_order:
        seen = set()
        result = []
        for x in data:
            if x not in seen:
                seen.add(x)
                result.append(x)
        return result
    else:
        return list(set(data))
