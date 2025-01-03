#User function Template for python3

class Solution:
	def longestPrefixSuffix(self, s):
		n = len(s)
        lps = [0] * n
        i = 0
        j = 1
    
        while j < n:
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
    
        return lps[n - 1]


#{ 
 # Driver Code Starts
# Testing the function
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str_input = input()
        ob = Solution()
        print(ob.longestPrefixSuffix(str_input))
        print("~")
# } Driver Code Ends