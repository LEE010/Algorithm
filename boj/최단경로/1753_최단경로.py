'''
최단경로

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	42604	10083	4911	23.277%

문제

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의
최단 경로를 구하는 프로그램을 작성하시오.

단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다.
(1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.

둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.

시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

예제 입력 1
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

5 7
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
4 1 1

예제 출력 1
0
2
3
7
INF

출처
빠진 조건을 찾은 사람: algoshipda
데이터를 추가한 사람: august14 djm03178
문제를 만든 사람: author5
알고리즘 분류
보기

메모
메모 작성하기
'''
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

V, E = map(int,input().split())
K = int(input())
D = [ float('inf') for _ in range(V)]
D[K-1] = 0

graph = [list() for _ in range(V)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u-1].append((w,v-1))

q = [(0,K-1)]

while q:
    w,pos = heappop(q)

    for nw,p in graph[pos]:
        if D[p] > w+nw:
            D[p] = w+nw
            heappush(q,(nw+w,p))

for i in range(V):
    print('INF' if D[i] == float('inf') else D[i])
