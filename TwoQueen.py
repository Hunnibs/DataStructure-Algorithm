'''
n x n 체스 보드에 2개의 여왕을 놓고 싶다. 두 여왕은 같은 가로선, 세로선, 대각선 상에 놓이면 안된다.
'''

'''
배열로 치면 [0,0] 부터 [0,n],[n,0]까지만을 계산해주고 다음 행열은 재귀함수로 풀어준다. 계산식은 다음과 같다.
행 혹은 열에 칸 개수 * (총 칸의 개수 - 2번째 퀸이 위치한 칸의 개수)
(퀸의 위치는 행열당 한 칸을 기준으로 잡고 계산한다. 이때, 어떤 칸에서든 대각선과 행,열에 해당하는 2번째 퀸의 개수는 같다.)
식: 
row = n* (n*n) -(2n-1+n-1) = n * (n^2-3n+2) 
column = (n-1) * [{n*(n-1)} - (2n-2+n-2)] = (n-1) * (n^2-4n+4) (열 계산시에는 행에서 [0,0]칸을 계산해줬으므로 한 줄을 빼준다)
시간 복잡도는 N번의 연산만으로 가능하기때문에 Big-O는 O(N)이다.
'''

def Queen(n):
	if n==2:
		return 0
	
	row = n*(n**2-3*n+2)
	column = (n-1)*(n**2-4*n+4)
	
	return row+column+Queen(n-1)

n = int(input())

print(Queen(n))