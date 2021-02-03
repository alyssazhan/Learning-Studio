class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[end]:#left side sorted
                if nums[start]<=target and target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:             #right side sorted
                if nums[mid]<target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1               
        return -1    