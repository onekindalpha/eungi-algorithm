"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    # 시간 복잡도: O(N) - 문자열의 각 문자를 한 번씩 확인한다.
    # 공간 복잡도: O(N) - 여는 괄호를 stack에 저장할 수 있다.
    stack = []
    # TODO: 문자열의 각 문자를 순서대로 확인한다. 
    # : 여는 괄호 '('면 스택에 추가한다. 
    for char in s:
        if char == "(":
            stack.append(char)

    # : 닫는 괄호 ')'를 만나면 짝이 되는 "("가 있는지 확인한다. 
        else:
        # stack이 비어 있다면 짝이 될 "("가 없으므로 잘못된 괄호이다. 
            if not stack:
                return False
            # 짝이 되는 "("를 stack를 제거한다. 
            stack.pop()
    
    # TODO: 반복이 끝나면 스택이 비어있는지 확인 
    # 모든 문자를 확인한 뒤 stack이 비어 있으면 모든 괄호의 짝이 맞는다. 
    return not stack

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


