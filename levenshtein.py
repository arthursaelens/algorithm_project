"""
Group: 5

Template for Levenshtein distance methods. 
"""

def tail(s: str):
    """
    Extract tail of string.

    :param str s: Input string.
    :return str: Tail of s.
    """
    return s[1:]

def lev(a: str, b: str) -> int:
    """
    Naive, recursive implementation of the Levenshtein distance.

    :param str a: First string.
    :param str b: Second string.
    :return int: Levenshtein distance between a and b.
    """
    if min(len(a),len(b))==0:
        return max(len(a),len(b))
    if a[0]==b[0]:
        return lev(tail(a),tail(b))
    else:
        return 1+min(lev(tail(a),b), lev(a,tail(b)), lev(tail(a),tail(b)))

def lev_dp(a: str, b: str) -> int:
    """
    Dynamic programming implementation of the Levenshtein distance.

    :param str a: First string.
    :param str b: Second string.
    :return int: Levenshtrein distance between a and b.
    """
    m = len(a)
    n = len(b)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    return d[m][n]
