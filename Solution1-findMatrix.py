class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        twoD = []
        mapFrecuency = dict()
        for n in nums:
            actualFrecuency = mapFrecuency.get(n,0)
            if actualFrecuency >= len(twoD):
                twoD.append([])
            twoD[actualFrecuency].append(n)
            mapFrecuency[n] = actualFrecuency + 1

        return twoD
