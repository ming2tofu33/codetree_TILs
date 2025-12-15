n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
arr.insert(0,0)  # 0번 째 인덱스 삽입

def cum(i, j):
    global arr
    return sum(arr[i: j + 1])

for i, j in queries:
    print(cum(i, j))