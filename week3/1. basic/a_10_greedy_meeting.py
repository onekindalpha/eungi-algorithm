"""
[그리디 + heapq - 최소 회의실 개수]

문제 설명:
- 여러 개의 회의가 있고, 각 회의는 시작 시간과 종료 시간이 있음.
- 회의실은 여러 개 써도 되지만, 주어진 회의를 하나도 빠짐없이 전부 배정해야 함.
- 그러기 위해 필요한 최소 회의실 개수를 구함.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- 필요한 최소 회의실 개수

힌트:
- 시작 시간 기준으로 정렬
- 최소힙으로 "현재 진행 중인 회의실들의 종료시간"을 관리
- 새 회의 시작 시, 가장 빨리 끝나는 회의실이 이미 끝났으면 재사용, 아니면 새 회의실 필요
"""
import heapq

def min_meeting_rooms(meetings):
    # 회의리스트가 비어있으면 0을 리턴한다.
    # 필요한 회의실의 개수가 없게되니까  
    if not meetings:
        return 0

    meetings = sorted(meetings, key=lambda x: x[0])  # 시작 시간 기준 정렬
    heap = []  # 현재 사용 중인 회의실들의 종료시간 (최소힙)

    for start, end in meetings:
        # 힙이 비어있지 않고. 
        # 최소힙에서 가장 작은 값이 start보다 일찍 끝난다면. 
        # 기존회의실을 재사용할 수 있다면, 꺼내서 쓴다. 
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # 가장 먼저 끝나는 회의실이 이미 끝났으면 재사용
        # 새로운 회의실을 사용해야 한다면 - 기존 회의실을 재사용할 수 없으면
        heapq.heappush(heap, end)  # 회의실 사용(재사용했든 새로 열었든 종료시간 등록)

    return len(heap)


# 테스트 케이스
if __name__ == "__main__":
    print("=== 테스트 1: 원래 예제 ===")
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
                 (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    print(f"회의: {meetings1}")
    print(f"필요한 최소 회의실 개수: {min_meeting_rooms(meetings1)}개")
    print()

    print("=== 테스트 2: 하나도 안 겹치는 경우 (방 1개면 충분해야 함) ===")
    meetings2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(f"회의: {meetings2}")
    print(f"필요한 최소 회의실 개수: {min_meeting_rooms(meetings2)}개")
    print()

    print("=== 테스트 3: 전부 다 겹치는 경우 (회의 개수만큼 방이 필요해야 함) ===")
    meetings3 = [(1, 10), (2, 10), (3, 10), (4, 10)]
    print(f"회의: {meetings3}")
    print(f"필요한 최소 회의실 개수: {min_meeting_rooms(meetings3)}개")
    print()

    print("=== 테스트 4: 빈 리스트 ===")
    meetings4 = []
    print(f"회의: {meetings4}")
    print(f"필요한 최소 회의실 개수: {min_meeting_rooms(meetings4)}개")
    print()

    print("=== 테스트 5: 끝나자마자 바로 다음 회의가 시작 (경계값, 재사용 가능해야 함) ===")
    meetings5 = [(1, 5), (5, 10)]
    print(f"회의: {meetings5}")
    print(f"필요한 최소 회의실 개수: {min_meeting_rooms(meetings5)}개")