import queue
from typing import List, Any


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp: Any = queue.Queue()
        for i in range(len(arr)):
            if arr[i] == 0:
                temp.put(0)
            if not temp.empty():
                temp.put(arr[i])
                arr[i] = temp.get()
