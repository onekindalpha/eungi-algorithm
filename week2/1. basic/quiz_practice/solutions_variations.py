"""
[심화 변형 7문제 - 정답 예시]

week2/1. basic 의 기본 문제에서 "한 단계 확장"된 형태로 자주 출제되는 변형들입니다.
먼저 practice_variations.py 에서 직접 작성해 본 뒤, 이 파일과 비교해 보세요.

1. Two Sum        (04 변형) : 해시맵으로 O(N)
2. 팰린드롬       (01 변형) : 가장 긴 팰린드롬 부분 문자열 (중심 확장)
3. 이분 탐색      (10 변형) : 가장 왼쪽 / 가장 오른쪽 등장 위치
4. 피보나치       (05 변형) : 반복문으로 O(N) 시간, O(1) 공간
5. 순열           (06 변형) : 조합이 아닌 순열 생성
6. 괄호 검사      (12 변형) : (), {}, [] 세 종류 모두 검사
7. 해시 충돌      (15 변형) : 체이닝 방식 해시 테이블 직접 구현
"""


# ============================================================================
# 1. Two Sum - 해시맵으로 O(N)  (04_brute_force.py 변형)
# ============================================================================
def two_sum_hash(nums, target):
    """
    합이 target이 되는 모든 (i, j) 인덱스 쌍을 찾는다. (i < j)

    기존 완전 탐색: 시간 O(N^2)
    해시맵 방식   : 시간 O(N + K), 공간 O(N)   K는 정답 쌍의 개수

    핵심 아이디어:
    "두 수를 모두 고른다"가 아니라 "지금 수를 고정하고, 짝이 되는 수를 이미 봤는지 조회한다"
    """
    # 이미 지나온 값 -> 그 값이 등장했던 인덱스 목록
    # 같은 값이 여러 번 나올 수 있으므로 인덱스를 리스트로 모아 둔다.
    seen = {}
    # 조건을 만족하는 인덱스 쌍을 저장할 리스트
    pairs = []

    # 배열을 앞에서부터 한 번만 순회한다.
    for j, num in enumerate(nums):
        # 현재 값과 더해서 target이 되는 값(짝)을 계산한다.
        complement = target - num

        # 짝이 되는 값을 이전에 본 적이 있다면, 그 인덱스들과 모두 쌍을 이룬다.
        # 딕셔너리 조회는 평균 O(1)이므로 이중 반복문이 사라진다.
        if complement in seen:
            for i in seen[complement]:
                pairs.append((i, j))

        # 현재 값과 인덱스를 기록해 두어 뒤에 오는 원소가 조회할 수 있게 한다.
        # setdefault: 키가 없으면 빈 리스트를 만들고, 있으면 기존 리스트를 가져온다.
        seen.setdefault(num, []).append(j)

    # 완전 탐색과 결과 "집합"은 같지만 담기는 순서는 다를 수 있다.
    return pairs


# ============================================================================
# 2. 가장 긴 팰린드롬 부분 문자열 - 중심 확장  (01_string.py 변형)
# ============================================================================
def expand_from_center(s, left, right):
    """
    (left, right)를 중심으로 양쪽으로 벌리면서 팰린드롬인 동안 확장한다.

    Returns:
        확장이 끝난 시점의 팰린드롬 길이
    """
    # 인덱스가 문자열 범위를 벗어나지 않고, 양쪽 문자가 같은 동안 계속 벌린다.
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # while이 끝난 시점의 left, right는 "팰린드롬이 아닌" 한 칸 바깥이다.
    # 따라서 실제 팰린드롬 길이는 (right - 1) - (left + 1) + 1 = right - left - 1
    return right - left - 1


def longest_palindrome(s):
    """
    가장 긴 팰린드롬 부분 문자열을 반환한다.

    시간 복잡도: O(N^2) - 각 중심마다 최대 N까지 확장
    공간 복잡도: O(1)   - 인덱스 변수만 사용

    핵심 아이디어:
    팰린드롬은 항상 "중심"을 가진다. 중심은 2N-1개 (문자 N개 + 문자 사이 N-1개).
    """
    # 빈 문자열이면 확장할 중심 자체가 없다.
    if not s:
        return ""

    # 지금까지 찾은 가장 긴 팰린드롬의 시작/끝 인덱스
    start, end = 0, 0

    # 모든 위치를 중심으로 삼아 확장을 시도한다.
    for i in range(len(s)):
        # 길이가 홀수인 팰린드롬: 중심이 문자 하나 (예: "aba")
        odd_len = expand_from_center(s, i, i)
        # 길이가 짝수인 팰린드롬: 중심이 문자 사이 (예: "abba")
        even_len = expand_from_center(s, i, i + 1)
        # 두 경우 중 더 긴 쪽을 이번 중심의 결과로 삼는다.
        length = max(odd_len, even_len)

        # 기존 최장 길이(end - start + 1)보다 길면 갱신한다.
        if length > end - start + 1:
            # 중심 i에서 길이 length가 나왔을 때의 시작/끝 인덱스를 역산한다.
            start = i - (length - 1) // 2
            end = i + length // 2

    # 파이썬 슬라이싱은 끝 인덱스를 포함하지 않으므로 +1
    return s[start:end + 1]


