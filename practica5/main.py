from analysis import (
    load_data,
    clean_missing_values,
    calculate_age_statistics,
    calculate_salary_statistics,
    plot_ages,
    plot_salaries
)

"""
Juan Francisco Gareca Aguirre
Andrea Elizabeth Arana Ore
CLARA INES OLMEDO RODRIGUEZ
Oliver Ronald Camacho Velasco
JORGE LUIS TORREZ GARCIA
"""

def main():
    # Carga de datos
    df = load_data('data.csv')
    print("Datos originales:")
    print(df)
    print("-" * 30)

    # Limpieza de datos
    cleaned_df = clean_missing_values(df)
    print("\nDatos limpios:")
    print(cleaned_df)
    print("-" * 30)

    # Análisis de datos
    age_stats = calculate_age_statistics(cleaned_df['edad'])
    salary_stats = calculate_salary_statistics(cleaned_df['salario'])

    print("\nEstadísticas de Edad:")
    print(age_stats)
    print("\nEstadísticas de Salario:")
    print(salary_stats)
    print("-" * 30)

    # Visualización
    print("\nGenerando gráficos...")
    plot_ages(cleaned_df, filename='grafico_edades.png')
    plot_salaries(cleaned_df, filename='grafico_salarios.png')

if __name__ == '__main__':
    main()