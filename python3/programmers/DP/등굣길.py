'''
계속되는 폭우로 일부 지역이 물에 잠겼습니다.
물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

image0.png

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래,
즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어질 때,
학교에서 집까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록
solution 함수를 작성해주세요.

제한사항
격자의 크기 M, N은 1 이상 100 이하인 자연수입니다.
물에 잠긴 지역은 0개 이상 10개 이하입니다.
집과 학교는 물에 잠기지 않았습니다.
입출력 예
m	n	puddles	return
4	3	[[2, 2]]	4
입출력 예 설명
image1.png
'''
m = 4
n = 3
puddles = [[2,2]]

def solution(m, n, puddles):
    global maps
    maps = [[-1]*(m+2)]+[[-1]+[0]*(m)+[-1] for _ in range(n)]+[[-1]*(m+2)]
    maps[1][1] = 1
    for x,y in puddles:
        maps[x][y] = -1

    for x in range(1,n+1):
        for y in range(1,m+1):
            if maps[x][y] == -1:
                continue
            for wx,wy in ((0,1),(1,0)):
                if maps[x-wx][y-wy] != -1:
                    maps[x][y] += maps[x-wx][y-wy]

    return maps[n][m]%1000000007

solution(m,n,puddles)
