class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        number=[1]
        rows=[]
        while len(rows) <numRows:
            rows.append(number)
            temp=[1]
            for i in range(1,len(number)):
                temp.append(number[i - 1] + number[i])
            temp.append(1)
            number=temp
        return number                


                    
