"""
[정수론 - 최대공약수(GCD)와 최소공배수(LCM)]

문제 설명:
- 두 정수의 최대공약수(GCD)와 최소공배수(LCM)를 구합니다.
- 유클리드 호제법을 사용하여 GCD를 효율적으로 계산합니다.
- GCD를 이용하여 LCM을 계산합니다.

입력:
- a, b: 두 개의 양의 정수

출력:
- GCD: 최대공약수
- LCM: 최소공배수

예제:
입력: a = 48, b = 18
출력: 
  GCD = 6
  LCM = 144

힌트:
- 유클리드 호제법: gcd(a, b) = gcd(b, a % b)
- LCM 공식: lcm(a, b) = (a × b) / gcd(a, b)
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """
    # TODO: 유클리드 호제법 구현
    # base case: b가 0이 되면 현재 a가 최대공약수이므로 반환한다.
    if b == 0:
        return a
    # Recursive Case:
    # gcd(a, b) = gcd(b, a%b를 이용해 문제를 더 작은 형태로 줄인다.     
    return gcd(b, a % b)

def gcd_iterative(a, b):

    """
    반복문을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """
    # TODO: 반복문으로 구현
    # b가 0이 될 때까지 a와 b를 갱신한다. 
    while b != 0:
        # 이전의 b를 a로 옮기고,
        # a를 b로 나눈 나머지를 새로운 b로 설정한다. 
        a, b = b, a % b
    # b가 0이 되면 a가 최대공약수이다. 
    return a

def lcm(a, b):
    """
    최소공배수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최소공배수
    """
    # TODO: LCM 계산 = a x b + GCD
    # 정수 결과를 얻기 위해 // 연산을 사용한다. 
    return a * b // gcd_iterative(a, b)

def extended_gcd(a, b):
    """
    확장 유클리드 호제법
    ax + by = gcd(a, b)를 만족하는 x, y를 찾음
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        (gcd, x, y) 튜플
    """
    # TODO: 확장 유클리드 호제법 구현
    # Base case: 
    # b가 0이면 gcd = a이고
    # ax1+0x0 = a이므로 (a, 1, 0)을 반환한다.    
    if b == 0:
        return (a, 1, 0)
    # Recursive case:
    # 작은 문제 gcd(b, a % b)를 먼저 해결한다. 
    gcd, x1, y1 = extended_gcd(b, a % b)

    # 작은 문제에서 구한 x1, y1을 이용해
    # 현재 문제의 x, y를 역추적하여 계산한다. 
    x = y1
    y = x1 - (a//b) * y1
    # 현재 gcd와 현재 문제의 x, y를 반환한다. 
    return gcd, x, y

import math

def is_prime(n):
    """
    소수 판별
    
    Args:
        n: 판별할 양의 정수
    
    Returns:
        소수이면 True, 아니면 False
    """
    # TODO: 소수 판별 구현
    # 0과 1은 소수가 아니므로 False를 반환한다. 
    if n < 2: 
        return False
    # 2는 유일한 짝수인 소수이므로 True를 반환한다. 
    if n == 2:
        return True
    # 2를 제외한 짝수는 소수가 아니므로 False를 반환한다. 
    if n % 2 == 0:
        return False
    # 약수는 항상 하나가 sqrt(n)이하이므로
    # 3부터 sqrt(n)까지만 확인하면 된다.  
    limit = int(math.sqrt(n))
    # 짝수는 이미 제외했으므로 홀수 약수만 확인한다. 
    for i in range(3, limit + 1, 2):
        # 나누어떨어지는 수가 있으면 소수가 아니다. 
        if n % i == 0:
            return False
    # 약수가 발견되지 않았으면 소수이다. 
    return True 

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")


