from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, tipo_relatorio: str):
        lista_produtos = self.importer.import_data(path)
        for produto in lista_produtos:
            self.data.append(produto)

        if tipo_relatorio == 'simples':
            return SimpleReport.generate(self.data)
        elif tipo_relatorio == 'completo':
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
