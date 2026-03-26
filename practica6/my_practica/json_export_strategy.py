from .export_strategy import ExportStrategy
import json

class JsonExportStrategy(ExportStrategy):
    
    def export(self, data: list[dict[str,any]]) -> str:
        return json.dumps(data, indent=4)

