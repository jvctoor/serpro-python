
def isSubsequence(s, t):
    mp = {}
    str = ""
    for char in t:
        mp[char] = char

    for char in s:
        if char in mp:
            str += char

    if str == s:
        return True
    else:
        return False


def isSubsequence2(s, t):
    ponteiro2 = 0
    str = ""
    for ponteiro1 in range(len(t)):
        if t[ponteiro1] == s[ponteiro2]:
            ponteiro2+=1
            str += t[ponteiro1]

    if str == s:
        return True
    else:
        return False





s = "acd"
t = "ahbgdc"

print(isSubsequence2(s, t))