lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = ".?!&#,;:-_* "
nums = "1234567890"

def isValid(password):
    return 1 in [1 for p in password if p in lower] and 1 in [1 for p in password if p in upper]


def chaEvaluator(last, password):
    current = last + 1
    characters = [char for char in password]
    try:
        if characters[last] == characters[current]:
            return 0
        elif characters[last] in lower and characters[current] in upper or characters[current] in lower and characters[last] in upper:
            return 5
        elif characters[last] in nums and (characters[current] in upper or characters[current] in lower) or characters[current] in nums and (characters[last] in upper or characters[last] in lower):
            return 8
        elif characters[last] in special and (characters[current] in upper or characters[current] in lower) or characters[current] in special and (characters[last] in upper or characters[last] in lower):
            return 10
        elif characters[last] in special and characters[current] in nums or characters[current] in special and characters[last] in nums:
            return 12
        else:
            return 2
    except:
        return 2


def passwordEvaluator(password):
    leng = 0
    for i in password:
        leng += 1
    values = [chaEvaluator(i, password) for i in range(leng)]
    ans = 0
    for a in values:
        ans += int(a)
    if ans * 2 > 100:
        return 100
    else:
        return ans * 2

