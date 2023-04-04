from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(1, 'computador', 'tekcompany',
                      '2023-03-25', '2027-03-25', "5497", "guardar na caixa")
    assert produto.id == 1
    assert produto.nome_do_produto == 'computador'
    assert produto.nome_da_empresa == 'tekcompany'
    assert produto.data_de_fabricacao == '2023-03-25'
    assert produto.data_de_validade == '2027-03-25'
    assert produto.numero_de_serie == '5497'
    assert produto.instrucoes_de_armazenamento == 'guardar na caixa'
