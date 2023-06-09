def uniqueLetterString(str):
    set1 = set()
    maxLen = 0
    start = 0
    end = 0
    while start < len(str) and end < len(str):
        if str[end] not in set1:
            set1.add(str[end])
            maxLen = max(len(set1), maxLen)
            end += 1
        else:
            set1.remove(str[start])
            start += 1
    return maxLen


print(uniqueLetterString("thisishowwedoit"))
