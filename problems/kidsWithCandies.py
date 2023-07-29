
def kidsWithCandies(candies, extraCandies):
    result = []
    for i in range(len(candies)):
        candiesWithExtra = candies[i] + extraCandies
        greatestNumber = True
        cont = 0
        while greatestNumber:
            if cont >= len(candies):
                break
            if candiesWithExtra < candies[cont]:
                greatestNumber = False
            cont += 1
        result.append(greatestNumber)
    return result


candies = [2,3,5,1,3]
extraCandies = 3

result = kidsWithCandies(candies, extraCandies)

print(result)