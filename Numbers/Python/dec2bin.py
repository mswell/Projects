conv = []
def dec2bin(num):
    '''
    Exemplo de um simples conversor de decimal para binário.
    '''
    (num/2 > 0 and (dec2bin(int(num/2)), conv.append(num%2)))
    print(''.join(map(str, conv)))

dec2bin(int(input('Decimal: ')))
