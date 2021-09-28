def tabuada(num):
    for cont in range(1,11):
        print('{0} x {1} = {2}'.format(num, cont, num * cont))

def calcular_contador(num, cont):
    return num * cont

if __name__ == '__main__':
    num = int(input('Informa o numero para tabuada:  '))

    tabuada(num)