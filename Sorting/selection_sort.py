# 시간 복잡도: O(n^2)
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i # 가장 작은 원소의 인덱스
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i] # 스와프
    print(array)

selection_sort([1, 2, 4, 3, 0, 9, 8])