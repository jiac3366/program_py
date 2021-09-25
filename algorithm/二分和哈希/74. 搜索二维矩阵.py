def searchMatrix(matrix, target):
    if not matrix: return -1
    for item in range(1, len(matrix)):
        matrix[0].extend(matrix[item])

    left = 0
    right = len(matrix[0]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[0][mid] == target:
            return True
        elif matrix[0][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    searchMatrix([[1], [3]], 3)
