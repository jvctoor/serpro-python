

# NAO RESOLVIDO AINDA
def canPlaceFlowers(flowerbed, n):

    primeiraPlantaAchada = False
    indexPrimeiraPlanta = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            primeiraPlantaAchada = True
            indexPrimeiraPlanta = i
            break
        else:
            primeiraPlantaAchada = False
            indexPrimeiraPlanta = 0
            break

    if (indexPrimeiraPlanta + 1) % 2 == 1:
        casaPlantas = "Ímpar"

    if not primeiraPlantaAchada:
        if n <= (int(len(flowerbed) / 2)):
            return True
        else:
            return False

    for i in range(len(flowerbed)):
        pass


x = [1,0,0,0,1]
h = [0,0,0,0,0]
y = 1

print(canPlaceFlowers(x, y))
print(canPlaceFlowers(h, y))

