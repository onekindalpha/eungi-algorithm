"""
[재귀 함수 - 팩토리얼과 피보나치 수열]

문제 설명:
- 재귀 함수를 사용하여 팩토리얼과 피보나치 수를 계산합니다.
- 재귀의 기본 개념인 base case와 recursive case를 이해합니다.

입력:
- n: 양의 정수

출력:
- 팩토리얼: n!
- 피보나치: n번째 피보나치 수

예제:
입력: n = 5
팩토리얼 출력: 120 (5! = 5 × 4 × 3 × 2 × 1)
피보나치 출력: 5 (0, 1, 1, 2, 3, 5)

힌트:
- 팩토리얼: n! = n × (n-1)!, 0! = 1
- 피보나치: fib(n) = fib(n-1) + fib(n-2), fib(0) = 0, fib(1) = 1
"""

def factorial(n):
    """
    재귀를 사용한 팩토리얼 계산
    
    Args:
        n: 양의 정수
    
    Returns:
        n의 팩토리얼 값
    """
    # TODO: base case를 작성하세요
    # Base Case:
    # 0! 과 1! 은 모두 1이므로 여기서 재귀를 종료한다. 
    if n == 0 or n == 1:
        return 1
    
    # TODO: recursive case를 작성하세요
    # n! = n x (n-1)!을 이용해 더 작은 문제로 나눈다. 
    return n * factorial(n-1)

def fibonacci(n):
    """
    재귀를 사용한 피보나치 수 계산
    
    Args:
        n: 구하고자 하는 피보나치 수의 인덱스
    
    Returns:
        n번째 피보나치 수
    """
    # TODO: base case를 작성하세요
    # Base Case:
    # fib(0) = 0, fib(1) = 1이므로 재귀를 종료한다. 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # TODO: recursive case를 작성하세요
    # Recursive Case:
    # fib(n) = fib(n-1)+ fib(n-2)를 이용한다. 
    return fibonacci(n-1) + fibonacci(n-2)

# 메모제이션 버전
# 결과를 저장해놓으면 다시 계산할 필요가 없지 않을까?
# memo는 재귀 호출마다 새로 만드는게 아니라, 하나의 딕셔너리를 여러 재귀호출이 공유하는 구조임
# 시간 복잡도 O(2^N) -> O(N) 수준으로 줄임. 
# 대신에 memo에 저장하니까, 추가 메모리 O(N)을 사용함. 

def fibonacci(n, memo=None):
    """
    재귀를 사용한 피보나치 수 계산
    
    Args:
        n: 구하고자 하는 피보나치 수의 인덱스
    
    Returns:
        n번째 피보나치 수
    """
    # 메모가 없다면 한 번만 빈 딕셔너리를 생성한다. 
    if memo is None:
        memo = {}        
    
    # TODO: base case를 작성하세요
    # 이미 계산한 값이면 다시 계산하지 않고 바로 반환한다. 
    if n in memo:
        return memo[n]
    # Base Case:
    # fib(0) = 0, fib(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # 아직 계산하지 않은 값을 재귀적으로 계산한다. 
    # 계산한 결과를 memo[n]에 저장하여 다음에 재사용한다. 
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    # TODO: recursive case를 작성하세요
    # memo에 저장한 n번째 피보나치 값을 반환한다. 
    return memo[n]

# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {factorial(10)}")
    print(f"fib(15) = {fibonacci(15)}")


