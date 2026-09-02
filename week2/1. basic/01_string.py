"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""
#
def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수

    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 시간 복잡도: O(N) - 문자열을 양쪽에서 한 번씩 확인한다.
    # 공간 복잡도: O(1) - 추가 문자열이나 리스트 없이 변수만 사용한다.
    # 왼쪽 시작 인덱스
    left = 0
    # 오른쪽 시작 인덱스
    # 마지막 원소의 인덱스는 문자열 길이 -1이다. 
    right = len(s) -1
    # 왼쪽과 오른쪽이 만날 때까지 비교한다. 
    while left < right:
        # 왼쪽 문자가 알파벳이나 숫자가 아니면 건너뛴다. 
        if not s[left].isalnum():
            left += 1
            continue
        # 오른쪽 문자가 알파벳이나 숫자가 아니면 건너뛴다. 
        if not s[right].isalnum():
            right -= 1
            continue
        # 대소문자를 무시하고 양쪽 문자가 같은지 비교한다. 
        if s[left].lower() != s[right].lower():
            return False
        # 두 문자가 같으면 다음 비교를 위해 양쪽 인덱스를 비교한다. 
        left += 1
        right -= 1
    # 모든 문자가 조건을 만족하면 회문이다. 
    return True
    
# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


