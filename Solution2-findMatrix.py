class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        twoD = []
        twoD.append([])
        i = 0
        for n in nums:
            i = 0

            while n in twoD[i]:
                i = i + 1
                if i == len(twoD):
                    twoD.append([])

            twoD[i].append(n)

        return twoD



            
            

            



        
         