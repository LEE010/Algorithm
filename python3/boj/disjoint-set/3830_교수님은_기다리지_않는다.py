'''
교수님은 기다리지 않는다 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	11632	3299	2192	27.099%
문제
상근이는 매일 아침 실험실로 출근해서 샘플의 무게를 재는 일을 하고 있다. 상근이는 두 샘플을 고른 뒤, 저울을 이용해서 무게의 차이를 잰다.

교수님의 마음에 들기 위해서 매일 아침부터 무게를 재고 있지만, 가끔 교수님이 실험실에 들어와서 상근이에게 어떤 두 샘플의 무게의 차이를 물어보기도 한다. 이때, 상근이는 지금까지 잰 결과를 바탕으로 대답을 할 수도 있고, 못 할 수도 있다.

상근이는 결과를 출근한 첫 날부터 공책에 적어 두었다. 하지만, 엄청난 양의 무게가 적혀있기 때문에, 교수님의 질문에 재빨리 대답할 수가 없었다. 이런 상근이를 위해서 프로그램을 만들려고 한다.

상근이가 실험실에서 한 일이 순서대로 주어진다. 어떤 두 샘플의 무게의 차이를 구할 수 있는지 없는지를 알아내는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스의 첫째 줄에는 샘플의 종류의 개수 N (2 ≤ N ≤ 100,000)과 상근이가 실험실에서 한 일의 수 M (1 ≤ M ≤ 100,000)이 주어진다. 샘플은 1번부터 N번까지 번호가 매겨져 있다. 다음 M개 줄에는 상근이가 실험실에서 한 일이 주어진다.

상근이가 무게를 쟀다면, ! a b w와 같은 형식으로 주어진다. 이 뜻은 b가 a보다 w그램 무겁다는 뜻이다. (a ≠ b) w는 1,000,000을 넘지 않는 음이 아닌 정수이다. 모든 측정은 정확하고, 일관성을 유지한다.

교수님의 질문은 ? a b와 같은 형식으로 주어진다. 이 뜻은 b가 a보다 얼마나 무거운지를 출력하라는 뜻이다.

마지막 줄에는 0이 두 개 주어진다.

출력
교수님의 질문 (? a b)이 입력으로 들어올 때 마다, 지금까지 측정한 결과를 바탕으로 a와 b의 무게 차이를 계산할 수 있다면, b가 a보다 얼마나 무거운지를 출력한다. 무게의 차이의 절댓값이 1,000,000을 넘지 않는다. 만약, 측정한 결과를 바탕으로 무게의 차이를 계산할 수 없다면, "UNKNOWN"을 출력한다.

예제 입력 1
2 2
! 1 2 1
? 1 2
2 2
! 1 2 1
? 2 1
4 7
! 1 2 100
? 2 3
! 2 3 100
? 2 3
? 1 3
! 4 3 150
? 4 1
0 0
예제 출력 1
1
-1
UNKNOWN
100
200
-50
출처
ICPC > Regionals > Asia Pacific > Japan > Asia Regional Contest 2012 in Tokyo F번

문제를 번역한 사람: baekjoon
'''

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
readline = stdin.readline

WORK = '!'
QUESTION = '?'
UNKNOWN = 'UNKNOWN'


def find(parent, weights, n):
    if parent[n] != n:
        root = find(parent, weights, parent[n])
        weights[n] += weights[parent[n]]
        parent[n] = root
    return parent[n]


def union(parent, weights, a, b, w):
    root_a, root_b = find(parent, weights, a), find(parent, weights, b)

    if root_a == root_b:
        return

    parent[root_b] = root_a
    weights[root_b] = weights[a] - weights[b] + w


def measure(parent, weights, a, b, w):
    union(parent, weights, a, b, w)


def summary(parent, weights, a, b):
    if find(parent, weights, a) == find(parent, weights, b):
        return weights[b] - weights[a]
    else:
        return UNKNOWN


if __name__ == '__main__':
    while True:
        N, M = map(int, readline().split())

        if N == 0 and M == 0:
            break

        parent = [i for i in range(N + 1)]
        weights = [0 for _ in range(N + 1)]

        for _ in range(M):
            cmd, *args = readline().split()
            args = map(int, args)
            if cmd == WORK:
                measure(parent, weights, *args)
            elif cmd == QUESTION:
                print(summary(parent, weights, *args))
