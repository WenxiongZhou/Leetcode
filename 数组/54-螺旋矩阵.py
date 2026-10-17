class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        H = len(matrix)
        W = len(matrix[0])
        start_x = 0
        start_y = 0
        top = 0
        left = 0
        bottom = H - 1
        right = W - 1
        result = []

        while top <= bottom and left <= right:
            # 遍历top整行
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1
            if top > bottom:
                break
            
            # 遍历right整列
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -= 1
            if left > right:
                break
            
            # 遍历bottom整行
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
            if top > bottom:
                break
            
            # 遍历left列
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
            if left > right:
                break
        
        return result
