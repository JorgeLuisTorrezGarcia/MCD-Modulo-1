from export_file import ExportFile

class Exporte:
    
    def __init__(self, strategy: ExportFile):
        self._strategy = strategy
        
    def set_strategy(self, strategy: ExportFile):
        self._strategy=strategy
        
    def do_export(self, data:list[dict[str, any]])->str:
        print(f"Estrategia elegida: {self._strategy.__class__.__name__}")
        result = self._strategy.exportar(data)
        return result