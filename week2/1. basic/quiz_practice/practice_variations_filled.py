"""
[심화 변형 7문제 - 답 채운 버전]

practice_variations.py 의 TODO를 모두 채운 파일입니다.
힌트와 자동 채점기는 그대로 두었으니, 실행하면 21/21이 나옵니다.

    python3 practice_variations_filled.py
"""


# ============================================================================
# 1. Two Sum - 해시맵으로 O(N)   (04_brute_force.py 변형)
# ============================================================================
def two_sum_hash(nums, target):
    """
    합이 target이 되는 모든 (i, j) 인덱스 쌍을 찾는다. (i < j)

    기존 완전 탐색은 이중 반복문으로 O(N^2)였다.
    딕셔너리 조회가 평균 O(1)이라는 점을 이용해 O(N)으로 줄인다.

    시간 복잡도: O(N + K)  K는 정답 쌍의 개수
    공간 복잡도: O(N)
    """
    # 이미 지나온 값 -> 그 값이 등장했던 인덱스 목록
    # 같은 값이 여러 번 나올 수 있으므로 인덱스를 리스트로 모아 둔다.
    seen = {}
    # 조건을 만족하는 인덱스 쌍을 저장할 리스트
    pairs = []

    # 배열을 앞에서부터 한 번만 순회한다.
    for j, num in enumerate(nums):
        # 현재 값과 더해서 target이 되는 짝을 계산한다.
        complement = target - num

        # 짝이 되는 값을 앞에서 본 적이 있다면 그 인덱스들과 모두 쌍을 이룬다.
        # 앞에서 본 값이므로 i < j 가 자동으로 보장된다.
        if complement in seen:
            for i in seen[complement]:
                pairs.append((i, j))

        # 현재 값과 인덱스를 기록해 뒤에 오는 원소가 조회할 수 있게 한다.
        # setdefault: 키가 없으면 빈 리스트를 만들고, 있으면 기존 리스트를 가져온다.
        seen.setdefault(num, []).append(j)

    return pairs


# ============================================================================
# 2. 가장 긴 팰린드롬 부분 문자열   (01_string.py 변형)
# ============================================================================
def expand_from_center(s, left, right):
    """
    (left, right)를 중심으로 양쪽으로 벌리며 팰린드롬인 동안 확장하고,
    확장이 끝난 시점의 팰린드롬 "길이"를 반환한다.
    """
    # 인덱스가 문자열 범위를 벗어나지 않고, 양쪽 문자가 같은 동안 계속 벌린다.
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # while이 끝난 시점의 left, right는 팰린드롬이 아닌 한 칸 바깥이다.
    # 실제 길이 = (right - 1) - (left + 1) + 1 = right - left - 1
    return right - left - 1


def longest_palindrome(s):
    """
    가장 긴 팰린드롬 부분 문자열을 반환한다.

    시간 복잡도 O(N^2), 공간 복잡도 O(1)

    핵심: 팰린드롬은 항상 중심을 가진다. 중심은 총 2N-1개
          (문자 하나가 중심인 홀수 길이 N개 + 문자 사이가 중심인 짝수 길이 N-1개)
    """
    # 빈 문자열이면 확장할 중심 자체가 없다.
    if not s:
        return ""

    # 지금까지 찾은 가장 긴 팰린드롬의 시작/끝 인덱스
    start, end = 0, 0

    # 모든 위치를 중심으로 삼아 확장을 시도한다.
    for i in range(len(s)):
        # 홀수 길이 팰린드롬: 중심이 문자 하나 (예: "aba")
        odd_len = expand_from_center(s, i, i)
        # 짝수 길이 팰린드롬: 중심이 문자 사이 (예: "abba")
        even_len = expand_from_center(s, i, i + 1)
        # 두 경우 중 더 긴 쪽을 이번 중심의 결과로 삼는다.
        length = max(odd_len, even_len)

        # 기존 최장 길이(end - start + 1)보다 길면 갱신한다.
        if length > end - start + 1:
            # 중심 i에서 길이 length가 나왔을 때의 시작/끝 인덱스를 역산한다.
            start = i - (length - 1) // 2
            end = i + length // 2

    # 슬라이싱은 끝 인덱스를 포함하지 않으므로 +1
    return s[start:end + 1]


# ============================================================================
# 3. 이분 탐색 - 첫 위치 / 마지막 위치   (10_binary_search.py 변형)
# ============================================================================
def find_first(arr, target):
    """
    target이 처음(가장 왼쪽) 등장하는 인덱스를 반환한다. 없으면 -1
    시간 복잡도 O(log N), 공간 복잡도 O(1)
    """
    left, right = 0, len(arr) - 1
    # 찾지 못했을 때를 대비해 -1로 초기화한다.
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # 바로 반환하지 않고 답 후보로만 저장한다.
            answer = mid
            # 더 왼쪽에도 같은 값이 있을 수 있으므로 왼쪽 범위를 계속 탐색한다.
            right = mid - 1
        elif arr[mid] < target:
            # 가운데 값이 작으면 정답은 오른쪽에 있다.
            left = mid + 1
        else:
            # 가운데 값이 크면 정답은 왼쪽에 있다.
            right = mid - 1

    return answer


