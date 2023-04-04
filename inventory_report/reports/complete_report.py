from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls,  produtos: 'list[dict]'):
        relatorio_simples = super().generate(produtos)

        empresa = [
            produto['nome_da_empresa']
            for produto in produtos
        ]

        quantidade_por_empresa = Counter(empresa)
        relatorio = ''
        for empresa, quantidade in quantidade_por_empresa.items():
            relatorio += f'- {empresa}: {quantidade}\n'

        return (
            f'{relatorio_simples}'
            f'\nProdutos estocados por empresa:\n'
            f'{relatorio}'
        )
