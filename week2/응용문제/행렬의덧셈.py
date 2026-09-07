#  행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됨. 2개의 행렬 arr1과 arr2를 
# 2개의 행렬 arr1, arr2를 입력받아 행렬 덧셈의 결과를 반환하는 함수
# zip
def solution(arr1, arr2):
    answer = [
        [a + b for a, b in zip(row1, row2)]
        for row1, row2 in zip(arr1, arr2)
    ]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution([[1],[2]],[[3],[4]]))