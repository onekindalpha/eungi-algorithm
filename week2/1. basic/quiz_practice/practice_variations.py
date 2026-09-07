"""
[심화 변형 7문제 - 연습용]

week2/1. basic 의 기본 문제에서 한 단계 확장된 형태입니다.
각 함수의 TODO를 직접 채운 뒤 이 파일을 실행하면 자동으로 채점됩니다.

    python3 practice_variations.py

정답 예시는 같은 폴더의 solutions_variations.py 에 있습니다.
먼저 스스로 작성해 본 뒤에 열어보세요.
"""


# ============================================================================
# 1. Two Sum - 해시맵으로 O(N)   (04_brute_force.py 변형)
# ============================================================================
def two_sum_hash(nums, target):
    """
    합이 target이 되는 모든 (i, j) 인덱스 쌍을 찾는다. (i < j)

    기존 완전 탐색은 이중 반복문으로 O(N^2)였다.
    딕셔너리 조회가 평균 O(1)이라는 점을 이용해 O(N)으로 줄여보자.

    힌트:
    - "두 수를 모두 고른다"가 아니라 "지금 수를 고정하고 짝을 조회한다"로 발상을 바꾼다.
    - 지금 수가 num이면 짝은 target - num 이다.
    - 같은 값이 여러 번 나올 수 있으므로 {값: [인덱스, ...]} 형태로 저장한다.
    """
    # TODO: 이미 지나온 값 -> 인덱스 목록을 저장할 딕셔너리를 만드세요
    # TODO: 배열을 한 번만 순회하면서
    #       (1) 짝이 되는 값이 딕셔너리에 있으면 그 인덱스들과 쌍을 만들고
    #       (2) 현재 값과 인덱스를 딕셔너리에 기록하세요
    pass


# ============================================================================
# 2. 가장 긴 팰린드롬 부분 문자열   (01_string.py 변형)
# ============================================================================
def expand_from_center(s, left, right):
    """
    (left, right)를 중심으로 양쪽으로 벌리며 팰린드롬인 동안 확장하고,
    확장이 끝난 시점의 팰린드롬 "길이"를 반환한다.

    힌트:
    - 인덱스가 범위를 벗어나지 않고 s[left] == s[right] 인 동안 left -= 1, right += 1
    - while이 끝난 시점의 left, right는 한 칸 바깥이므로 길이는 right - left - 1
    """
    # TODO: 중심에서 양쪽으로 확장하는 while 문을 작성하세요
    pass


def longest_palindrome(s):
    """
    가장 긴 팰린드롬 부분 문자열을 반환한다.

    시간 복잡도 O(N^2), 공간 복잡도 O(1)

    힌트:
    - 팰린드롬은 항상 중심을 가진다. 중심은 총 2N-1개다.
      홀수 길이("aba")는 문자 하나가 중심, 짝수 길이("abba")는 문자 사이가 중심.
    - 각 i에 대해 expand_from_center(s, i, i) 와 expand_from_center(s, i, i+1) 을 모두 시도
    - 길이 length가 중심 i에서 나왔다면 start = i - (length-1)//2, end = i + length//2
    """
    # TODO: 모든 중심을 순회하며 최장 길이와 그 시작/끝 인덱스를 갱신하세요
    pass


# ============================================================================
# 3. 이분 탐색 - 첫 위치 / 마지막 위치   (10_binary_search.py 변형)
# ============================================================================
def find_first(arr, target):
    """
    target이 처음(가장 왼쪽) 등장하는 인덱스를 반환한다. 없으면 -1

    힌트:
    - 기본 뼈대는 이분 탐색과 같다.
    - arr[mid] == target 일 때 바로 반환하지 말고, 답 후보로 저장한 뒤
      "왼쪽에 더 있을 수 있으니" right = mid - 1 로 계속 좁힌다.
    """
    # TODO: 왼쪽 경계를 찾는 이분 탐색을 작성하세요
    pass


