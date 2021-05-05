N, M = map(int, input().split())

result = 0 #항상 받아야하는 값에서

for i in range(N):
    data = list(map(int, input().split())) #행마다 데이터를 삽입하고 싶을 때
    min_value = min(data) #데이터 줄마다의 최소 값을 산출해주고
    result = max(result, min_value) #Max 함수를 사용할때에는 default 값을 지정해줘야 한다 객체가 비어있어서는 실행이 안됨.

print(result)

