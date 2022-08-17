class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or i == j:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)
        return triangle[-1]