def find_last(arr, target):
    """
    target이 마지막(가장 오른쪽) 등장하는 인덱스를 반환한다. 없으면 -1

    힌트: find_first와 반대로, 찾았을 때 left = mid + 1 로 오른쪽을 계속 본다.
          (10_binary_search.py 에 작성한 코드가 사실 이 동작이다)
    """
    # TODO: 오른쪽 경계를 찾는 이분 탐색을 작성하세요
    pass


def count_target(arr, target):
    """
    정렬된 배열에서 target의 개수를 O(log N)에 센다.

    힌트: 마지막 위치 - 첫 위치 + 1. 단, 존재하지 않을 때 처리를 잊지 말 것.
    """
    # TODO: find_first와 find_last를 이용해 개수를 구하세요
    pass


# ============================================================================
# 4. 피보나치 - 반복문 버전   (05_recursion.py 변형)
# ============================================================================
def fibonacci_iterative(n):
    """
    반복문으로 n번째 피보나치 수를 구한다.

    시간 복잡도 O(N), 공간 복잡도 O(1)
    (메모이제이션은 O(N) 공간, 재귀는 호출 스택으로 O(N) 공간이 필요했다)

    힌트:
    - fib(n)에 필요한 것은 직전 두 값뿐이다.
    - prev, curr = curr, prev + curr 로 한 칸씩 밀어준다.
    """
    # TODO: base case와 반복문을 작성하세요
    pass


# ============================================================================
# 5. 순열 생성   (06_backtracking.py 변형)
# ============================================================================
def permutations(n, k):
    """
    1 ~ n 중 k개를 뽑아 만드는 모든 순열을 반환한다.

    조합과의 차이는 딱 한 군데다.
      조합: backtrack(num + 1, ...) 로 "고른 수보다 큰 수만" 시도 -> 순서 무시
      순열: 매번 1부터 모두 시도하되 이미 쓴 수만 걸러냄        -> 순서 구분

    힌트:
    - used = [False] * (n + 1) 로 사용 여부를 관리한다.
    - 선택(Choose) -> 탐색(Explore) -> 취소(Unchoose) 3단계는 그대로.
      단, 취소할 때 current.pop() 뿐 아니라 used[num] = False 도 되돌려야 한다.
    """
    # TODO: result와 used를 만들고, backtrack 헬퍼 함수를 작성하세요
    pass


# ============================================================================
# 6. 괄호 검사 - (), {}, [] 세 종류   (12_stack.py 변형)
# ============================================================================
def is_valid_brackets(s):
    """
    세 종류의 괄호가 올바르게 짝지어졌는지 확인한다.

    힌트:
    - 닫는 괄호 -> 여는 괄호 매핑 딕셔너리를 만든다: {")": "(", "}": "{", "]": "["}
    - 닫는 괄호를 만나면 두 가지를 확인해야 한다.
      (1) 스택이 비어 있지 않은가
      (2) pop한 여는 괄호가 이 닫는 괄호의 짝이 맞는가   <- "([)]" 를 걸러내는 조건
    """
    # TODO: 스택으로 세 종류의 괄호를 검사하세요
    pass


# ============================================================================
# 7. 해시 테이블 - 체이닝 방식 직접 구현   (15_hash_table.py 변형)
# ============================================================================
class ChainingHashTable:
    """
    충돌을 체이닝으로 해결하는 해시 테이블.

    체이닝    : 같은 버킷에 충돌이 나면 그 자리에 리스트로 이어 붙인다.
    개방 주소법: 충돌이 나면 다른 빈 칸을 찾아가 저장한다.

    힌트:
    - 저장 위치는 hash(key) % self.size 로 구한다. (이 나머지 연산 때문에 충돌이 생긴다)
    - 각 버킷은 (key, value) 튜플을 담는 리스트다.
    - put: 같은 키가 이미 있으면 값을 갱신, 없으면 체인 끝에 append
    - get: 해당 버킷의 체인을 순차 탐색 (그래서 최악의 경우 O(N))
    """

    def __init__(self, size=8):
        self.size = size
        # TODO: size개의 빈 리스트(버킷)를 만드세요
        self.buckets = None

    def _index(self, key):
        # TODO: 키의 해시값을 버킷 개수로 나눈 나머지를 반환하세요
        pass

    def put(self, key, value):
        # TODO: 같은 키가 있으면 갱신, 없으면 체인에 추가하세요
        pass

    def get(self, key):
        # TODO: 해당 버킷의 체인을 순회하며 키를 찾으세요. 없으면 None
        pass


