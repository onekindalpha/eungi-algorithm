from collections import Counter
my_list = [3,3,3,2,2,2]
my_dict = dict(Counter(my_list))
# 한번 키만 모아볼까
keys = list(my_dict.keys())
# 한번 값만 모아볼까
values = list(my_dict.values())
print(my_dict)
# 키들만 모으기 (여기서는 아마 포켓몬 종류의 수겠지) - 근데 왜 선택할 수 있는 포켓몬 종류 번호의 최댓값을 구하는 것이지. 
print(len(keys))
# 값들만 모으기 (여기서는 아마 포켓몬 마리의 수겠지)
print(sum(values))
# 만약에 포켓몬 마리의 수를 모은다고 하면 n //2를 해서 이것을 모을 수 있는지를 보기. 