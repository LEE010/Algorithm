'''
문제 설명
서울에서 경산까지 여행을 하면서 모금 활동을 하려 합니다.
여행은 서울에서 출발해 다른 도시를 정해진 순서대로 딱 한 번 방문한 후 경산으로 도착할 예정입니다.
도시를 이동할 때에는 도보 혹은 자전거를 이용합니다.
이때 도보 이동에 걸리는 시간, 도보 이동 시 얻을 모금액,
자전거 이동에 걸리는 시간, 자전거 이동 시 얻을 모금액이 정해져 있습니다.
K시간 이내로 여행할 때 모을 수 있는 최대 모금액을 알아보려 합니다.

예를 들어 여행 루트가 다음과 같고 K = 1,650 일 때

ㅅㅡㅋㅡㄹㅣㄴㅅㅑㅅ 2018-08-16 ㅇㅗㅈㅓㄴ 11.08.33.png

1, 2번 구간은 도보로, 3번 구간은 자전거로 이동해 모금액을 660으로 하는 것이 가장 좋은 방법입니다.
이때, 1,600시간이 소요됩니다.

solution 함수의 매개변수로 각 도시를 이동할 때 이동 수단별로 걸리는 시간과
모금액을 담은 2차원 배열 travel과 제한시간 K가 주어집니다.
제한시간 안에 서울에서 경산까지 여행을 하며 모을 수 있는 최대 모금액을 return 하도록
solution 함수를 작성하세요.

제한사항
travel 배열의 각 행은 순서대로
[도보 이동에 걸리는 시간, 도보 이동 시 얻을 모금액,
자전거 이동에 걸리는 시간, 자전거 이동 시 얻을 모금액]입니다.
travel 배열 행의 개수는 3 이상 100 이하인 정수입니다.
travel 배열에서 시간을 나타내는 숫자(각 행의 첫 번째, 세 번째 숫자)는 10,000 이하의 자연수,
모금액을 나타내는 숫자(각 행의 두 번째, 네 번째 숫자)는 1,000,000 이하의 자연수입니다.
K는 0보다 크고 100,000보다 작거나 같은 자연수입니다.
입출력 예
K	travel	return
1650	[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]	660
3000	[[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]	5900
입출력 예 설명
입출력 예#1
앞서 설명한 예와 같습니다.

입출력 예#2
1, 4번 구간은 도보로 이동하고 2, 3번 구간은 자전거로 이동하여 모금액을 5,900원으로 하는 것이 가장 좋은 방법입니다. 이때 걸리는 시간은 3,000시간입니다.
'''
True if {} else False
travel = [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]
#
# def solution(K, travel):
#     answer = 0
#     N = len(travel)
#     cache = []
#     for i in range(1,N):
#         awt, awc, abt, abc = travel[i-1]
#         bwt, bwc, bbt, bbc = travel[i]
#         cache.append([
#             [awt+bwt,awc+bwc],
#             [abt+bbt,abc+bbc],
#             [abt+bwt,abc+bwc],
#             [awt+bbt,awc+bbc]])
#
#     for i in range(1,len(cache)):
#         for j in range(4):
#             for k in range(4):
#                 (prev_time, prev_cost), (next_time, next_cost) = cache[i-1][j],cache[i][k]
#                 if prev_time + next_time <= K:
#                     cost = prev_cost + next_cost
#                     if cost > answer:
#                         answer = cost
#     print(answer)
#     return cache
#
# solution(1650,[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]])
# solution(3000,[[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]])
# ###################################################################################
# def solution(K, travel):
#     def dp(path):
#         try:
#             return cache[path]
#         except KeyError:
#             temp = travel[len(path)-1][:2] if path[-1] == 'w' else travel[len(path)-1][2:]
#             cache[path] = list(map(sum,zip(dp(path[:-1]),temp)))
#         return cache[path]
#
#     answer = 0
#     N = len(travel)
#     cache = {'w':travel[0][:2],'b':travel[0][2:]}
#
#     paths = ['w','b']
#     for _ in range(N-1):
#         temp = []
#         for path in paths:
#             for type in ('w','b'):
#                 next = path + type
#                 res = dp(next)
#                 if res[0] <= K:
#                     answer = max(res[1],answer)
#                     temp.append(next)
#         paths = temp
#     return answer
#
# solution(1650,[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]])
# solution(3000,[[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]])
################################################################################
def solution(K, travel):
    N = len(travel)
    cache = [0 for _ in range(K+1)]

    for walk_time, walk_cost, bike_time, bike_cost in travel:
        temp = [0 for _ in range(K+1)]

        for time in range(K+1):
            walk = cache[time-walk_time] + walk_cost if time >= walk_time and cache[time-walk_time] != -1 else -1
            bike = cache[time-bike_time] + bike_cost if time >= bike_time and cache[time-bike_time] != -1 else -1
            temp[time] = max(walk,bike)
        cache = temp

    return cache[-1]

solution(1650,[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]])
solution(3000,[[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]])
