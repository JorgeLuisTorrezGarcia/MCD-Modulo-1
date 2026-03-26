from exporte import Exporte
from strategy_json import StrategyJson
from strategy_csv import StrategyCsv


def main():

    sample_data = [
        {"id": 1, "name": "Alice", "role": "Developer"},
        {"id": 2, "name": "Jorge", "role": "Architect"},
        {"id": 3, "name": "Charlie", "role": "Designer"},
    ]
    
    print("DATOS EXAMPLE")
    print(sample_data)
    
    exportar = Exporte(StrategyJson())
    
    json_output = exportar.do_export(sample_data)
    print(json_output)
    print("")
    
    exportar.set_strategy(StrategyCsv())
    csv_output = exportar.do_export(sample_data)
    print(csv_output)
    
if __name__ == "__main__":
    main()