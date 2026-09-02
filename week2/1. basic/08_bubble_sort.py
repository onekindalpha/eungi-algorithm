"""
[버블 정렬 구현]

문제 설명:
- 버블 정렬(Bubble Sort) 알고리즘을 구현합니다.
- 인접한 두 원소를 비교하여 정렬하는 방식입니다.
- 가장 큰 원소가 배열의 끝으로 "버블"처럼 이동합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [64, 34, 25, 12, 22, 11, 90]
출력: [11, 12, 22, 25, 34, 64, 90]

힌트:
- 외부 반복문: n-1번 실행
- 내부 반복문: 인접한 원소 비교 및 교환
- 최적화: 교환이 없으면 이미 정렬된 것이므로 조기 종료
"""

def bubble_sort(arr):
    """
    버블 정렬 구현
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    # 시간 복잡도: O(N²)
    # 공간 복잡도: O(1)
    n = len(arr)

    # TODO: 외부 반복문 - n-1번 반복
    # 각 패스마다 가장 큰 원소가 배열의 끝으로 이동한다. 
    for i in range(n-1):
    ## TODO: 내부 반복문 - 인접한 원소 비교
        # 이미 정렬된 뒤쪽 원소는 제외하고
        # 인접한 두 원소를 비교한다. 
        for j in range(0, n-1-i):
            # 앞의 원소가 뒤의 원소보다 크면 두 원소를 교환한다. 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    ## TODO: 인접한 두 원소 비교 및 교환
    # 정렬된 배열을 반환한다. 
    return arr

def bubble_sort_optimized(arr):
    """
    최적화된 버블 정렬 (조기 종료 포함)
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    # 최악의 경우 시간 복잡도: O(N²)
    # 이미 정렬된 경우 시간 복잡도: O(N)
    # 공간 복잡도: O(1)
    n = len(arr)
    # 탐색할 범위가 1개 이하가 될 때까지 반복한다. 
    while n > 1:
        # 이번 패스에서 마지막으로 교환된 위치를 저장한다. 
        # 교환이 한 번도 일어나지 않으면 0을 유지한다. 
        last_swap = 0 

        # TODO: 내부 반복문과 교환 로직 구현
        # 현재 정렬 범위에서 인접한 원소를 비교한다. 
        for j in range(0, n-1):
            # 앞의 원소가 뒤의 원소보다 크면 두 원소를 교환한다. 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # 현재 위치에서 교환이 일어났음을 기록한다. 
                last_swap = j+1
        # TODO: 
        # 마지막으로 교환된 위치까지만 다음 패스에서 확인한다. 
        # 그 뒤쪽은 이미 정렬된 상태이므로 다시 비교할 필요가 없다. 
        n = last_swap
    # 정렬된 배열을 반환한다. 
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = bubble_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2: 이미 정렬된 배열
    arr2 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 2: 이미 정렬됨 ===")
    print(f"정렬 전: {arr2}")
    result2 = bubble_sort_optimized(arr2.copy())
    print(f"정렬 후: {result2}")
    print("최적화 버전은 1번의 패스만 수행")
    print()
    
    # 테스트 케이스 3: 역순 배열
    arr3 = [5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = bubble_sort(arr3.copy())
    print(f"정렬 후: {result3}")


