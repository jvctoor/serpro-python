
def titleToNumber(columnTitle):
    vl = 0
    firstPlay = True
    for i in range(len(columnTitle)-1, -1, -1):
        char = columnTitle[i]
        if firstPlay:
            pt = ord(char) - 64
            vl += pt
            firstPlay = False
        else:
            vl+=26
    return vl


print(titleToNumber("AB"))