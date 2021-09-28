from src.fosforo import calcular_qdade_de_fosforos, caixa
print('Como informado, o numero de teste sera o (9).')
def test_qdade_de_fosforos_em_caixa():
    num1 = 9
    num2 = 40
    resultado_esperado = 360
    resultado_atual = calcular_qdade_de_fosforos(num1,caixa)
    assert resultado_esperado == resultado_atual
