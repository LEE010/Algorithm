'''
로프
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	192 MB	11117	5002	4189	45.791%

문제

N(1≤N≤100,000)개의 로프가 있다.
이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.

각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때,
이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.

모든 로프를 사용해야 할 필요는 없으며,
임의로 몇 개의 로프를 골라서 사용해도 된다. 단, 각각의 로프는 한 개씩만 존재한다.

입력
첫째 줄에 정수 N이 주어진다.
다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
이 값은 10,000을 넘지 않는 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1
2
10
15
예제 출력 1
20
출처
빠진 조건을 찾은 사람: bububu111
데이터를 추가한 사람: kdk8361
알고리즘 분류
보기

메모
'''
'''
3
1
10
15

3
10
15
100

'''
# from sys import stdin
# input = stdin.readline
#
# N = int(input())
# ropes = [int(input()) for _ in range(N)]
# res = 0
#
# ropes.sort()
# for n in range(N):
#     res = max(ropes[n]*(N-n),res)
# print(res)

from sys import stdin
input = stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
res = []

ropes.sort()
for n in range(N):
    res.append(ropes[n]*(N-n))
print(max(res))