# ============================================================================
# 자동 채점
# ============================================================================
def check(label, got, expected):
    ok = got == expected
    mark = "✅" if ok else "❌"
    print(f"{mark} {label}")
    if not ok:
        print(f"     기대: {expected}")
        print(f"     결과: {got}")
    return ok


if __name__ == "__main__":
    results = []

    print("=== 1. Two Sum (해시맵) ===")
    # 순서는 달라도 되므로 정렬해서 비교한다.
    got = two_sum_hash([2, 7, 11, 15], 9)
    results.append(check("[2,7,11,15], target=9", sorted(got) if got else got, [(0, 1)]))
    got = two_sum_hash([1, 3, 4, 2, 5, 6], 7)
    results.append(check("[1,3,4,2,5,6], target=7", sorted(got) if got else got, [(0, 5), (1, 2), (3, 4)]))
    got = two_sum_hash([1, 1, 1, 1], 2)
    results.append(check("[1,1,1,1], target=2", sorted(got) if got else got,
                         [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]))
    print()

    print("=== 2. 가장 긴 팰린드롬 ===")
    results.append(check("\"cbbd\"", longest_palindrome("cbbd"), "bb"))
    results.append(check("\"abacdfgdcaba\"", longest_palindrome("abacdfgdcaba"), "aba"))
    results.append(check("\"a\"", longest_palindrome("a"), "a"))
    print()

    print("=== 3. 이분 탐색 경계 ===")
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    results.append(check("2의 첫 위치", find_first(arr, 2), 1))
    results.append(check("2의 마지막 위치", find_last(arr, 2), 3))
    results.append(check("2의 개수", count_target(arr, 2), 3))
    results.append(check("9의 개수 (없는 값)", count_target(arr, 9), 0))
    print()

    print("=== 4. 피보나치 (반복문) ===")
    results.append(check("fib 0~9", [fibonacci_iterative(i) for i in range(10)],
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))
    results.append(check("fib(50)", fibonacci_iterative(50), 12586269025))
    print()

    print("=== 5. 순열 ===")
    got = permutations(3, 2)
    results.append(check("P(3,2)", sorted(got) if got else got,
                         [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]))
    got = permutations(3, 3)
    results.append(check("P(3,3) 개수", len(got) if got else got, 6))
    print()

    print("=== 6. 괄호 검사 (3종) ===")
    results.append(check("\"(){}[]\"", is_valid_brackets("(){}[]"), True))
    results.append(check("\"([{}])\"", is_valid_brackets("([{}])"), True))
    results.append(check("\"([)]\"  <- 짝 종류가 어긋난 경우", is_valid_brackets("([)]"), False))
    results.append(check("\"(()\"", is_valid_brackets("(()"), False))
    print()

    print("=== 7. 체이닝 해시 테이블 ===")
    try:
        table = ChainingHashTable(size=4)
        for name, score in [("Alice", 85), ("Bob", 92), ("Charlie", 78)]:
            table.put(name, score)
        table.put("Alice", 100)  # 같은 키 갱신
        results.append(check("get('Bob')", table.get("Bob"), 92))
        results.append(check("get('Alice') 갱신 후", table.get("Alice"), 100))
        results.append(check("get('Frank') 없는 키", table.get("Frank"), None))
    except Exception as e:
        print(f"❌ 해시 테이블 실행 중 오류: {e}")
        results.append(False)
    print()

    passed = sum(1 for r in results if r)
    print(f"{'=' * 40}")
    print(f"통과: {passed} / {len(results)}")
