'''
숨바꼭질 4 스페셜 저지분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	13981	4880	3392	32.954%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
출처
문제를 만든 사람: baekjoon
비슷한 문제
1697번. 숨바꼭질
12851번. 숨바꼭질 2
13549번. 숨바꼭질 3
'''
from collections import deque

POS_MIN = 0
POS_MAX = 1000000


def get_path(D, s, e):
    path = deque()
    pos = e

    while D[pos] != s:
        path.appendleft(pos)
        pos = D[pos]

    path.appendleft(pos)
    path.appendleft(s)

    return path


def search(n, k):
    visited = [-1 for _ in range(POS_MAX+1)]
    time = 0

    q = deque([n, -1])

    while True:
        cur = q.popleft()
        
        if cur == -1:
            time += 1
            q.append(-1)
            continue

        if cur == k:
            path = get_path(visited, n, k)
            return time, path

        if cur < POS_MAX and visited[cur+1] == -1:
            visited[cur+1] = cur
            q.append(cur+1)

        if cur > POS_MIN and visited[cur-1] == -1:
            visited[cur-1] = cur
            q.append(cur-1)

        if cur*2 <= POS_MAX and visited[cur*2] == -1:
            visited[cur*2] = cur
            q.append(cur*2)


if __name__ == '__main__':
    n, k = map(int, input().split(' '))

    if n >= k:
        print(n-k)
        print(*range(n, k-1, -1))
    else:
        time, path = search(n, k)
        print(time)
        print(*path)
