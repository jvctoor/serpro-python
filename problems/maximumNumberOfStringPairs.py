def maximumNumberOfStringPairs(words):
    mapWords = {}
    cont = 0

    def reverseString(word):
        newStr = ''
        for i in range(len(word) - 1, -1, -1):
            newStr += word[i]
        return newStr

    for word in words:
        wordReversa = reverseString(word)
        if wordReversa in mapWords:
            cont += 1
        else:
            mapWords[word] = wordReversa

    return cont



print(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
