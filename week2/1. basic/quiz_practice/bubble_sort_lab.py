"""
[버블 정렬 - 3가지 버전 비교 실습]

08_bubble_sort.py 에서 작성한 코드를 확장해, 최적화가 실제로 무엇을 줄이는지
비교 횟수 / 교환 횟수 / 패스 수를 직접 세어 눈으로 확인합니다.

버전 1) 기본형          : 항상 n-1번의 패스를 끝까지 돈다.
버전 2) swapped 플래그  : 한 패스에서 교환이 한 번도 없으면 즉시 종료한다.
버전 3) last_swap 축소  : 마지막으로 교환된 위치까지만 다음 패스를 돈다. (가장 강함)

핵심 질문:
- 최선 / 평균 / 최악 시간 복잡도는?  -> O(N) / O(N^2) / O(N^2)   (버전 2, 3 기준)
- 버전 1은 왜 이미 정렬된 배열에도 O(N^2)인가?  -> 교환이 없어도 반복문을 계속 돌기 때문
- 버블 정렬은 왜 안정 정렬(stable)인가?         -> 값이 "같을 때"는 교환하지 않기 때문
"""


# ============================================================================
# 버전 1) 기본형 - 08_bubble_sort.py 의 bubble_sort()
# ============================================================================
def bubble_sort_basic(arr):
    """
    시간 복잡도: 최선/평균/최악 모두 O(N^2)
    공간 복잡도: O(1) - 원본 배열 안에서 교환만 한다 (in-place)

    Returns:
        (정렬된 배열, 비교 횟수, 교환 횟수, 패스 수)
    """
    n = len(arr)
    comparisons = swaps = passes = 0

    # 패스를 n-1번 "무조건" 반복한다. 이미 정렬되어 있어도 멈추지 않는다.
    for i in range(n - 1):
        passes += 1
        # 뒤쪽 i개는 이미 제자리를 찾았으므로 비교 범위에서 제외한다.
        for j in range(0, n - 1 - i):
            comparisons += 1
            # 앞의 원소가 더 크면 두 원소를 교환한다.
            # 같을 때(==)는 교환하지 않기 때문에 같은 값의 순서가 유지된다 = 안정 정렬
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps, passes


# ============================================================================
# 버전 2) swapped 플래그 - 교환이 없으면 조기 종료
# ============================================================================
def bubble_sort_flag(arr):
    """
    시간 복잡도: 최선 O(N) (이미 정렬된 경우 1패스로 종료) / 최악 O(N^2)
    공간 복잡도: O(1)

    아이디어: 한 패스 동안 교환이 한 번도 없었다면 = 모든 인접 쌍이 정렬되어 있다 = 끝.
    """
    n = len(arr)
    comparisons = swaps = passes = 0

    for i in range(n - 1):
        passes += 1
        # 이번 패스에서 교환이 일어났는지 기록하는 깃발
        swapped = False

        for j in range(0, n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        # 교환이 한 번도 없었다면 이미 정렬이 끝난 것이므로 남은 패스를 생략한다.
        if not swapped:
            break

    return arr, comparisons, swaps, passes


# ============================================================================
# 버전 3) last_swap 범위 축소 - 08_bubble_sort.py 의 bubble_sort_optimized()
# ============================================================================
def bubble_sort_last_swap(arr):
    """
    시간 복잡도: 최선 O(N) / 최악 O(N^2)
    공간 복잡도: O(1)

    아이디어: 마지막으로 교환이 일어난 위치 뒤쪽은 이미 정렬이 끝난 구간이다.
    깃발 방식이 "교환이 아예 없을 때만" 멈추는 데 비해,
    이 방식은 매 패스마다 정렬이 끝난 꼬리를 한 번에 여러 칸 잘라낸다.
    """
    n = len(arr)
    comparisons = swaps = passes = 0

    # 확인해야 할 범위가 1개 이하가 되면 정렬이 끝난 것이다.
    while n > 1:
        passes += 1
        # 이번 패스에서 마지막으로 교환된 위치. 교환이 없으면 0으로 남는다.
        last_swap = 0

        for j in range(0, n - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                # 교환이 일어난 오른쪽 인덱스를 기록해 둔다.
                last_swap = j + 1

        # 다음 패스는 마지막 교환 지점까지만 확인하면 된다.
        # 교환이 없었다면 last_swap = 0 이므로 while 조건에서 바로 종료된다.
        n = last_swap

    return arr, comparisons, swaps, passes


# ============================================================================
# 패스별 진행 과정 출력 (손으로 트레이스할 때 답 맞춰보기용)
# ============================================================================
def bubble_sort_trace(arr):
    """한 패스가 끝날 때마다 배열 상태를 출력한다."""
    arr = arr[:]
    n = len(arr)
    print(f"  시작      : {arr}")

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 이번 패스에서 확정된 원소(맨 뒤 i+1개)를 표시한다.
        fixed = arr[n - 1 - i:]
        print(f"  패스 {i + 1} 후 : {arr}   확정: {fixed}")
        if not swapped:
            print(f"  -> 교환 없음. 조기 종료 (총 {i + 1}패스)")
            break

    return arr


# ============================================================================
# 테스트
# ============================================================================
if __name__ == "__main__":
    print("=== 패스별 진행 과정 ===")
    bubble_sort_trace([64, 34, 25, 12, 22, 11, 90])
    print()

    print("=== 이미 정렬된 배열 (최선의 경우) ===")
    bubble_sort_trace([1, 2, 3, 4, 5])
    print()

    # 세 버전을 같은 입력으로 비교한다.
    cases = {
        "이미 정렬 [1..10]": list(range(1, 11)),
        "역순      [10..1]": list(range(10, 0, -1)),
        "거의 정렬 (뒤 2개만 뒤바뀜)": list(range(1, 9)) + [10, 9],
        "무작위": [7, 2, 9, 1, 5, 10, 3, 8, 4, 6],
    }

    versions = [
        ("기본형", bubble_sort_basic),
        ("swapped 플래그", bubble_sort_flag),
        ("last_swap 축소", bubble_sort_last_swap),
    ]

    print("=== 버전별 비교 (배열 크기 10) ===")
    for case_name, data in cases.items():
        print(f"\n[{case_name}]")
        print(f"  {'버전':<16}{'비교':>6}{'교환':>6}{'패스':>6}")
        for version_name, sort_func in versions:
            # 각 버전이 같은 입력을 받도록 복사본을 넘긴다.
            result, comparisons, swaps, passes = sort_func(data[:])
            print(f"  {version_name:<16}{comparisons:>6}{swaps:>6}{passes:>6}")
            # 정렬 결과가 올바른지 항상 확인한다.
            assert result == sorted(data), "정렬 결과가 올바르지 않습니다"

    print("\n=== 정리 ===")
    print("- 이미 정렬된 배열: 기본형은 45번 비교, 최적화 버전은 9번 비교 -> O(N^2) vs O(N)")
    print("- 역순 배열: 세 버전 모두 O(N^2). 최적화는 '이미 정렬된 부분'이 있을 때만 이득")
    print("- 무작위 배열에서는 last_swap 방식이 플래그 방식보다 비교 횟수가 조금 더 적다 (38 vs 39)")
    print("  -> 플래그는 '교환이 아예 없을 때'만 멈추지만, last_swap은 매 패스마다 꼬리를 잘라내기 때문")
    print("- 세 버전 모두 공간 복잡도 O(1) (in-place), 안정 정렬(stable)")
