import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _, path, tipo_relatorio = sys.argv

    if path.endswith("csv"):
        relatorio = InventoryRefactor(CsvImporter).import_data(
            path, tipo_relatorio
        )
        sys.stdout.write(relatorio)

    elif path.endswith("json"):
        relatorio = InventoryRefactor(JsonImporter).import_data(
            path, tipo_relatorio
        )
        sys.stdout.write(relatorio)

    elif path.endswith("xml"):
        relatorio = InventoryRefactor(XmlImporter).import_data(
            path, tipo_relatorio
        )
        sys.stdout.write(relatorio)