# ============================================================================
# 3. 이분 탐색 - 가장 왼쪽 / 가장 오른쪽 등장 위치  (10_binary_search.py 변형)
# ============================================================================
def find_first(arr, target):
    """
    target이 처음(가장 왼쪽) 등장하는 인덱스를 반환한다. 없으면 -1

    시간 복잡도: O(log N), 공간 복잡도: O(1)
    """
    left, right = 0, len(arr) - 1
    # 찾지 못했을 때를 대비해 -1로 초기화한다.
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # 일단 답 후보로 저장한다.
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

    10_binary_search.py 에 작성한 코드와 동일한 동작이다.
    (찾아도 멈추지 않고 left = mid + 1 로 오른쪽을 계속 보기 때문)
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            # 더 오른쪽에도 같은 값이 있을 수 있으므로 오른쪽 범위를 계속 탐색한다.
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def count_target(arr, target):
    """
    정렬된 배열에서 target의 개수를 O(log N)에 센다.

    핵심: (마지막 위치 - 첫 위치 + 1)
    """
    first = find_first(arr, target)
    # 존재하지 않으면 개수는 0
    if first == -1:
        return 0
    return find_last(arr, target) - first + 1


# ============================================================================
# 4. 피보나치 - 반복문 버전  (05_recursion.py 변형)
# ============================================================================
def fibonacci_iterative(n):
    """
    반복문으로 n번째 피보나치 수를 구한다.

    시간 복잡도: O(N)
    공간 복잡도: O(1) - 메모이제이션(O(N))이나 재귀 스택(O(N))이 필요 없다.

    핵심 아이디어:
    fib(n)을 구하는 데 필요한 것은 직전 두 값뿐이다. 전부 저장할 이유가 없다.
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
# 5. 순열 생성  (06_backtracking.py 변형)
# ============================================================================
def permutations(n, k):
    """
    1 ~ n 중에서 k개를 뽑아 만드는 모든 순열을 반환한다.

    조합과의 차이 (딱 한 군데):
      조합: backtrack(num + 1, ...)  -> 고른 수보다 큰 수만 시도 = 순서 무시
      순열: 매번 1부터 다시 시도하되, 이미 쓴 수만 used로 걸러냄 = 순서 구분
    """
    result = []
    # 인덱스를 1 ~ n 그대로 쓰기 위해 n+1 크기로 만든다. (0번은 사용하지 않음)
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
            current.pop()
            used[num] = False

    backtrack([])
    return result


# ============================================================================
# 6. 괄호 검사 - (), {}, [] 세 종류  (12_stack.py 변형)
# ============================================================================
def is_valid_brackets(s):
    """
    세 종류의 괄호가 올바르게 짝지어졌는지 확인한다.

    시간 복잡도: O(N), 공간 복잡도: O(N)

    기존 코드와의 차이:
    닫는 괄호를 만났을 때 "스택이 비었는지"뿐 아니라
    "pop한 여는 괄호가 짝이 맞는 종류인지"까지 확인해야 한다.
    """
    # 닫는 괄호 -> 짝이 되는 여는 괄호
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # 여는 괄호는 나중에 짝을 맞추기 위해 스택에 쌓는다.
        if char in "({[":
            stack.append(char)

        # 닫는 괄호를 만나면 가장 최근에 열린 괄호와 짝이 맞아야 한다. (LIFO)
        elif char in pairs:
            # 스택이 비어 있으면 짝이 될 여는 괄호가 없다.
            if not stack:
                return False
            # 가장 최근 여는 괄호가 이 닫는 괄호의 짝이 아니면 잘못된 괄호다.
            # 예: "([)]" -> ')'를 만났을 때 pop한 값은 '[' 이므로 False
            if stack.pop() != pairs[char]:
                return False

        # 괄호가 아닌 문자는 무시한다.

    # 모든 문자를 확인한 뒤 스택이 비어 있어야 모든 짝이 맞은 것이다.
    return not stack


# ============================================================================
# 7. 해시 테이블 - 체이닝(Chaining) 방식 직접 구현  (15_hash_table.py 변형)
# ============================================================================
class ChainingHashTable:
    """
    충돌을 체이닝으로 해결하는 해시 테이블.

    체이닝    : 같은 버킷에 여러 데이터가 오면 그 자리에 리스트로 이어 붙인다.
    개방 주소법: 충돌이 나면 다른 빈 칸(다음 칸 등)을 찾아가 저장한다.

    평균 시간 복잡도 O(1) / 최악 O(N)
      - 최악은 모든 키가 같은 버킷으로 몰려 리스트를 처음부터 훑어야 하는 경우
    """

    def __init__(self, size=8):
        # 버킷 개수 (작을수록 충돌이 자주 일어난다)
        self.size = size
        # 각 버킷은 (key, value) 튜플을 담는 리스트 = 체인
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        """키를 해시값으로 바꾼 뒤 버킷 개수로 나눈 나머지 = 저장 위치"""
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

        # 없으면 체인 끝에 새로 매단다. (충돌이 나도 데이터가 밀려나지 않는다)
        bucket.append((key, value))

    def get(self, key):
        """조회. 없으면 None"""
        # 버킷은 O(1)에 찾지만, 체인 안에서는 순차 탐색이 필요하다.
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return None

    def show(self):
        """어떤 버킷에 충돌이 일어났는지 눈으로 확인하는 헬퍼"""
        for i, bucket in enumerate(self.buckets):
            if bucket:
                mark = "  <- 충돌!" if len(bucket) > 1 else ""
                print(f"  버킷[{i}]: {bucket}{mark}")


# ============================================================================
# 테스트
# ============================================================================
if __name__ == "__main__":
    print("=== 1. Two Sum - 해시맵 O(N) ===")
    print(f"[2,7,11,15], target=9  -> {two_sum_hash([2, 7, 11, 15], 9)}")
    print(f"[1,3,4,2,5,6], target=7 -> {two_sum_hash([1, 3, 4, 2, 5, 6], 7)}")
    print(f"[1,1,1,1], target=2    -> {two_sum_hash([1, 1, 1, 1], 2)}")
    print()

    print("=== 2. 가장 긴 팰린드롬 부분 문자열 ===")
    for text in ["babad", "cbbd", "abacdfgdcaba", "a"]:
        print(f"\"{text}\" -> \"{longest_palindrome(text)}\"")
    print()

    print("=== 3. 이분 탐색 - 첫/마지막 위치 ===")
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    print(f"배열: {arr}")
    print(f"2의 첫 위치: {find_first(arr, 2)}, 마지막 위치: {find_last(arr, 2)}, 개수: {count_target(arr, 2)}")
    print(f"4의 첫 위치: {find_first(arr, 4)}, 마지막 위치: {find_last(arr, 4)}, 개수: {count_target(arr, 4)}")
    print(f"9의 첫 위치: {find_first(arr, 9)}, 개수: {count_target(arr, 9)}")
    print()

    print("=== 4. 피보나치 - 반복문 O(1) 공간 ===")
    print(f"fib 0~9: {[fibonacci_iterative(i) for i in range(10)]}")
    print(f"fib(50) = {fibonacci_iterative(50)}  (재귀로는 사실상 불가능한 크기)")
    print()

    print("=== 5. 순열 vs 조합 ===")
    perms = permutations(3, 2)
    print(f"P(3,2) = {perms}  -> 총 {len(perms)}개")
    print("C(3,2) = [[1, 2], [1, 3], [2, 3]]  -> 총 3개 (순서를 따지지 않아 절반)")
    print()

    print("=== 6. 괄호 검사 - 세 종류 ===")
    for test in ["(){}[]", "([{}])", "([)]", "(()", "{[()]}"]:
        print(f"\"{test}\" -> {is_valid_brackets(test)}")
    print()

    print("=== 7. 해시 테이블 - 체이닝 ===")
    table = ChainingHashTable(size=4)   # 버킷을 일부러 작게 만들어 충돌을 유도
    for name, score in [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95), ("Eve", 88)]:
        table.put(name, score)
    table.show()
    print(f"  get('Bob')   -> {table.get('Bob')}")
    print(f"  get('Frank') -> {table.get('Frank')}")
