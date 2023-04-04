from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(1, 'computador', 'tekcompany',
                      '2023-03-25', '2027-03-25', "5497", "guardar na caixa")

    relatorio = (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )

    assert repr(produto) == relatorio
