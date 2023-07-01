class Solution:
    def defBits(self, N):
        self.N = N
        a = bin(N)
        result = 0
        for i in a:
            if i == "1":
                result += 1
            else:
                pass
        return result


a = Solution()
print(a.defBits(10))