def find_last(arr, target):
    """
    target이 마지막(가장 오른쪽) 등장하는 인덱스를 반환한다. 없으면 -1
    (10_binary_search.py 에 작성한 코드가 사실 이 동작이다)
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            # find_first와 반대로, 더 오른쪽을 계속 탐색한다.
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def count_target(arr, target):
    """
    정렬된 배열에서 target의 개수를 O(log N)에 센다.
    """
    first = find_first(arr, target)
    # 존재하지 않으면 개수는 0 (이 처리를 빼면 -1 - -1 + 1 = 1 이라는 오답이 나온다)
    if first == -1:
        return 0
    return find_last(arr, target) - first + 1


# ============================================================================
# 4. 피보나치 - 반복문 버전   (05_recursion.py 변형)
# ============================================================================
def fibonacci_iterative(n):
    """
    반복문으로 n번째 피보나치 수를 구한다.

    시간 복잡도 O(N)
    공간 복잡도 O(1)  (메모이제이션 O(N), 재귀 호출 스택 O(N)이 필요 없다)
    """
    # fib(0) = 0, fib(1) = 1 은 그대로 반환한다.
    if n < 2:
        return n

    # prev = fib(0), curr = fib(1) 에서 시작한다.
    prev, curr = 0, 1

    # 2번째부터 n번째까지 한 칸씩 앞으로 밀며 계산한다.
    for _ in range(2, n + 1):
        # 오른쪽 식이 먼저 모두 계산된 뒤 한 번에 할당되므로 임시 변수가 필요 없다.
        prev, curr = curr, prev + curr

    return curr


# ============================================================================
# 5. 순열 생성   (06_backtracking.py 변형)
# ============================================================================
def permutations(n, k):
    """
    1 ~ n 중 k개를 뽑아 만드는 모든 순열을 반환한다.

    조합과의 차이:
      조합: backtrack(num + 1, ...) 로 "고른 수보다 큰 수만" 시도 -> 순서 무시
      순열: 매번 1부터 모두 시도하되 이미 쓴 수만 used로 걸러냄  -> 순서 구분
    """
    result = []
    # 숫자 1 ~ n 을 인덱스 그대로 쓰기 위해 n+1 크기로 만든다. (0번은 사용 안 함)
    used = [False] * (n + 1)

    def backtrack(current):
        # Base Case: k개를 다 골랐으면 하나의 순열이 완성된 것이다.
        if len(current) == k:
            # current는 이후 append/pop으로 계속 바뀌므로 복사본을 저장한다.
            result.append(current[:])
            return

        # 조합과 달리 start가 없다. 매번 1부터 모든 숫자를 후보로 본다.
        for num in range(1, n + 1):
            # 이미 이번 순열에서 사용한 숫자는 건너뛴다.
            if used[num]:
                continue

            # [Choose] 숫자를 선택하고 사용 표시를 남긴다.
            used[num] = True
            current.append(num)

            # [Explore] 다음 자리를 채우러 더 깊이 들어간다.
            backtrack(current)

            # [Unchoose] 다른 숫자를 시도하기 위해 선택을 되돌린다.
            # pop() 만 하고 used를 되돌리지 않으면 그 숫자를 영영 못 쓰게 된다.
            current.pop()
            used[num] = False

    backtrack([])
    return result


# ============================================================================
# 6. 괄호 검사 - (), {}, [] 세 종류   (12_stack.py 변형)
# ============================================================================
def is_valid_brackets(s):
    """
    세 종류의 괄호가 올바르게 짝지어졌는지 확인한다.
    시간 복잡도 O(N), 공간 복잡도 O(N)
    """
    # 닫는 괄호 -> 짝이 되는 여는 괄호
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # 여는 괄호는 나중에 짝을 맞추기 위해 스택에 쌓는다.
        if char in "({[":
            stack.append(char)

        # 닫는 괄호는 가장 최근에 열린 괄호와 짝이 맞아야 한다. (LIFO)
        elif char in pairs:
            # 스택이 비어 있으면 짝이 될 여는 괄호가 없다.
            if not stack:
                return False
            # 짝 종류까지 확인해야 "([)]" 를 걸러낼 수 있다.
            # ')'를 만났을 때 pop한 값이 '[' 이므로 False
            if stack.pop() != pairs[char]:
                return False

        # 괄호가 아닌 문자는 무시한다.

    # 모든 문자를 확인한 뒤 스택이 비어 있어야 모든 짝이 맞은 것이다.
    return not stack


# ============================================================================
# 7. 해시 테이블 - 체이닝 방식 직접 구현   (15_hash_table.py 변형)
# ============================================================================
class ChainingHashTable:
    """
    충돌을 체이닝으로 해결하는 해시 테이블.

    체이닝    : 같은 버킷에 충돌이 나면 그 자리에 리스트로 이어 붙인다.
    개방 주소법: 충돌이 나면 다른 빈 칸을 찾아가 저장한다.

    평균 O(1) / 최악 O(N) - 최악은 모든 키가 한 버킷에 몰린 경우
    """

    def __init__(self, size=8):
        self.size = size
        # 각 버킷은 (key, value) 튜플을 담는 리스트 = 체인
        # [[]] * size 로 만들면 같은 리스트가 복제되어 버그가 생기므로 컴프리헨션을 쓴다.
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        """키의 해시값을 버킷 개수로 나눈 나머지 = 저장 위치"""
        # 이 나머지 연산 때문에 서로 다른 키가 같은 위치를 가리킬 수 있다 = 충돌
        return hash(key) % self.size

    def put(self, key, value):
        """삽입 또는 갱신"""
        bucket = self.buckets[self._index(key)]

        # 같은 키가 이미 체인에 있으면 값만 덮어쓴다.
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # 없으면 체인 끝에 새로 매단다. (충돌이 나도 기존 데이터가 밀려나지 않는다)
        bucket.append((key, value))

    def get(self, key):
        """조회. 없으면 None"""
        # 버킷 위치는 O(1)에 찾지만, 체인 안에서는 순차 탐색이 필요하다.
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return None


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
