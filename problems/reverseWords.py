
def reverseWords(str):
    arr = str.split()
    arrInvertido = []

    for i in range(len(arr)-1, -1, -1):
        arrInvertido.append(arr[i])

    return " ".join(arrInvertido)


str = "ola serpro"
print(reverseWords(str))