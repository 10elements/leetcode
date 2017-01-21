def rangeBitwiseAnd( m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    shift = 0
    while m != n:
        m >> 1
        n >> 1
        shift += 1
        print(m, n)
    m << shift
    return m

def main():
    m = 0
    n = 1
    return rangeBitwiseAnd(m, n)
    
if __name__ == '__main__':
    main()