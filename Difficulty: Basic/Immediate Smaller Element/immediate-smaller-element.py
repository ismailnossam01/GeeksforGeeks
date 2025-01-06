#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def immediateSmaller(self, arr):
		# code here
		n = len(arr)
        for i in range(n - 1):  # Iterate until the second-to-last element
            if arr[i + 1] < arr[i]:  # Check if the right neighbor is smaller
                arr[i] = arr[i + 1]  # Update the current element to the smaller neighbor
            else:
                arr[i] = -1  # Update the current element to -1 if the neighbor is not smaller
        arr[-1] = -1  # The last element is always -1
        return arr
		

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.immediateSmaller(arr)
        for x in arr:
            print(x, end=" ")
        print()
        print("~")
        t -= 1


# } Driver Code Ends