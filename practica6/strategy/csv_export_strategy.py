from .export_strategy import ExportStrategy
import csv
import io


class CsvExportStrategy(ExportStrategy):
    # Implementa el algoritmo usando la Estrategia de exportación a CSV.

    def export(self, data: list[dict]) -> str:
        if not data:
            return ""

        output = io.StringIO()
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

        return output.getvalue()
