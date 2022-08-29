def partition(arr, l, h):
    low, high = l, h
    if l < h:
        #设置第一个元素为枢纽
        pivot = arr[l]
        #从下一个数开始
        low = low + 1
        while low <= high:
            #如果左右两端都大于枢纽则互换左右两元素
            if arr[low] > pivot and arr[high] < pivot:
                arr[high], arr[low] = arr[low], arr[high]
            #如果只有左端<=枢纽则左端向右移一位
            elif arr[low] <= pivot:
                low = low + 1
            #如果只有右端>=枢纽则右端向左移一位
            elif arr[high] >= pivot:
                high = high - 1
            print(arr)
    #最后第一个元素和右端元素互换
    arr[l], arr[high] = arr[high], arr[l]
    #返回分区完成的位置位置
    return high


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        print(pi)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


array = [1, 7, 8, 9, 1, 2, 6, 4, 7, 2, 3, 9, 0]
quick_sort(array, 0, len(array)-1)
print(array)
