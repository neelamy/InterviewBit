# Source : https://www.interviewbit.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) – Push element x onto stack.
# pop() – Removes the element on top of the stack.
# top() – Get the top element.
# getMin() – Retrieve the minimum element in the stack.

# Algo/DS : stack

# Complexity :O(n)

class MinStack:
    
    def __init__(self):
        self.stack =[]
        self.minimum = [] 
    
    # append x to stack and if x <= last min then add it to minimum
    # if x > last min then popping it wont affect the min so no need to store x  in minimum  
    def push(self, x):

    	if not self.stack:	

        	self.minimum.append(x)

        elif x <= self.minimum[-1] :

        		self.minimum.append(x)
    
        self.stack.append(x)
        
        
    
    # remove last element from stack. if removed item is last min then remove it too
    def pop(self):

        if self.stack:

            x = self.stack.pop()

            if x == self.minimum[-1]:

                self.minimum.pop()


    
    # get the last element from stack without removing it
    def top(self):

        return self.stack[-1] if self.stack else -1


    
    # return the last element of minimum as its the current min value
    def getMin(self):
        
        return self.minimum[-1] if self.minimum else -1
