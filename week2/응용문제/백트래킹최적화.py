# 백트래킹 최적화 코드
def combi(n, k):
    result = []
    # n개 중 k개를 뽑을 수 없는 경우 아예 가지치기를 함. 
    if k > n:
        return []
    def bt(start, current):
        # 현재 뽑은 개수가 k개가 되면
        if len(current) == k:
            result.append(list(current))
            # 더이상 탐색하지 않고 돌아감
            return
        # 앞으로 몇개를 더 뽑아야 하는지 
        need = k - len(current)
        # 현재 숫자로 선택할 수 있는 최대 시작값
        last_start = n - need + 1
        # start부터 last_start까지 숫자를 하나씩 선택
        for num in range(start, last_start + 1):
            #선택
            current.append(num)
            #탐색
            bt(num + 1, current)
            #다시 돌아감
            current.pop()
    bt(1, [])
    return result

print(combi(4, 2))
