class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n *= -1
            x = 1 / x

        leftover = 1

        while n > 1:
            if n % 2 != 0:
                leftover *= x
                n -= 1
            x *= x
            n /= 2

        return x * leftover


print(Solution().myPow(3, 10))
