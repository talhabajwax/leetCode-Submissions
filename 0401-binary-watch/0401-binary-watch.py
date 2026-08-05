class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times=[]
        def recursion(turnedOn):
            for i in range(0,12):
                for j in range (0,60):
                    counti=0
                    countj=0
                    for k in bin(i):
                        if k=='1':
                            counti+=1
                    for l in bin(j):
                        if l=='1':
                            countj+=1
                    if counti + countj == turnedOn:
                        times.append(f"{i}:{j:02d}")
        recursion(turnedOn)
        return times
        