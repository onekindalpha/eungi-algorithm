"""
[이분 탐색 - Binary Search]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색 알고리즘을 구현합니다.
- 배열을 반으로 나누어 탐색 범위를 절반씩 줄여갑니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
출력: 3

힌트:
- left, right 포인터 사용
- mid = (left + right) // 2
- arr[mid]와 target 비교하여 범위 조정
"""

def binary_search(arr, target):
    """
    이분 탐색 구현
    
    Args:
        arr: 정렬된 배열
        target: 찾을 값
    
    Returns:
        target의 인덱스 (없으면 -1)
    """
    # 시간 복잡도: O(log N) - 탐색 범위를 매번 절반으로 줄인다.
    # 공간 복잡도: O(1) - 추가 배열 없이 변수만 사용한다.
    
    # 탐색 범위의 시작 인덱스
    left = 0
    # 탐색 범위의 끝 인덱스
    # 마지막 인덱스는 배열의 길이 -1 이다. 
    right = len(arr) - 1
    # target을 찾았을 때 인덱스를 저장할 변수
    # 아직 찾지 못햇으면 -1을 유지한다. 
    top = -1

    # TODO: 
    # 탐색할 범위가 존재하는 동안 반복한다. 
    # left > right가 되면 탐색할 범위가 사라진 것이다.  
    while left <= right:
        # 현재 탐색 범위의 가운데 인덱스를 구한다.   
        mid = (left + right) // 2
        # 가운데 값이 target과 같으면 위치를 저장한다. 
        if arr[mid] == target:
            top = mid
            # target을 찾았더라도 더 뒤에 같은 값이 있을 수 있으므로
            # 오른쪽 범위에서 계속 탐색한다. 
            left = mid + 1
        # target이 가운데 값보다 크면 오른쪽 절반을 탐색한다. 
        elif target > arr[mid]:
            left = mid + 1     
        # target이 가운데 값보다 작으면 왼쪽 절반을 탐색한다. 
        else:
            right = mid - 1
    # target을 찾았다면 저장한 인덱스를 반환하고,
    # 찾지 못했다면 처음부터 유지된 -1을 반환한다.  
    return top

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()
    
    # 테스트 케이스 3: 없는 값
    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")
