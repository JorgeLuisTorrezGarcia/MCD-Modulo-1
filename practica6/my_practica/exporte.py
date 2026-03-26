from .export_strategy import ExportStrategy

class Exporter:
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        self._strategy = strategy

    def do_export(self, data: list[dict[str,any]])->str:
        print(f"Exportando datos uando la estrategia: {self._strategy.__class__.__name__}")
        print(self._strategy.__class__)

        result = self._strategy.export(data)
        return result
