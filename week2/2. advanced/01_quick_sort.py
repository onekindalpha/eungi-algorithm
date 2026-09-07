"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""

def partition(arr, low, high):
    """
    배열을 피벗 기준으로 분할하는 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    
    Returns:
        피벗의 최종 위치 인덱스
    """
    # TODO: 피벗을 선택 (일반적으로 마지막 원소)
    pivot = arr[high]
    
    # TODO: i는 작은 원소들의 마지막 인덱스를 추적
    # 지금까지 찾은 작은 값들을 모아놓은 영역의 끝 위치를 가리킴. 
    # i는 피벗보다 작거나 같은 값들의 영역을 표시한다고 할 수 있음.
    # 작은 값이 들어갈 위치의 바로 앞에서 시작.   
    i = low -1
    
    # TODO: low부터 high-1까지 순회하면서
    ## 현재 원소가 피벗보다 작거나 같으면:
    ##   1. i를 1 증가
    ##   2. arr[i]와 arr[j]를 교환
    for j in range(low, high):
        # for j 안에서는 작은 값들을 앞으로 모음. j는 low부터 high-1까지 이동하면서 피벗보다 작거나 같은 값을 찾는다.
        if arr[j] <= pivot:
            # 그리고 pivot보다 작은 값을 찾게 되면
            # i를 1 증가시켜 작은 값이 들어갈 다음 위치로 이동. 
            i+=1
            # arr[i]와 arr[j]를 교환해서, 찾은 작은 값을 작은 값 영역에 넣는다.
            arr[i], arr[j] = arr[j], arr[i]
            # TODO: 피벗을 올바른 위치(i+1)에 배치
    # j의 탐색이 끝나면 i는 작은 값 영역의 마지막 위치를 가리킨다. 따라서 i+1이 피벗이 들어갈 위치가 된다.
    arr[i+1], arr[high]= arr[high], arr[i+1]
    # 피벗의 최종 인덱스를 반환한다.
    return i + 1

def quick_sort_helper(arr, low, high):
    """
    퀵 정렬 재귀 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    """
    # TODO: base case - low가 high보다 작을 때만 정렬
    # low == high이면 원소가 1개이고, low > high이면 정렬할 구간이 없으므로 종료한다.
    if low < high:
        ## 분할하여 피벗 인덱스 얻기
        p = partition(arr, low, high)
        ## 피벗 왼쪽 부분 재귀 정렬
        quick_sort_helper(arr, low, p-1)
        ## 피벗 오른쪽 부분 재귀 정렬
        quick_sort_helper(arr, p+1, high)
    else:
        return
    

def quick_sort(arr):
    """
    퀵 정렬 메인 함수
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    # 처음에 배열 전체를 정렬하는 것. 
    # arr: 정렬할 배열, low: 현재 정렬 구간의 시작 인덱스, high: 현재 정렬 구간의 마지막 인덱스. 
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")


