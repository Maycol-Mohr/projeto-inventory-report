import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, extensao_do_arquivo: str):
        if not extensao_do_arquivo.endswith('xml'):
            raise ValueError('Arquivo inválido')

        with open(extensao_do_arquivo) as file:
            ler_xml = xmltodict.parse(file.read())['dataset']['record']

        return ler_xml
