'''
쉬운 계단 수
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	37886	11435	8280	28.450%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1
1
예제 출력 1
9
예제 입력 2
2
예제 출력 2
17
출처
문제를 만든 사람: baekjoon
'''
from sys import setrecursionlimit
setrecursionlimit(1000000000)
def sn(n):
    try:
        return nums[n]
    except KeyError:
        before_num, num_dict = sn(n-1)
        temp = {num:num_dict[num-1]+num_dict[num+1] for num in range(1,9)}
        temp[0] = num_dict[1]
        temp[9] = num_dict[8]
        nums[n] = (before_num*2 -(num_dict[0]+num_dict[9]),temp)
        return nums[n]
n = int(input())
nums = {1:(9,{0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1})}
print(sn(n)[0]%1000000000)
