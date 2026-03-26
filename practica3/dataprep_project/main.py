
from datapreputils import (
    # Funciones de estadística
    mean,
    median,
    std_dev,
    mode,
    harmonic_mean,
    geometric_mean,
    # Funciones de normalización
    min_max,
    z_score,
    # Funciones de limpieza
    remove_nulls,
    replace_missing_values,
    replace_missing_with_mean,
    remove_duplicates,
)


def print_section(title):
    """Imprime un título de sección formateado."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():

    # Datos de ejemplo
    data = [10, 24, 28, 40, 50]
    data_with_nulls = [10, None, 20, 28, None, 40, 50]
    data_with_duplicates = [10, 20, 20, 28, 40, 40, 50]

    # ========== FUNCIONES DE ESTADÍSTICA ==========
    print_section("FUNCIONES DE ESTADÍSTICA")

    print(f"Datos originales: {data}\n")

    m = mean(data)
    med = median(data)
    std = std_dev(data)
    mod = mode([10, 24, 24, 28, 40, 50])
    h_mean = harmonic_mean(data)
    g_mean = geometric_mean(data)

    print(f"  Media (aritmética):     {m:.2f}")
    print(f"  Mediana:               {med:.2f}")
    print(f"  Desviación estándar:   {std:.2f}")
    print(f"  Moda:                  {mod}")
    print(f"  Media armónica:        {h_mean:.2f}")
    print(f"  Media geométrica:      {g_mean:.2f}")

    # ========== FUNCIONES DE NORMALIZACIÓN ==========
    print_section("FUNCIONES DE NORMALIZACIÓN")

    print(f"Datos originales: {data}\n")

    normalized_minmax = min_max(data)
    normalized_zscore = z_score(data, m, std)

    print(f"  Normalización Min-Max:")
    print(f"  {[f'{x:.4f}' for x in normalized_minmax]}\n")

    print(f"  Normalización Z-Score:")
    print(f"  {[f'{x:.4f}' for x in normalized_zscore]}\n")

    # ========== FUNCIONES DE LIMPIEZA ==========
    print_section("FUNCIONES DE LIMPIEZA DE DATOS")

    print(f"Datos con valores nulos: {data_with_nulls}\n")

    cleaned_data = remove_nulls(data_with_nulls)
    print(f"  Eliminando valores nulos:")
    print(f"  {cleaned_data}\n")

    replaced_data = replace_missing_values(data_with_nulls, 0)
    print(f"  Reemplazando nulos con 0:")
    print(f"  {replaced_data}\n")

    replaced_mean = replace_missing_with_mean(data_with_nulls)
    print(f"  Reemplazando nulos con la media:")
    print(f"  {[f'{x:.2f}' for x in replaced_mean]}\n")

    print(f"Datos con duplicados: {data_with_duplicates}\n")

    unique_data = remove_duplicates(data_with_duplicates)
    print(f"  Eliminando duplicados:")
    print(f"  {unique_data}\n")

    # ========== EJEMPLO INTEGRADO ==========
    print_section("EJEMPLO INTEGRADO: PIPELINE DE PREPARACIÓN DE DATOS")

    # Simular un dataset con problemas comunes
    raw_data = [100, None, 150, 150, 200, None, 250, 300]
    print(f"Datos crudos: {raw_data}\n")

    # Etapa 1: Limpieza
    print("Etapa 1: Limpianza de datos")
    step1 = replace_missing_with_mean(raw_data)
    print(f"  Después de llenar nulos: {[f'{x:.2f}' for x in step1]}\n")

    # Etapa 2: Eliminar duplicados
    print("Etapa 2: Eliminar duplicados")
    step2 = remove_duplicates(step1)
    print(f"  Después de eliminar duplicados: {[f'{x:.2f}' for x in step2]}\n")

    # Etapa 3: Análisis estadístico
    print("Etapa 3: Análisis estadístico")
    m2 = mean(step2)
    med2 = median(step2)
    std2 = std_dev(step2)
    print(f"  Media: {m2:.2f}")
    print(f"  Mediana: {med2:.2f}")
    print(f"  Desviación estándar: {std2:.2f}\n")

    # Etapa 4: Normalización
    print("Etapa 4: Normalización de datos")
    step4 = z_score(step2, m2, std2)
    print(f"  Datos normalizados (Z-Score): {[f'{x:.4f}' for x in step4]}\n")

    print_section("PROCESO COMPLETADO")
    print("El paquete datapreputils facilita la preparación de datos\n")


if __name__ == "__main__":
    main()
