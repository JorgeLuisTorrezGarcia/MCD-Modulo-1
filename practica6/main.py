from my_practica import Exporter, JsonExportStrategy, CsvExportStrategy

def main():
    sample_data = [
        {"id": 1, "name": "Alice", "role": "Developer"},
        {"id": 2, "name": "Jorge", "role": "Architect"},
        {"id": 3, "name": "Charlie", "role": "Designer"}
    ]

    print("--- DATOS DE PRUEBA ---")
    print(f'{sample_data} \n')

    exporter = Exporter(JsonExportStrategy())
    json_output =exporter.do_export(sample_data)
    print("--- JSON EXPORTADO ---")
    print(f'{json_output} \n')

    # Cliente cambia la estrategia a CSV en tiempo de ejecución
    exporter.set_strategy(CsvExportStrategy())
    csv_output = exporter.do_export(sample_data)
    print("--- Resultado CSV ---")
    print(csv_output)

if __name__ == "__main__":
    main()
    