# Source : https://www.interviewbit.com/problems/zigzag-string/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
#And then read line by line: PAHNAPLSIIGYIR
#Write the code that will take a string and make this conversion given a number of rows

# Algo/DS : String

# Complexity :O(n)

class zigzag:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        
        if len(A) < B or B < 1 : return A
        
        # create B empty array
        w = [[] for i in range(B)]
        
        # if up is True then move upward i.e row = row -1
        # else move downward i.e. row = row + 1
        up = False
        
        row = 0
        
        for i in A:
            
            # if last row reached then move to second last row
            # and start moving upward
            if row == B: 
                
                row = B - 2
                
                up = True
            
            # if first row reached then move to second row
            # and start moving down    
            elif row < 0:
                
                row = 1
                
                up = False
            
            # change row according to up
            if up == False:
                
                w[row].append(i)
                
                row += 1
                
            else:
                
                w[row].append(i)
                
                row -= 1
       
       	# join each list to create string 
        w = map(lambda x : "".join(x), w) 

        # combine all strings together
        res = reduce(lambda x,y : x + y,w )
            
        return res



def main():
	print zigzag().convert("PAYPALISHIRING", 3) #PAHNAPLSIIGYIR


if __name__ == '__main__':
	main()