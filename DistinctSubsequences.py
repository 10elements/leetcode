class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        if bool(m) ^ bool(n):
            return 0
        elif m == 0 and n == 0:
            return 0
        table = [[0] * n for i in range(m)]
        cnt = 0
        for i in range(m):
            # print(s[i], t[0])
            if s[i] == t[0]:
                # print(cnt)
                cnt += 1
            table[i][0] = cnt
        for j in range(1, n):
            for i in range(j, m):
                table[i][j] = sum([table[x - 1][j - 1] for x in range(1, i + 1) if s[x] == t[j]])
        # for line in table:
        #     print(line)
        return table[m - 1][n - 1]

c = Solution()
s = "xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsul\\\
jkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocgl\\\
wzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwd\\\
uqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyv\\\
sqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgvwonalpsyddqmaemcrrwvrjmjjnygyebwtqxehrclwsxzylbqexnxjcgspeynlbmetlkacnnbhmaizbadynajpibepbuac\\\
ggxrqavfnwpcwxbzxfymhjcslghmajrirqzjqxpgtgisfjreqrqabssobbadmtmdknmakdigjqyqcruujlwmfoagrckdwyiglviyyrekjealvvigiesnvuumxgsveadrxlpwetioxibtdjblowblqvzpbrmhupyrdophjxvhgzclidzybajux\\\
llacyhyphssvhcffxonysahvzhzbttyeeyiefhunbokiqrpqfcoxdxvefugapeevdoakxwzykmhbdytjbhigffkmbqmqxsoaiomgmmgwapzdosorcxxhejvgajyzdmzlcntqbapb\\\
pofdjtulstuzdrffafedufqwsknumcxbschdybosxkrabyfdejgyozwillcxpcaiehlelczioskqtptzaczobvyojdlyflilvwqgyrqmjaeepydrcchfyftjighntqzoo"
t = "rwmimatmhydhbujebqehjprrwfkoebcxxqfktayaaeheys"
print(c.numDistinct(s, t))