class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]
        for i in range(len(ratings)):
            if i == 0 or ratings[i-1] >= ratings[i]:
                new_candy = 1
            else:
                new_candy = candies[i-1] + 1
            candies[i] = new_candy
        for i in range(len(ratings)-1,-1,-1):
            if i == len(ratings)-1 or ratings[i+1] >= ratings[i]:
                new_candy = 1
            else:
                new_candy = candies[i+1] + 1
            candies[i] = max(candies[i], new_candy)
        
        return sum(candies)
