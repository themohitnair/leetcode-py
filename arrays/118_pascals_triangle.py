class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]

        for i in range(1, numRows):
            aux = [0] + triangle[i - 1] + [0]
            next = []
            for i in range(1, len(aux)):
                next.append(aux[i] + aux[i - 1])
            triangle.append(next)

        return triangle
