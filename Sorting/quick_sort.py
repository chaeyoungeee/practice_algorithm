# 시간 복잡도: 최악의 경우: O(n^2) / 평균적인 경우: O(NlogN)
def quick_sort(array, start, end):
    if start >= end: # 리스트의 원소의 개수가 1개인 경우 종료
        return
    pivot = start # pivot은 첫번째 원소
    left = start + 1
    right = end
    while left <= right: # pivot을 기준으로 분할
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[start] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 pivot을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)