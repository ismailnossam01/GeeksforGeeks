# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        s_arr1 = sorted(arr1)
        s_arr2 = sorted(arr2)
        if(s_arr1) == (s_arr2):
            return True 
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(arr1, arr2):
            print("true")
        else:
            print("false")

# } Driver Code Ends