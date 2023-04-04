import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, tipo_relatorio: str):
        with open(path, encoding='utf-8') as file:
            arquivo_prod = csv.DictReader(file, delimiter=',', quotechar='"')
            ler_produtos = []
            for produto in arquivo_prod:
                ler_produtos.append(produto)
            ler_produtos = list(ler_produtos)

        if tipo_relatorio == 'simples':
            return SimpleReport.generate(ler_produtos)
        elif tipo_relatorio == 'completo':
            return CompleteReport.generate(ler_produtos)
        raise ValueError(
            'Erro ao ler o arquivo de relatório'
        )
