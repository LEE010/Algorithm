'''
차이를 최대로 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	12985	7999	6146	62.288%
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

예제 입력 1 
6
20 1 15 8 4 10
예제 출력 1 
62
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기
'''

from sys import stdin
from itertools import permutations

readline = stdin.readline

N = int(readline())
perms = permutations(map(int, readline().split()), N)
res = 0

for perm in perms:
    nums = list(perm)
    total = 0
    for i in range(1, N):
        total += abs(nums[i] - nums[i-1])
    res = max(res, total)

print(res)
