class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # creates an empty array for the results list
        RL = []
        # initialises the running totals value to zero
        RT = 0
        #iterates through the all elements in the nums list, where range starts from 0 and increments until it reaches the  maximum number of elements stored in the nums list
        for i in range(len(nums)):
            # Adds the value of the  whatever element [i] pulls from the nums list  to the running total
            RT += nums[i]
            # appends the value of the running total to the results list 
            RL.append(RT) 
        return RL