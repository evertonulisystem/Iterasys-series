import pytest
from src.tabuada import calcular_contador
num=input("")
def test_multiplo_de_uma_tabuada():
    num = 2
    cont = 9
    multiplo_esperado = 18
    valor_atual = calcular_contador(num, cont)
    assert multiplo_esperado == valor_atual
