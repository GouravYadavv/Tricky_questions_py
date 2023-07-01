class solution:
    def isDivisible(self, s):
        self.s = s
        x = int(s, 2)
        if x % 3 == 0:
            return 1
        else:
            return 0


t = solution()
b = t.isDivisible("1111")
print(b)
