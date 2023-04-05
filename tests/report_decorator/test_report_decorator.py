from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import pytest

AZUL = "\033[36m"
VERDE = "\033[32m"
VERMELHO = "\033[31m"
RESET = "\033[0m"


@pytest.fixture
def lista_de_produtos():
    return [
            {
                "id": "1",
                "nome_do_produto": "Nicotine Polacrilex",
                "nome_da_empresa": "Target Corporation",
                "data_de_fabricacao": "2021-02-18",
                "data_de_validade": "2023-09-17",
                "numero_de_serie": "CR25 1551 4467 2549 4402 1",
                "instrucoes_de_armazenamento": "instrucao 1"
            },
            {
                "id": "2",
                "nome_do_produto": "fentanyl citrate",
                "nome_da_empresa": "Target Corporation",
                "data_de_fabricacao": "2020-12-06",
                "data_de_validade": "2023-12-25",
                "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
                "instrucoes_de_armazenamento": "instrucao 2"
            }
            ]


def test_decorar_relatorio(lista_de_produtos):
    simple_report = SimpleReport()

    colorido = ColoredReport(simple_report).generate(lista_de_produtos)

    texto1 = 'Data de fabricação mais antiga:'
    texto2 = 'Data de validade mais próxima:'
    texto3 = 'Empresa com mais produtos:'

    relatorio = (
        f"{VERDE}{texto1}{RESET} {AZUL}2020-12-06{RESET}\n"
        f"{VERDE}{texto2}{RESET} {AZUL}2023-09-17{RESET}\n"
        f"{VERDE}{texto3}{RESET} {VERMELHO}Target Corporation{RESET}"
    )

    assert colorido == relatorio
