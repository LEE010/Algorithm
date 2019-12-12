'''
외판원 순회

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	14536	3305	1939	26.284%

문제

외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.

여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다)
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐
다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
단, 한 번 갔던 도시로는 다시 갈 수 없다.
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
이런 여행 경로는 여러 가지가 있을 수 있는데,
가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
비용은 대칭적이지 않다.
즉, W[i][j] 는 W[j][i]와 다를 수 있다.

모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며
이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때,
가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16)
다음 N개의 줄에는 비용 행렬이 주어진다.
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

예제 입력 1
4
0 10 15 20
5  0  9 10
6 13  0 12
8  8  9  0

4
0 1 2 3
2 0 3 0
3 0 0 0
1 2 3 0

4
0 1 100 100
0 0 3 0
0 200 0 400
1 1 1 0

4
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

예제 출력 1
35

11

405
출처
데이터를 추가한 사람: coke sys7961
빠진 조건을 찾은 사람: kcm1700
문제의 오타를 찾은 사람: tjrwodnjs999
알고리즘 분류
보기

메모
메모 작성하기
'''
# N = 20
# sum([2**n for n in range(N)])
# list(enumerate([1,2,3],1))
# [min(dp[n][bm]+cities[n][i])]
# MAX = 2**16-1
# bin(MAX&1)
15&~(2**3)
1 << 0
from sys import stdin

def dp(bm,cur):
    try:
        return cache[cur][bm]
    except KeyError:

        if bm == MAX and cities[cur][0]:
            return cities[cur][0]

        next = [i for i in range(N) if bm&(2**i) == 0 and cities[cur][i]]

        if not next:
            return float('inf')

        cache[cur][bm] = min(map(lambda n: cities[cur][n] + dp(bm|(2**n),n),next))

        return cache[cur][bm]

N = int(stdin.readline())
MAX = 2**N-1
cities = [list(map(int,stdin.readline().split())) for _ in range(N)]
cache = [{} for _ in range(N)]
print(dp(1,0))
