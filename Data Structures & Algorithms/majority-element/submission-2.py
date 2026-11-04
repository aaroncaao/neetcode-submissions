class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        result, maxCount = 0, 0
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
            if map[i] > maxCount:
                result = i
                maxCount = map[i]
            print(map)
        
        return result