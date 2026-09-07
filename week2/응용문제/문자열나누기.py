# 여러 문자열로 분해하는 과정
def solution(s):
    # 분회한 횟수를 알기위해서 anwer라고 함
    # 어쩔수없이 인덱스 번호를 따로 지정함. i는 1에서 시작하고. 
    # 분리한 문자열을 빼고 남은 부분에 대해서 이과정을 반복함. 
    answer = 0
    i = 0
    # 아직 읽지 않은 글자가 있는 동안 반복함. 
    while i < len(s):  
      # 반복할 횟수를 정함 
      x = s[i]
      x_count = 0
      not_x_count = 0
      # 아직 읽지 않은 글자가 있는 동안 반복함.
      while i < len(s):
        if s[i] == x:
        # x가 처음 나온 숫자와 같다면. 
          x_count += 1
        else:
        # x가 아닌 다른 문자열이 나온다면
          not_x_count +=1
        i += 1
        # 처음으로 두 횟수가 같아지는 순간 멈춤
        if x_count == not_x_count:
          break 
      # while 문이 끝나기 전에 분해한 횟수를 더함. 
      answer += 1
      # 지금까지 읽은 문자열을 분리함. 총 더한 i인덱스 다음부터 보면 되는거고. 
        # 분리한 문자열을 빼고 남은 부분에 대해 이 과정을 반복해야 함.  
        #분해한 횟수를 구해야 하는거니까. 분해한 횟수를 하나 더함. 
    # 만약 두 횟수가 다른 상태에서 더이상 읽을 글자가 없다면
    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))