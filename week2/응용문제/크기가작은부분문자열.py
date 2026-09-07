# 숫자로 이루어진 문자열 t와 p가 주어질 때, 
# t에서 p와 길이가 같은 부분 문자열 중에서
# 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 
# 같은 것이 나오는 횟수를 return

def solution(t, p):
    n = len(p)
    count = 0
    # 1. i = 0에서 시작하고 그냥 하나씩 더하면 될듯
    # 몇 번 반복할지를 알아야 하는데. 
    for i in range(len(t)):
      # p보다 작거나 같은 수
      # i에서 시작해서 n길이 만큼 더하고 그 직전까지 문자열에 포함하면
      if len(t[i:i+n]) < n:
        break
      if int(t[i:i+n]) <= int(p):
        #print(int(t[i:i+n]))
        count += 1
    # 2. 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution
    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))
