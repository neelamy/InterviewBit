# Source : https://www.interviewbit.com/problems/power-of-2/
# Find if Given number is power of 2 or not. Dont change string to int

# Algo/DS : String

# Complexity :

class PowerOf2:
    
    # divide A by B
    def divide(self,A, B):
        
        rem = 0
        
        ans = ""
        
        for i in A:
            
            ans += str((ord(i) - ord('0') + (10 * rem)) / B)
            
            rem = (ord(i) - ord('0') + (10 * rem)) % B
            
        if ans [0] == '0' : ans = ans[1:]
            
        return ans    


    def power(self, A):
        

        reject = ['1','3','5','7','9','0']
               
        while A:

            n = len(A)

            if n == 1:
            
                return 1 if A not in reject else 0

            # return 0 if last digits are in reject
            if A[-1] in reject : return 0
            
            # divide A by 2
            A = self.divide(A, 2)
            
        return 0


def main():
	print PowerOf2().power("64") # 1


if __name__ == '__main__':
	main()