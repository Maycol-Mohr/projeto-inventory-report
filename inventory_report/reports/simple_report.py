from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls,  produtos: 'list[dict]'):
        data_fabricacao = [
            produto['data_de_fabricacao']
            for produto in produtos
        ]

        data_de_validade = [
            produto['data_de_validade']
            for produto in produtos
        ]

        emprsa = [
            produto['nome_da_empresa']
            for produto in produtos
        ]

        data_mais_antiga = min(data_fabricacao)
        data_mais_proxima = str(date.max)

        for data in data_de_validade:
            if data <= data_mais_proxima and data >= str(date.today()):
                data_mais_proxima = data

        return (
            f'Data de fabricação mais antiga: {data_mais_antiga}\n'
            f'Data de validade mais próxima: {data_mais_proxima}\n'
            f'Empresa com mais produtos: {Counter(emprsa).most_common()[0][0]}'
        )
