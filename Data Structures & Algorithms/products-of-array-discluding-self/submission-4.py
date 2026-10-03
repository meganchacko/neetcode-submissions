class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need to multiply all values except for arr[curr]
        # brute force is nested for loop, first loop iterates through array to get current index (what will be excluded from calculation), nested for loop will go through array again and multiply indices excluding arr[curr]

        # optimized : divide by number at index !!


        total_product = 1
        zero_counter = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_counter+= 1

            if zero_counter > 1:
                total_product = 0
            elif zero_counter == 1:
                if nums[i] != 0:
                    total_product = int(total_product * nums[i])
            else:
                total_product = int(total_product * nums[i])
            #print(f"total product: {total_product} for i = {i}")

        final_result = []
        for i in range(len(nums)):
            if zero_counter == 1:
                if nums[i] != 0:
                    final_result.append(0)
                else:
                    final_result.append(int(total_product))
            elif zero_counter > 1:
                final_result.append(0)
            else:
                final_result.append(int(total_product/nums[i]))
            #print(f"after appending: {final_result} for i = {i}")

        #final_result = [int(x) for x in final_result]
        return final_result


        