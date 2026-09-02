"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 해시 테이블로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)

힌트:
- 딕셔너리 사용
- 평균: sum(scores.values()) / len(scores)
- 최고점: max(scores, key=scores.get)
"""

def manage_grades(students):
    """
    학생 성적 관리 시스템
    
    Args:
        students: {이름: 점수} 딕셔너리
    
    Returns:
        평균, 최고점 학생 이름, 최고점
    """
    # TODO: 평균 점수 계산
    # students.values()로 모든 학생의 점수(value)만 가져온다. 
    # sum()으로 모든 점수의 합을 구하고, len(studdents)로 학생 수를 구해 평균을 계산한다. 
    average = sum(students.values()) / len(students)
    # TODO: 최고 점수 학생 찾기 
    # 각 학생 이름(key)에 students.get()을 적용해 점수(value)를 비교한다.  
    # 따라서 가장 높은 점수를 가진 학생의 이름(key)이 반환된다. 
    # key = students.get 때문에 비교할 때만 각각 점수를 봄. 
    top_student = max(students, key=students.get)
    # 최고 점수 학생의 이름으로 딕셔너리에서 점수를 가져온다. 
    top_score = students[top_student]
    # 평균, 최고점 학생 이름, 최고점수를 반환한다. 
    return average, top_student, top_score

def find_student_score(students, name):
    """
    특정 학생의 점수 조회
    
    Args:
        students: 학생 딕셔너리
        name: 찾을 학생 이름
    
    Returns:
        점수 (없으면 None)
    """
    # TODO: students에서 name 찾기  
    # students에서 name을 key로 찾아 해당 점수를 가져온다. 
    # 학생이 존재하면 점수를 반환하고, 없으면 None을 반환한다. 
    return students.get(name, None)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {top_name} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")


