class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        position = {x: i for i, x in enumerate(arr2)}
        def custom_key(x):
            return (position[x],x) if x in position else (float(inf),x)
        arr1.sort(key=custom_key)

        return arr1
