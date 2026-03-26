from .export_strategy import ExportStrategy
class Exporter:
    """
    El Contexto define la interfaz de interés para los clientes. Mantiene una
    referencia a un objeto de Estrategia, pero no conoce la clase concreta.
    """

    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        # Permite reemplazar la Estrategia en tiempo de ejecución.
        self._strategy = strategy

    def do_export(self, data: list[dict]) -> str:
        """
        El Contexto delega parte del trabajo al objeto de Estrategia en lugar de
        implementar múltiples versiones del algoritmo por su cuenta.
        """
        print(
            f"Exporter: Exportando datos usando la estrategia {self._strategy.__class__.__name__}"
        )
        result = self._strategy.export(data)
        return result
