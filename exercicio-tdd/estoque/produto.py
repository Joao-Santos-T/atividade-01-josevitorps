from datetime import date

class Produto:
    def __init__(self, nome, preco, quantidade, validade=None, minimo=0, maximo=1000):
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço ou quantidade não pode ser negativo")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.validade = validade
        self.minimo = minimo
        self.maximo = maximo
        self.movimentacoes = []

    def adicionar_estoque(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade inválida")
        self.quantidade += quantidade
        self.movimentacoes.append(("entrada", quantidade))

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente")
        self.quantidade -= quantidade
        self.movimentacoes.append(("saida", quantidade))

    def valor_total(self):
        return self.quantidade * self.preco

    def estoque_baixo(self):
        return self.quantidade < self.minimo

    def expirado(self):
        return self.validade and self.validade < date.today()

    def perdas_por_validade(self):
        if self.expirado():
            return self.valor_total()
        return 0
