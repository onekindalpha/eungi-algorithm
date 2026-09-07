"""
[완전 탐색 - 배열에서 두 수의 합 찾기]

문제 설명:
- 정수 배열과 목표 값이 주어졌을 때, 배열에서 두 수를 선택하여 
  그 합이 목표 값과 같아지는 모든 쌍을 찾습니다.
- 완전 탐색(Brute Force) 방식으로 모든 경우를 확인합니다.

입력:
- nums: 정수 배열
- target: 목표 합

출력:
- 합이 target이 되는 (i, j) 인덱스 쌍의 리스트 (i < j)

예제:
입력: nums = [2, 7, 11, 15, 3], target = 9
출력: [(0, 1), (0, 4)]
설명: nums[0] + nums[1] = 2 + 7 = 9
      nums[0] + nums[4] = 2 + 7 = 9 (중복이지만 인덱스가 다름)

실제로는: nums[0] + nums[1] = 2 + 7 = 9만 해당

힌트:
- 이중 반복문을 사용하여 모든 쌍을 확인하세요
- i < j 조건을 유지하여 중복을 방지하세요
"""

def find_two_sum_pairs(nums, target):
    """
    배열에서 합이 target이 되는 모든 인덱스 쌍 찾기
    
    Args:
        nums: 정수 배열
        target: 목표 합
    
    Returns:
        list: (i, j) 인덱스 쌍의 리스트
    """
    # 시간 복잡도: O(N²) - 모든 두 원소의 조합을 확인한다.
    # 공간 복잡도: O(K) - 조건을 만족하는 인덱스 쌍을 pairs에 저장한다.
    # 합이 target이 되는 인덱스 쌍을 저장할 리스트
    pairs = []
    # 배열의 길이
    n = len(nums)
    
    # TODO: 이중 반복문으로 모든 쌍을 확인하세요
    # 첫 번째 원소의 인덱스를 선택한다. 
    for i in range(n):
        # 두 번째 원소는 i보다 뒤에 있느 원소만 선택한다. 
        # i +1 부터 시작하여 같은 쌍을 중복해서 확인하지 않는다. 
        for j in range(i+1, n):
            # 두 원소의 합이 target과 같으면 인덱스 쌍을 저장한다. 
            if (nums[i] + nums[j]) == target:
                pairs.append((i, j))
    # 조건을 만족하는 모든 인덱스 쌍을 반환한다. 
    return pairs

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_two_sum_pairs(nums1, target1)
    print(f"배열: {nums1}")
    print(f"목표 합: {target1}")
    print(f"결과 쌍: {result1}")
    print()
    
    # 테스트 케이스 2
    nums2 = [1, 3, 4, 2, 5, 6]
    target2 = 7
    result2 = find_two_sum_pairs(nums2, target2)
    print(f"배열: {nums2}")
    print(f"목표 합: {target2}")
    print(f"결과 쌍: {result2}")
    print()
    
    # 테스트 케이스 3
    nums3 = [1, 1, 1, 1]
    target3 = 2
    result3 = find_two_sum_pairs(nums3, target3)
    print(f"배열: {nums3}")
    print(f"목표 합: {target3}")
    print(f"결과 쌍: {result3}")


