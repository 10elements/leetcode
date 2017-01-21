def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    n = len(board[0])
    m = len(board)
    for i in range(m):
        board[i].insert(0, '')
        board[i].append('')
    board.insert(0, ['' for i in range(n + 2)])
    board.append(['' for i in range(n + 2)])
    m = len(board)
    n = len(board[0])
    print(m, n)
    print(board)
    start = word[0]
    s = []
    nextIndex = 0
    l = len(word)
    for i in range(m):
        for j in range(n):
            if board[i][j] == start:
                print(i, j)
                s.clear()
                s.append((i, j))
                nextIndex = 1
                visited = [[0 for i in range(n)] for j in range(m)]
                visited[0] = [1] * n
                for p in range(1, m - 1):
                    visited[p][0] = 1
                    visited[p][-1] = 1
                visited[-1] = [1] * n
                print(i, j)
                while len(s):
                    if nextIndex == l:
                        return True
                    x, y = s[-1]
                    r = accessible(board, word, nextIndex, visited, x, y)
                    if len(r) == 0:
                        s.pop()
                        nextIndex -= 1
                    else:
                        s.append(r[0])
                        nextIndex += 1
    return False
    
def accessible(board, word, index, visited, x, y):
    result = []
    t = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
    for r, c in t:
        if (not visited[r][c]) and (board[r][c] == word[index]):
            result.append((r, c))
    return result

def main():
    board = [list("ABCE"),list("SFCS"),list("ADEE")]
    word = "ABCESEEEFS"
    if exist(board, word):
        print('True')

if __name__ == '__main__':
    main()