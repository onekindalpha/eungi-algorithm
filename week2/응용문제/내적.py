
# 내적은 수학에서 두 벡터를 곱해서 하나의 숫자(스칼라)로 만드는 연산
# 내적은 안쪽으로 곱한다는 의미임. 
# 벡터의 내적이란 두 벡터의 각 성분끼리 곱한 후 합하는 것을 의미함. 
def solution(a, b):
    # a와 b 배열에서 같은 위치끼리 곱하는 연산.
    result = [x * y for x,y in zip(a, b)]
    return sum(result)
print(solution([1,2,3,4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))