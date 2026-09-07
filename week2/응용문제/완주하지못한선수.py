# 참여자들 배열과 완주한 선수들 배열임
# 완주하지 못한 선수들 이름
# 참가자 중에는 동명이인 있을 수도 있음
# 동명이인이 완주를 햇으면 그 사람이 완주했는지 내가 완주한건지 어떻게 알지
# 이건 set으로 제거하는게 아닌 것 같은데 . 
from collections import Counter
def solution(participant, completion):
    answer = ''
    # 1. 참가자와 완주자의 Counter를 구해서 뺌. 
    answer = Counter(participant) - Counter(completion)
    print(answer)
    # 2. 남은 key(이름) 하나를 꺼내서 문자열로 반환
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))