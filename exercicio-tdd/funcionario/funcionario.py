class Funcionario:
    def __init__(self, nome, salario_base, comissao=0, horas_extras=0, beneficios=0):
        if salario_base < 0 or comissao < 0 or horas_extras < 0 or beneficios < 0:
            raise ValueError("Valores negativos não são permitidos")
        
        self.nome = nome
        self.salario_base = salario_base
        self.comissao = comissao
        self.horas_extras = horas_extras
        self.beneficios = beneficios

    def calcular_pagamento(self):
        custo_empregador = self.salario_base * 0.2  # 20% do salário base
        valor_horas_extras = self.horas_extras * 50  # R$50 por hora extra
        total = self.salario_base + self.comissao + valor_horas_extras + self.beneficios + custo_empregador
        return total
