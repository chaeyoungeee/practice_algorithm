# 시간 복잡도: O(N+K)
# array의 모든 원소의 값이 0보다 크거나 같다고 가정
def count_sort(array):
    # 모든 범위를 포함하는 리스트의 값을 모두 0으로 초기화
    count = [0] * (max(array)+1)

    for x in range(len(array)):
        count[array[x]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for x in range(len(count)): # 리스트에 기록된 정렬 정보 확인
        for y in range(count[x]):
            print(x, end=' ') # 등장 횟수만큼 인덱스 출력

count_sort([7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2])