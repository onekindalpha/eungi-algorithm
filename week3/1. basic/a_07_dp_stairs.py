def climb_stairs_optimized(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 1  # dp[1]에 해당
    prev1 = 2  # dp[2]에 해당

    for i in range(3, n+1):
        prev2, prev1 = prev1, prev1 + prev2  # 한 칸씩 밀어서 갱신

    return prev1

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 계단 오르기 ===")
    for i in range(1, 11):
        result = climb_stairs_optimized(i)
        print(f"{i}번 계단: {result}가지")
    print()
    
    # 테스트 케이스 2: 큰 수
    n = 20
    result = climb_stairs_optimized(n)
    print(f"{n}번 계단: {result}가지")
    print()
    
    # 계단별 경로 예시
    print("=== 4번 계단의 경로 ===")
    print("1. 1+1+1+1")
    print("2. 1+1+2")
    print("3. 1+2+1")
    print("4. 2+1+1")
    print("5. 2+2")


