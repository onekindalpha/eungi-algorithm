# 해시 
# N 마리의 폰켓몬 중에서 N/2마리를 고르는 방법
# nums에는 폰켓몬 종류 번호가 담겨있는 1차원 배열이고 
# 항상 짝수로 주어짐
# 가장 많은 종류 폰켓몬 선택 방법이 여러가지인 경우에도
# 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return
from collections import Counter
# 리스트에 같은 번호가 있는 수를 세서 -> 딕셔너리 해시로 만들어. 
# 그래서 값을 더해서 N/2마리
# 근데 구하는 방법까지 구해야 하는데
# 일단 딕셔너리로 만들자. 
# 만약에 포켓몬 마리의 수를 N/2마리를 모으려고 하면, 한번 키를 모아보고 한번 값을 모아봐서, 값들을 더한 것이 N/2마리가 되도록 선택하는 방법

def solution(nums):
    answer = 0
    # 세트로 중복을 제거한다음에 이게 최대 종류 수인데
    my_set = set(nums)
    max_type = len(my_set)
    # print(my_set)
    # 구할 수 있는 마리의 수가 2개이면 그게 최대 종류 수임. 
    n = len(nums)
    # 최대 종류 수
    max_number = n // 2
    if max_number < max_type:
      answer = max_number
    else:
      answer = max_type
    return answer
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
