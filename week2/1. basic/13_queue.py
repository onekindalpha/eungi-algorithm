"""
[큐 - 프린터 대기열]

문제 설명:
- 큐(Queue)를 사용하여 프린터 작업을 순서대로 처리합니다.
- FIFO (First In First Out) 구조를 활용합니다.

입력:
- jobs: 인쇄 작업 리스트 (예: ["문서A", "문서B", "문서C"])

출력:
- 작업이 처리되는 순서

예제:
입력: ["문서A", "문서B", "문서C"]
출력:
처리: 문서A
처리: 문서B
처리: 문서C

힌트:
- 파이썬에서는 리스트로 큐 구현 가능
- append(): 뒤에 추가 (enqueue)
- pop(0): 앞에서 제거 (dequeue)
"""
from collections import deque
def process_print_queue(jobs):
    """
    프린터 작업을 순서대로 처리
    
    Args:
        jobs: 작업 리스트
    
    Returns:
        처리된 작업 리스트
    """
    # 시간 복잡도 : O(N), 공간복잡도 O(N) 
    # TODO: deque로 작업 대기열을 생성한다.  
    queue = deque(jobs)
    # popleft()는 앞에서 제거한다.
    # 따라서 FIFO(First In First Out) 방식으로 처리할 수 있다.
    # 처리한 작업을 순서대로 저장할 빈 리스트 
    processed = []
    
    # TODO: 큐가 빌 때까지 작업을 하나씩 처리한다. 
    while queue:
        # 큐의 맨 앞 작업을 꺼낸다. 
        # deque에서 popleft()는 O(1)이다.  
        job = queue.popleft()    

        # 현재 처리 중인 작업을 출력한다. 
        print(f"처리: {job}")
        # 처리한 작업을 결과 리스트에 추가한다. 
        processed.append(job)
    # 처리된 작업 순서를 반환한다.
    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    jobs1 = ["문서A", "문서B", "문서C"]
    print("=== 프린터 작업 처리 ===")
    result1 = process_print_queue(jobs1)
    print(f"처리 완료: {result1}")
    print()
    
    # 테스트 케이스 2
    jobs2 = ["이메일", "보고서", "사진", "계약서"]
    print("=== 프린터 작업 처리 ===")
    result2 = process_print_queue(jobs2)
    print(f"처리 완료: {result2}")


