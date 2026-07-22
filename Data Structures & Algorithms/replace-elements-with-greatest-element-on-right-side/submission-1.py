class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0 
        for i in range(len(arr) - 1):
            max_subarray = max(arr[i+1:])
            arr[i] = max_subarray
        arr[len(arr) - 1] = -1
        return arr
        