import timeit
import random

def anagram_find(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    print(c1, c2)
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos]  = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos]  = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []

    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]
