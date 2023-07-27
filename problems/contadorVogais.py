
def contarVogais(str):
    vogais = ('a', 'e', 'i', 'o', 'u')
    cont = 0
    for i in range(0, len(str), 1):
        if str[i].lower() in vogais:
            cont += 1
    return cont


if __name__ == '__main__':
    print('CONTADOR DE VOGAIS')
    palavra = input('Digite uma palavra: ')
    qtdVogais = contarVogais(palavra)
    print(f'A palavra {palavra.lower()} tem {qtdVogais} vogais.')





