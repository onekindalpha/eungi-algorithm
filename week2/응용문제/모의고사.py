# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아. 
# 수포자가 여러명임
# 문제의 정답은 1,2,3,4,5 중 하나임
# 가장 높은 점수 받은 사람이 여럿일 경우, return 값 배열을 오름차순 정렬함. 

def solution(answers):
    answer = []
    # 가장 많은 문제를 맞춘 사람이 누구인지. 
    # 문제의 정답인 answers와 비교해야 함. 
    # 1번 수포자가 찍는 방식은 1~5번까지 계속 반복함. 
    # 2번 수포자가 찍는 방식은 
    if len(answer) > 1:
        # sort()함수 이렇게 해도 되는지 헷갈리는데. 
        answer = answer.sort()
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
