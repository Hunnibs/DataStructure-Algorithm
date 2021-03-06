'''
좀비 n명이 직선으로 된 산 길에 일렬로 서 있다. 길의 양 끝 지점은 깊이를 알 수 없는 절벽으로 이어져 있다.
각 좀비에 대해 초기 위치와 처음 이동 방향 정보가 주어진다. 
모든 좀비는 초기 위치에서 처음에 움질일 방향으로 1거리단위/1초로 이동. 도중에 만나면 각자 움직이는 방향과 반대 방향으로 돌아서 계속 움직인다. 바꾸기 위한 시간은 0이라고 가정한다.
단, 좀비가 같이 떨어진다면 아이디가 더 작은 좀비가 더 먼저 떨어진다.

입력:
첫 줄에 n, L, K 세 정수가 주어진다.(n은 좀비 수, L은 길의 길이, k는 1과 n사이의 자연수)
다음 n개의 줄에는 각 좀비의 초기 위치와 좀비의 아이디가 주어진다.

출력:
k번째로 떨어지는 좀비의 아이디를 출력(아이디가 음수라면 음수 형식으로 양수라면 부호 없이 출력)
'''

'''
왼쪽부터 선형탐색을 진행했을 때 좀비 중 가장 먼저 왼쪽으로 진행하는 음수 인덱스 값을 가진 좀비의 위치 값은 어떤 경우에든 왼쪽으로 가장 먼저 떨어지는 좀비의 총 턴 수와 같다. 이는 가장 먼저 오른쪽으로 진행하는 양수 인덱스 값을 가진 좀비의 위치 값도 동일하다. 오른쪽은 끝이 L이므로 현재 좀비의 위치에서 끝까지의 거리 즉 L-(현재 좀비 위치)를 하면 오른쪽으로 가장 먼저 떨어지는 좀비의 총 턴 수와 같다. 이는 좀비가 부딪혀서 진행방향을 바꾸고 떨어지기까지의 시간을 측정하는 방식을 생각하면 쉽다. 예를 들어 가장 왼쪽 좀비가 오른쪽으로 이동하는 경우 다시 왼쪽 방향으로 진행방향을 바꾸기 위해서는 왼쪽 방향으로 이동하는 좀비를 만나야한다. 쉽게 말하면 시간으로 치면 오른쪽 좀비가 계속해서 왼쪽으로 걷는다는 가정을 하면 그 시간이 왼쪽 좀비가 오른쪽에서 오는 좀비를 만나 진행방향을 바꾸고 떨어지기까지의 시간과 동일하다는 것이다.
위와 같은 원리를 이용하여 선형탐색을 하면 각 좀비들이 어느 방향으로 떨어지고 떨어지는데 얼마나 많은 시간이 소요되는지를 한 번에 알 수가 있다.
예를 들어 문제 1은 leftFall = [19, 22, 24], rightFall = [25, 22, 5]로 만약 extend()시에는 각 인덱스에 해당하는 값이 떨어지기까지의 총 턴 수를 나타낸다. 
이 후에는 각 케이스 별 분류를 통해 좀비들을 순서대로 떨어뜨려 K번째 떨어지는 좀비를 찾아줘서 값을 출력한다. 
시간복잡도 계산은 떨어지는 좀비 들의 턴 수를 구하는데 N의 시간 K번째로 떨어지는 좀비의 시간을 구하는데 K시간이 걸려 총 N+K만큼 걸린다. 이를 Big-O 표기법으로 표기하면 O(n) 시간만큼 걸린다. 
'''

def zombieFall(zombie, n, L):  # 왼쪽으로 떨어지는 좀비와 오른쪽으로 떨어지는 좀비 턴 값을 저장하는 리스트 생성
	leftFall, rightFall = [], []
	
	for i in range(0,n):
		if zombie[i][1] > 0:  # 좀비 번호가 양수일 경우 오른쪽으로 떨어진다. 
			rightFall.append(L- zombie[i][0])  # 이 때 오른쪽 끝 L에서 현재 좀비 위치 값을 빼주면 총 턴 수가 나옴
		else:
			leftFall.append(zombie[i][0])  # 현재 좀비 위치 값이 총 턴 수
			
	return leftFall, rightFall

# 입력파트
n, L, K = map(int, input().split())
zombie = [list(map(int, input().split())) for _ in range(n)]  # 입력을 이차원 배열로 받아주었음 [i][0]에는 위치 정보, [i][1] 좀비 번호

left, right = zombieFall(zombie, n, L)

# K번째 값을 찾아내기 위한 변수 생성
lIndex, rIndex, start, end = 0, len(right)-1, 0, n-1

while K > 0:
	if rIndex < 0:  # 오른쪽으로 떨어지는 좀비가 없는 경우
		result = zombie[start][1]
		start += 1
	elif lIndex == len(left):  # 왼쪽으로 떨어지는 좀비가 없는 경우
		result = zombie[end][1]
		end -= 1
	else:
		if left[lIndex] < right[rIndex]:  # 왼쪽이 먼저 떨어지는 경우
			result = zombie[start][1]
			start += 1
			lIndex += 1
		elif left[lIndex] > right[rIndex]:  # 오른쪽이 먼저 떨어지는 경우
			result = zombie[end][1]
			end -= 1
			rIndex -= 1
		else:  # 같이 떨어지는 경우-값이 더 작은 쪽이 먼저 떨어지는 케이스 구현
			if zombie[start][1] < zombie[end][1]:
				result = zombie[start][1]
				start += 1
				lIndex += 1
			else:
				result = zombie[end][1]
				end -= 1
				rIndex -= 1
			
	K -= 1
	
print(result)