def merge_sort(numbers,low,high):
    if low < high:
        #mid = (low+high)//2
        mid = (low + (high - low ) // 2)
        merge_sort(numbers, low, mid)
        merge_sort(numbers,mid+1,high)
        merge(numbers,low,mid,high)

#while i < len(array1) and j < len(array2):

def merge(numbers, low, mid, high):
    #copy 1st half of array to array1
    array1 = numbers[low:mid+1]
    #copy 2nd half of array to array2
    array2 = numbers[mid+1:high+1]
    merged_array = []
    k = low
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i+=1
        else:
            numbers[k] = array2[j]
            j+=1
        k+=1
    numbers += array1[i:]
    numbers += array2[j:]
arr=[2,3,4,5,7,6,8]
merge_sort(arr,0,len(arr)-1)



