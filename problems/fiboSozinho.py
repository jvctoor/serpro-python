# 1 1 2 3 5 8 13 21
def fiboDinamico(num):
    map = {}
    map[0] = 1
    map[1] = 1
    if num < 0:
        return "Index deve ser maior ou igual a 0"
    if num == 0 or num == 1:
        return 1
    for i in range(2, num+1):
        if i not in map:
            map[i] = map[i - 1] + map[i - 2]

    return map[num]

def fiboRecursivo(num):
    if num == 0 or num == 1:
        return 1
    return fiboRecursivo(num-1) + fiboRecursivo(num-2)

print(fiboDinamico(6))
print(fiboRecursivo(6))