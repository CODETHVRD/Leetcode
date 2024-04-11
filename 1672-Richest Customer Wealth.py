class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Wealthiest = 0
        for customer_account in accounts:
            Wealthiest = max(sum(customer_account), Wealthiest)
        
        return Wealthiest  
