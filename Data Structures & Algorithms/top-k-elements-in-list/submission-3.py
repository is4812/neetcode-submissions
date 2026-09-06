class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C={}
        freq=[[] for i in range (len(nums)+1)]
        for i in nums:
            C[i]=1+C.get(i,0)
        for v,c in C.items():
            freq[c].append(v)
        res=[]
        for j in range(len(freq)-1,0,-1):
            for n in freq[j]:
                res.append(n)
                if len(res)==k:
                    return res