class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return True
            if nums[mid]<nums[end]:#right side sorted
                if nums[mid]<=target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
            elif nums[mid]>nums[end]: #left side sorted
                if nums[start]<=target and target<=nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                end-=1
                mid+=1
                    
            
        return False
                