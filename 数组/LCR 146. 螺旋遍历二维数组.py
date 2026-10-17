class Solution(object):
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        if array == []:
            return []
        top = 0
        left = 0
        right = len(array[0]) - 1
        bottom = len(array) - 1
        result = []
        while (top <= bottom and left <= right):
            # 遍历top行
            for col in range(left, right+1):
                result.append(array[top][col])
            top += 1
            if top > bottom:
                break
            
            # 遍历right列
            for row in range(top, bottom+1):
                result.append(array[row][right])
            right -= 1
            if left > right:
                break

            # 遍历bottom行
            for col in range(right, left-1, -1):
                result.append(array[bottom][col])
            bottom -= 1
            if top > bottom:
                break

            # 遍历left行
            for row in range(bottom, top-1, -1):
                result.append(array[row][left])
            left += 1
            if left > right:
                break
        return result

        
