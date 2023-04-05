import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, extensao_do_arquivo: str):
        if not extensao_do_arquivo.endswith('json'):
            raise ValueError('Arquivo inválido')

        with open(extensao_do_arquivo) as file:
            content = file.read()
            ler_relatorio_json = json.loads(content)

        return ler_relatorio_json
