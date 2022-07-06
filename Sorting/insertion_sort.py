# 시간 복잡도: O(n^)
# 선택 정렬과 시간 복잡도는 같으나 데이터가 거의 정렬되어 있는 경우 빠르게 동작함
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 i에서 1씩 감소
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

insertion_sort([1, 6, 77, 3, 2, 11, 27])
