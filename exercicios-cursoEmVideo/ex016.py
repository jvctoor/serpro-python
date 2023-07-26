

cigarrosFumados = int(input('Cigarros fumados por dia: '))
anosFumando = int(input('Anos fumando: '))

tempoPerdidoDia = (cigarrosFumados * 10) #Tempo perdido em minutos por dia
diasFumando = ((anosFumando * 365) * tempoPerdidoDia) / 24

print('-',diasFumando, 'dias de vida')



