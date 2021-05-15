'''
구간 곱 구하기 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9179	3218	2281	33.265%
문제
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다. 만약에 1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
예제 출력 1 
240
48
예제 입력 2 
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
예제 출력 2 
0
240
출처
문제의 오타를 찾은 사람: adh0463, nosiar, yj9404
문제를 만든 사람: baekjoon
빠진 조건을 찾은 사람: codenstory
'''
from sys import stdin

readline = stdin.readline

RES_MAX = 1000000007


def update(idx, val):
    while idx <= N:
        tree[idx] = (tree[idx] * val) % RES_MAX
        idx += (idx & -idx)


def prefix_mul(idx):
    res = 1

    while idx > 0:
        res = (res * tree[idx]) % RES_MAX
        idx -= (idx & -idx)

    return res


def interval_mul(start, end):
    return (prefix_mul(end) // prefix_mul(start-1)) % RES_MAX


N, M, K = map(int, readline().split())

arr = [1] * (N + 1)
tree = [1] * (N + 1)

for i in range(1, N + 1):
    val = int(readline())
    arr[i] = val
    update(i, val)

for _ in range(M + K):
    mode, a, b = map(int, readline().split())

    # if mode == 1:
    #     update(a, b//a)
    #     arr[a] = b
    # else:
    #     print(interval_mul(a, b))
    