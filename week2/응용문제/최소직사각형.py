# 완전탐색 문제
# sizes 원소는 [w, h]
# w는 명함의 가로 길이, h는 명함의 세로 길이
# Brute Force 문제인데 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때
def rotate(sizes):
    for size in sizes:
        if size[0] < size[1]:
            # 가로와 세로의 길이를 바꾼다음에 
            size[0], size[1] = size[1], size[0] 
    return sizes

def solution(sizes):
    max_square = 0
    # 회전을 해볼 횟수 
    n = len(sizes)
    # 회전함수를 호출함.
    sizes = rotate(sizes)
    # 각 열에서 최대값을 찾음
    max_values = [max(column) for column in zip(*sizes)]
    # 최대 가로값
    max_w = max_values[0]
    # 최대 세로값
    max_h = max_values[1]
    # 최대 가로값과 최대 가로값을 곱한 값을 구함
    max_square = max_w * max_h 
    return max_square

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))