# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here
        words = str.split(".")
        words = words[::-1]
        res = ""
        for i in words:
            res = res + (i + ".") 
        res1 = res[:-1]
        return res1
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends