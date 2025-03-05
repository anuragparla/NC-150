class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        we know there is pile of bananas
        we know the total time koko has is h 
        we don't know what would be koko's speed to complete eating all bananas in the list of pile within the time frame 
        k is the speed at which koko eats 
        this can be anywhere between 1 and the max value in the pile 
        goal: to find the least possible k value from the given range 

        bf method:
        manually plugging in k value and checking the total time required to complete all the piles and see if its within h or more 
        this will lead to O(max(k)*len(pile))
        optimal soln:
        do a binary search on this k value range and then use it to determine if least k value can help koko finish all bananas in the given time span

        '''
        
        minVal = max(piles) 
        left, right = 1, max(piles)
        while left<=right:
            k = left + (right-left)//2
            totalTime = 0 
            for i in piles:
                totalTime += math.ceil(i/k)
            if totalTime<=h:
                minVal = min(minVal,k )
                right = k -1 
            else: 
                left = k +1 
        return minVal
        
            
            


        
