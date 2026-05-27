class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=0
            d[num]+=1
        sorted_nums= sorted(d,key=d.get,reverse= True)
        return sorted_nums[:k]


            
                
