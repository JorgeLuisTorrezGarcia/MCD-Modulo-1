from analysis import calculate_statistics, load_data, clean_missing_values

def main():
    # Load data from a CSV file/cargar datos desde el csv
    df = load_data('data.csv')

    print("datos originales:")
    print(df)

    #clean data/limpiar datos
    df_clean= clean_missing_values(df)
    print("\ndatos limpios:")
    print(df_clean)

    #analyze data/analizar datos
    ages = df_clean['edad'].tolist()  # Convertir la columna 'age' a una lista
    stats = calculate_statistics(ages)

    print("\nestadísticas de edad:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value:.2f}")

# Run the main function/ correr si es el archivo principal
if __name__ == "__main__":    
    main()


    
    

