

s = "hello"

def reverseVowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    vowelsInString = []
    vowelsInStringReverse = []
    newString = []

    for i in str:
        if i.lower() in vowels:
            vowelsInString.append(i)

    if len(vowelsInString) == 0 or len(str) == 0:
        return str

    for i in range(len(vowelsInString)-1, -1, -1):
        vowelsInStringReverse.append(vowelsInString[i])

    cont = 0
    for i in range(0, len(str)):
        if str[i].lower() in vowels:
            newString.append(vowelsInStringReverse[cont])
            cont += 1
        else:
            newString.append(str[i])

    return ''.join(newString)




print(reverseVowels(s))
