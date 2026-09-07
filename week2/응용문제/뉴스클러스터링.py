# 자카드 유사도 J(A, B) 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# J(A, B) = len({A and B}) / len({A or B})
# if A and B == 0 일 경우 J(A, B) =1로 정의함
# 영문자로 들어온 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수문자는 그 글자 쌍 버림
# 각 원소가 몇번 나오는지 세는 도구를 추가함
from collections import Counter

# 두글자씩 쪼개서 리스트에 넣을 때 영문자 쌍만 넣도록 함. 
# 두글자를 .isalpha()로 동시에 검사를 해서 넣음.  
def to_list(new_str):
  # 전체길이는 
    new_str_list = []
    for i in range(len(new_str)-1):
      if new_str[i].isalpha() and new_str[i+1].isalpha():
        # 리스트에는 원소두개를 동시에 못 넣으니까, pair로 해서 넣음
        # 동시에 소문자로 반환함. 
        pair = new_str[i:i+2].lower()
      # 페어를 구했으면 새로운 리스트로 반환함. 
        new_str_list.append(pair)
    return new_str_list

# 두글자씩 끊어서 다중집합의 원소로 만듦. 
# 만약에 한글자가 남으면 어떻게 하지 .
def solution(str1, str2):
    answer = 0
    new_str_list1 = to_list(str1)
    new_str_list2 = to_list(str2)
  # 공집합이면 J = 1로 정의함. 
    if len(new_str_list1) == 0 and len(new_str_list2) == 0 :
      answer = 1
  # 교집합과 합집합을 구하기 전 Counter를 통해 각 원소가 몇 번 나오는지 세는 도구를 구함.  
    a = Counter(new_str_list1)
    b = Counter(new_str_list2)
  # 교집합과 합집합을 구함
    intersection_count = sum((a & b).values())
    union_count = sum((a|b).values())
  # 만약 합집합이 0인경우 유사도는 1임. 
    if union_count == 0:
    # 자카도 유사도에 65536을 곱하는 것이니까
      return 65536
    answer = int(intersection_count / union_count * 65536)
    return answer

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))