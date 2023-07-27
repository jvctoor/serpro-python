def inverterString(str):
    n = len(str)
    newStr = ''
    for i in range(1, n+1, 1):
        newStr += str[-i]
    return newStr


if __name__ == '__main__':
    print('PALÍNDROMO CHECKER')
    palavra = input('Digite uma palavra: ')
    palavraInvertida = inverterString(palavra)
    if palavra.lower() == palavraInvertida.lower():
        print('É um palíndromo!')
        print(f'{palavra} = {palavraInvertida}')
    else:
        print('Não é um palíndromo!')
        print(f'{palavra} != {palavraInvertida}')





