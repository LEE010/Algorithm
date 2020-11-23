'''
부분수열의 합 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	29477	13603	8611	44.320%
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
출처
문제를 만든 사람: author5
문제의 오타를 찾은 사람: eric00513 jh05013
데이터를 추가한 사람: rdd6584
잘못된 데이터를 찾은 사람: tncks0121
'''
from sys import stdin
from itertools import combinations


def readline(): return map(int, stdin.readline().split())


N, S = readline()
nums = list( readline())
count = 0

for i in range(1, len(nums)+1):
    for c in combinations(nums, i):
        if sum(c) == S:
            count += 1

print(count)
