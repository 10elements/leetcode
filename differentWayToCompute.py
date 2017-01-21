def diffWaysToCompute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    n = []
    symbol = []
    p = 0
    i = 0
    for c in input:
        if c.isdigit():
            p = p * 10 + int(c)
        else:
            i += 1
            n.append(p)
            n.append(c)
            symbol.append(i)
            i += 1
            p = 0
    n.append(p)
    print(n)
    print(symbol)
    table = {}
    return compute(n, symbol, 0, len(n) - 1, table)

def compute(n, symbol, i, j, table):
    if i == j:
        table[(i, j)] = [n[i]]
        return [n[i]]
    if (i, j) in table:
        return table[(i, j)]
    r = []
    for s in symbol:
        if i < s < j:
            for val1 in compute(n, symbol, i, s - 1, table):
                for val2 in compute(n, symbol, s + 1, j, table):
                    if n[s] == '+':
                        r.append(val1 + val2)
                    elif n[s] == '-':
                        r.append(val1 - val2)
                    elif n[s] == '*':
                        r.append(val1 * val2)
                    else:
                        r.append(val1 / val2)
    table[(i, j)] = r
    return r

def t(x):
    r = [1]
    x.append(r)
    return r

def main():
    # s = '2-3+1'
    # t = diffWaysToCompute(s)
    # print(t)
    x = []
    print(t(x))
    print(x)

if __name__ == '__main__':
    main()