def lengthOfLongestSubstring(s):
    contadores = []
    cont = 1
    cursor = 0
    for i in range(1, len(s)):
        if i >= len(s):
            break
        stringAux = s[cursor:i]
        if s[i] in stringAux:
            contadores.append(cont)
            cont = 1
            cursor = i
            continue
        else:
            cont += 1
            contadores.append(cont)

    if len(contadores) >= 1:
        return max(contadores)
    else:
        if s == "":
            return 0
        else:
            return cont

def lengthOfLongestSubstring2(s):
    continues = []
    count = 0
    temp = 0
    for i in s:
        while i in continues:
            continues.pop(0)
            temp -= 1
        else:
            continues.append(i)
            temp += 1
            count = max(count, temp)
    return count


print(lengthOfLongestSubstring2("dvdf"))