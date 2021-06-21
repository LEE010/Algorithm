'''
버블 소트
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	12870	3225	2147	28.551%
문제
N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.

버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.

입력
첫째 줄에 N(1≤N≤500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0≤|A[i]|≤1,000,000,000의 범위에 들어있다.

출력
첫째 줄에 Swap 횟수를 출력한다

예제 입력 1 
3
3 2 1
예제 출력 1 
3
출처
데이터를 추가한 사람: akaishuichi
'''
from sys import stdin

readline = stdin.readline


def update(tree, idx):
    global N
    while idx <= N:
        tree[idx] += 1
        idx += (idx & -idx)


def interval_sum(tree, idx):
    res = 0

    while idx > 0:
        res += tree[idx]
        idx -= (idx & -idx)

    return res


def main():
    global N
    N = int(readline())
    arr = sorted(enumerate(map(int, readline().split()), 1), key=lambda x: (x[1], x[0]), reverse=True)
    tree = [0] * (N + 1)
    res = 0

    for idx, _ in arr:
        res += interval_sum(tree, idx-1)
        update(tree, idx)

    print(res)


if __name__ == '__main__':
    main()
