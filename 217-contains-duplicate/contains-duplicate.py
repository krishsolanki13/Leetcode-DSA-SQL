class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num)
        return False
