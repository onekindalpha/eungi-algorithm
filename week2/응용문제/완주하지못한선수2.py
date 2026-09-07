def solution(participant, completion):
  p_dict = {}
  # 1. 참가자 이름과 등장 횟수를 딕셔너리에 저장
  for p in participant:
    # (key, 기본값) 형태로 key를 찾되, 만약 그 key가 없으면 에러를 내는 대신 우리가 지정한 기본값(0)를 던져주는 고마운 기능임
    p_dict[p] = p_dict.get(p, 0) + 1
  # 2. 완주자 이름을 돌면서 횟수를 1씩 차감
  for c in completion:
    p_dict[c] -= 1
  # 3. 밸류가 1인 (차감되지 않고 남은) 사람을 찾아서 반환
  for key, val in p_dict.items():
    if val == 1:
      return key