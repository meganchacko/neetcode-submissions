from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # frequency map.... each key represents a value from the array nums[], and the value is the count

        # how to implement this? 
        # for i in len(nums)
        #   
        final_result = Counter(nums)
        
        max_num = 0
        print(final_result)
        for num,count in final_result.items():
            if count > (len(nums) // 2):
                return num


        return 0