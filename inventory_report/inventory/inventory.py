from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
# import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path: str, tipo_relatorio: str):

        lista_produtos = cls.ler_arquivo(path)
        if tipo_relatorio == 'simples':
            return SimpleReport.generate(lista_produtos)
        elif tipo_relatorio == 'completo':
            return CompleteReport.generate(lista_produtos)
        raise ValueError(
            'Erro ao ler o arquivo de relatório'
        )

    @classmethod
    def ler_arquivo(cls, path: str):
        if path.endswith('csv'):
            with open(path, encoding='utf-8') as file:
                aquivo_csv = csv.DictReader(file, delimiter=',', quotechar='"')
                ler_produtos = []
                for produto in aquivo_csv:
                    ler_produtos.append(produto)
                ler_produtos = list(ler_produtos)
                return ler_produtos

        elif path.endswith('json'):
            with open(path) as file:
                content = file.read()
                ler_relatorio = json.loads(content)
                return ler_relatorio

        # with open(path) as file:
        #     tree = ET.parse(file)  # leitura do arquivo
        #     root = tree.getroot()
