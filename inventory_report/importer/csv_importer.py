import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, extensao_do_arquivo: str):
        if '.csv' not in extensao_do_arquivo:
            raise ValueError('Arquivo inválido')

        with open(extensao_do_arquivo, encoding='utf-8') as file:
            arquivo_csv = csv.DictReader(file, delimiter=',', quotechar='"')
            ler_produtos = []
            for produto in arquivo_csv:
                ler_produtos.append(produto)
                ler_produtos_csv = list(ler_produtos)

            return ler_produtos_csv
            # return list(arquivo_csv) resolucao acima em 1 linha(outra forma)
