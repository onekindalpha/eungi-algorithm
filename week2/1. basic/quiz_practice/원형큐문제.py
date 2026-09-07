class CircularQueue:

    def __init__(self, capacity=10):
        # 큐에 저장할 수 있는 최대 개수
        self.capacity = capacity

        # 실제 데이터를 저장할 배열
        # 처음에는 모든 칸이 비어 있음
        self.arr = [None] * capacity

        # 데이터를 꺼낼 위치
        self.front = 0

        # 데이터를 넣을 위치
        self.rear = 0

        # 현재 큐에 들어있는 데이터 개수
        self.count = 0

    def enqueue(self, value):

        # 현재 데이터 개수가 최대 용량과 같으면
        # 더 이상 데이터를 넣을 수 없음
        if self.count == self.capacity:
            print("큐가 가득 찼습니다")
            return

        # rear가 가리키는 위치에 새로운 데이터 저장
        self.arr[self.rear] = value

        # rear를 다음 위치로 이동
        # % capacity를 사용하기 때문에
        # 배열의 마지막에 도달하면 다시 0번으로 돌아감
        self.rear = (self.rear + 1) % self.capacity

        # 큐에 들어있는 데이터 개수 증가
        self.count += 1

    def dequeue(self):

        # 데이터가 하나도 없으면 꺼낼 수 없음
        if self.count == 0:
            print("큐가 비어 있습니다")
            return None

        # front가 가리키는 데이터를 꺼냄
        value = self.arr[self.front]

        # 꺼낸 자리를 비움
        self.arr[self.front] = None

        # front를 다음 위치로 이동
        # 마지막 위치 다음에는 다시 0번으로 돌아감
        self.front = (self.front + 1) % self.capacity

        # 큐에 들어있는 데이터 개수 감소
        self.count -= 1

        # 꺼낸 데이터를 반환
        return value