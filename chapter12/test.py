# -*- coding: utf8 -*-
import sys
import os
import re


def solve(S, T):
    tl = len(T)
    sl = len(S)
    n = 0
    for i in range(sl - tl):
        sub_s = list(S[i:i + tl])
        rep_s = list(S[i:i + tl])
        for j in range(tl):
            ch = sub_s[j]
            rep_s[j] = T[j]
            for k in range(1, tl):
                if sub_s[k] == ch:
                    rep_s[k] = T[j]
        for h in range(tl):
            if rep_s[h] != T[h]:
                break
        if h == tl - 1:
            n += 1
    return n


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")
