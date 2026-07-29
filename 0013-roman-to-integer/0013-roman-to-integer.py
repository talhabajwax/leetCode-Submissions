class Solution:
    def romanToInt(self, s: str) -> int:
        list1= ["I","V","X","L","C","D","M"]
        list2=[1,5,10,50,100,500,1000]
        output =[]
        total=0
        for i in s:
            roman = list1.index(i)
            number = list2[roman]
            output.append(number)
        for n in range(len(output)-1):
            if output[n] < output[n+1]:
                total = total-output[n]
            else:
                total = total+output[n]
        total = total+ output[-1]
        return total

        