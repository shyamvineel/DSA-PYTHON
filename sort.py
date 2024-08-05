class bubble_sort:
    def __init__(self):
        pass
    def _sort(self,arr):
        for step in range(0,len(arr)-1):
            for i in range(0,len(arr)-step-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1] , arr[i]


class insertion_sort:
    def __init__(self) -> None:
        pass
    
    def _sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while key< arr[j] and j>=0:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key

class selection_sort:
    def __init__(self) -> None:
        pass

    def _sort(self, arr):
        for i in range(0, len(arr)-1):
            min = i
            for j in range(i+1, len(arr)-1):
                if arr[j]< arr[min]:
                    min = j
            
            temp = arr[min]
            arr[min] = arr[i]
            arr[i] = temp

class merge_sort:
    def __init__(self):
        pass

    def _sort(self, arr):
        n = len(arr)
        self.divide(arr,0, n-1)
    
    def divide(self, arr, begin, end):
        if begin >= end:
            return
        
        mid = begin + (end-begin)//2
        self.divide(arr, begin, mid)
        self.divide(arr,mid+1, end)
        self.conquer(arr,begin,mid, end)

    def conquer(self, arr, begin, mid, end):

        sub_array_one = mid-begin+1
        sub_array_two = end-mid

        leftArray = [0]*sub_array_one
        rightArray = [0]*sub_array_two

        for i in range(sub_array_one):
            leftArray[i] = arr[i+begin]
        
        for j in range(sub_array_two):
            rightArray[j] = arr[mid+1+j]

        idx1 = 0
        idx2 = 0 
        mergeIndex = begin

        while idx1 < sub_array_one and idx2 < sub_array_two:
            if leftArray[idx1] <= rightArray[idx2]:
                arr[mergeIndex] = leftArray[idx1]
                idx1+=1
                mergeIndex+=1

            else:
                arr[mergeIndex] = rightArray[idx2]
                idx2+=1
                mergeIndex+=1

        while idx1 < sub_array_one:
            arr[mergeIndex] = leftArray[idx1]
            idx1+=1
            mergeIndex+=1

        while idx2 < sub_array_two:
            arr[mergeIndex] = rightArray[idx2]
            idx2+=1
            mergeIndex+=1

class quick_sort:
    def __init__(self) -> None:
        
        pass
    def _sort(self, arr):
        pass
        
if __name__ == "__main__":
    srt = bubble_sort()
    srt1 = selection_sort()
    srt2 = insertion_sort()
    srt3 = merge_sort()
    lst = [1,4,2,5,0]
    print(lst)
    srt3._sort(lst)
    #srt1._sort(lst)
    #srt._sort(lst)
    print(lst)