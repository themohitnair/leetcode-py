class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2147483648, 2147483647

        if x == 0:
            return x

        sign = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x > 0:
            d = x % 10
            x //= 10
            rev = rev * 10 + d

        rev *= sign

        if rev < MIN or rev > MAX:
            return 0

        return rev
