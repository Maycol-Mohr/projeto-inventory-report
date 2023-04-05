from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, tipo_relatorio: str):
        lista_produtos = self.importer.import_data(path)
        for produto in lista_produtos:
            self.data.append(produto)

    def __iter__(self):
        return InventoryIterator(self.data)
