#User function Template for python3

class Solution:
    def transform(self, s):
        # code here
        list1 = s.split(" ")
        output = []
        for data in list1:
            data = data[0].upper()+data[1::]
            output.append(data)
        
        return " ".join(output)
        
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends