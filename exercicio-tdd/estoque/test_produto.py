import pytest
from datetime import date, timedelta
from estoque.produto import Produto

def test_valor_total():
    p = Produto("Sabão", 10, 5)
    assert p.valor_total() == 50

def test_adicionar_remover_estoque():
    p = Produto("Café", 10, 10)
    p.adicionar_estoque(5)
    p.remover_estoque(3)
    assert p.quantidade == 12

def test_estoque_baixo():
    p = Produto("Leite", 5, 3, minimo=5)
    assert p.estoque_baixo() is True

def test_validade_expirada():
    ontem = date.today() - timedelta(days=1)
    p = Produto("Iogurte", 2, 10, validade=ontem)
    assert p.expirado() is True

def test_validade_nao_expirada():
    amanha = date.today() + timedelta(days=1)
    p = Produto("Queijo", 5, 5, validade=amanha)
    assert p.expirado() is False

def test_produto_sem_validade_nao_expirado():
    p = Produto("Arroz", 5, 10)  # validade = None
    assert p.expirado() is False

def test_perdas_por_validade():
    ontem = date.today() - timedelta(days=1)
    p = Produto("Pão", 3, 4, validade=ontem)
    assert p.perdas_por_validade() == 12

def test_perdas_sem_expirar():
    amanha = date.today() + timedelta(days=1)
    p = Produto("Pão", 3, 4, validade=amanha)
    assert p.perdas_por_validade() == 0

def test_valores_negativos():
    with pytest.raises(ValueError):
        Produto("Erro", -1, 10)

    with pytest.raises(ValueError):
        Produto("Erro", 1, -10)

def test_remover_mais_que_estoque():
    p = Produto("Água", 2, 5)
    with pytest.raises(ValueError):
        p.remover_estoque(6)

def test_adicionar_estoque_invalido():
    p = Produto("Refrigerante", 3, 5)
    with pytest.raises(ValueError):
        p.adicionar_estoque(-2)

def test_movimentacoes():
    p = Produto("Feijão", 4, 10)
    p.adicionar_estoque(5)
    p.remover_estoque(3)
    assert p.movimentacoes == [("entrada", 5), ("saida", 3)]
