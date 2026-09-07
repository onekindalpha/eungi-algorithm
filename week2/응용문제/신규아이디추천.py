import re

# 2단계 - 맞지 않는 규칙의 문자들 제거하기
def is_valid(new_id):
    removed = ""
    for char in new_id:
        # 아이디로 사용할 수 잇는 것들 검증하기. 
        if char.isalpha() or char.isdigit() or char == "-" or char == "_" or char == ".":
          removed += char
    return removed

# 3단계 - 마침표가 연속으로 등장하면 치환
def is_continue(removed):
  changed = ""
  # 총 길이를 알아야 함. 
  # 마침표가 2개 이상({2, }) 연속되면 마침표 1개 (".")로 치환
  changed = re.sub(r'\.{2,}', '.', removed)
  return changed
# 여기까지는 통과

# 4단계 - 마침표가 처음이나 끝에 위치한다면 제거함
def is_end_remove(changed):
  # 마침표가 처음이나 끝에 위치한다면 제거함. 
  # 만약 end가 처음이나 끝에 위치한다면 제거를 함. 
  end_removed = changed.strip(".")
  return end_removed

# 빈 문자열일 경우
def solution(new_id):
    # 1단계
    lowered = new_id.lower()
    # 2단계 - 알파벳, 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    removed = is_valid(lowered)
    # 3단계 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환함
    changed = is_continue(removed)
    # 4단계 - 
    end_removed = is_end_remove(changed)
    # 5단계 빈 문자열이라면 끝에 "a"를 대입함
    if end_removed == "":
      end_removed += "a"
    # 6단계 - 길이가 16자 이상이면, 첫 15개 문자를 제외한 나머지 문자들을 모두 제거함. 
    if len(end_removed) >= 16:
      # 첫 15개 문자만 남기고 
      end_removed = end_removed[0:15]
      # 만약 제거후 마침표가 끝에 위치한다면 끝에 위치한 마침표 문자를 제거함.  
      if end_removed[-1] == ".":
      # 맨 뒤 원소를 제거하는 방법
        end_removed = end_removed.rstrip(".")
    # 7단계 - 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙임. 
    if len(end_removed) <= 2:
      # 여기서 마지막 문자를 정해줘야하고. 
      last = end_removed[-1]
      # 총 길이가 3이 될때까지 반복해서 끝에 붙임. 
      while len(end_removed) != 3:
        # 3번 붙일때까지 남은 횟수 = 반복할 횟수
        more = 3 - (len(end_removed))
        for _ in range(more):
          # 여기에 또 for문을 붙여야 하나?
          end_removed += last
    return end_removed

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
