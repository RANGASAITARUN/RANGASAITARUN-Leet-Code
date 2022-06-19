class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        negative = False
        
        if x[0] == '-':
            negative = True
            x = x[1:]
        
        x = x[::-1]
        
        index = 0
        while x[index] == 0:
            index += 1
        
        result = int(x[index:])
        
        
        if negative:
            result = -1 * result
            
        if result > 2 ** 31 -1 or result < -2 ** 31:
            return 0
        
        else:
            return result
        