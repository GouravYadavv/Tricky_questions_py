class Solution:
    def nextHappy(self, N):
        self.N = N
        num = N + 1

        def is_happy_number(num):
            visited = set()
            while True:
                if num == 1:
                    return True
                elif num in visited:
                    return False
                visited.add(num)
                num = sum(int(digit) ** 2 for digit in str(num))

        while True:
            if is_happy_number(num):
                return num
            num += 1


a = Solution()
print(a.nextHappy(10))
