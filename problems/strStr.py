def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    lenstr = len(needle)
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            pointer = 0
            for j in range(i, i + lenstr):
                if j >= len(haystack):
                    return -1
                if needle[pointer] == haystack[j]:
                    pointer += 1
                    if j == (i + lenstr) - 1:
                        return i
                else:
                    break

    return -1