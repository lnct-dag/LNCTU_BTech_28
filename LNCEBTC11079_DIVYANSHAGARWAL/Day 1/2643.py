class Solution:
    def rowAndMaximumOnes(self, mat):
        m = len(mat)
        n = len(mat[0])

        maxOnesRow = 0
        maxOnes = 0

        for row in range(m):
            ones_count = 0

            for column in range(n):
                if mat[row][column] == 1:
                    ones_count += 1

            if ones_count > maxOnes:
                maxOnesRow = row
                maxOnes = ones_count

        return [maxOnesRow, maxOnes]
        