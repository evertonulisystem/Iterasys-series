import pytest
print('Como estudo de caso, considere a variavel de numero 9 para a função e também para o teste.')
num1 = 9
caixa = 40
def calcular_qdade_de_fosforos(num1,caixa):
    return num1 * caixa
print('\nConsiderando que cada caixa possui 40 palitos.')
print(f'Terá um total de {calcular_qdade_de_fosforos(num1,caixa)} palitos.')
