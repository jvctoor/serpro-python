

def isPalindrome(palavra):
    ponteiro = len(palavra)-1
    for index in range(0, int(len(palavra)/2)):
        if palavra[index] == palavra[ponteiro]:
            ponteiro-=1
        else:
            return False
    return True


print(isPalindrome("aa"))
