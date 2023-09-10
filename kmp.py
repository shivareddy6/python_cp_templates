import random

def findCount(s, p):
    '''returns number of subarrays of p in s (subarrays may overlap)'''
    # longest common prefix suffix from p[0:i+1]
    lps = [0 for i in range(len(p))]
    prevLps, i = 0, 1

    while i < len(p):
        if p[i] == p[prevLps]:
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        elif prevLps == 0:
            lps[i] = 0
            i += 1
        else:
            prevLps = lps[prevLps-1]

    i = 0
    j = 0
    ans = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j-1]
        if j == len(p):
            ans += 1
            j = lps[j-1]

    return ans




def kmp(s, p):
    '''returns true if p is present in s'''
    lps = [0 for i in range(len(p))]
    prevLps, i = 0, 1

    while i < len(p):
        if p[i] == p[prevLps]:
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        elif prevLps == 0:
            lps[i] = 0
            i += 1
        else:
            prevLps = lps[prevLps-1]

    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j-1]
        if j == len(p):
            return True

    return False


