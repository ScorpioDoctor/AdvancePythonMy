# -*- coding: utf8 -*-
import sys
import os
import re


def solve(S, T):
    tl = len(T)
    sl = len(S)
    n = 0
    for i in range(sl - tl):
        sub_s = S[i:i + tl]
        rep_s = S[i:i + tl]
        for j in range(tl):
            rep_s = rep_s.replace(sub_s[j], T[j])
        if T == rep_s:
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
