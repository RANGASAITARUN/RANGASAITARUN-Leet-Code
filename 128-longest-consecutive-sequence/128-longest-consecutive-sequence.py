class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #c=1
        longest=0
        k=set(nums)
        # print(k)
        for i in nums:
            if i-1 not in k:
                length=0
                while length+i in k:
                    length=length+1
                longest=max(longest,length)
        return longest