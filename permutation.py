from math import factorial


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)


print(permute("ABC"))


def math_permutation(string):
    for p in range(factorial(len(string))):
        print(''.join(string))
        i = len(string) - 1
        while i > 0 and string[i - 1] > string[i]:
            i -= 1
        string[i:] = reversed(string[i:])
        if i > 0:
            q = i
            while string[i - 1] > string[q]:
                q += 1
            temp = string[i - 1]
            string[i - 1] = string[q]
            string[q] = temp


print(math_permutation(list("XYZ")))
