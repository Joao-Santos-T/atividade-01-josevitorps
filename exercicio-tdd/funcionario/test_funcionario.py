import pytest
from funcionario.funcionario import Funcionario

def test_calculo_salario_base():
    f = Funcionario("João", 2000)
    assert f.calcular_pagamento() == 2000 + 0 + 0 + 0 + 400  # 20% de custo empregador

def test_comissao_adicionada():
    f = Funcionario("Maria", 2000, comissao=500)
    assert f.calcular_pagamento() == 2000 + 500 + 0 + 0 + 400

def test_horas_extras():
    f = Funcionario("Ana", 2000, horas_extras=2)
    assert f.calcular_pagamento() == 2000 + 0 + 100 + 0 + 400

def test_beneficios():
    f = Funcionario("Carlos", 2000, beneficios=300)
    assert f.calcular_pagamento() == 2000 + 0 + 0 + 300 + 400

def test_valores_negativos():
    with pytest.raises(ValueError):
        Funcionario("Erro", -1000)

def test_todos_os_campos():
    f = Funcionario("Bruno", 2000, comissao=300, horas_extras=4, beneficios=250)
    assert f.calcular_pagamento() == 2000 + 300 + 200 + 250 + 400
