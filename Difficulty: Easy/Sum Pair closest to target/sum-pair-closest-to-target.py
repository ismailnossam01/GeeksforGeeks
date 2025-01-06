#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # Sort the array
        arr.sort()
        left = 0  # Start pointer at the beginning
        right = len(arr) - 1  # Start pointer at the end
        closest_sum = float('inf')  # Initialize to infinity
        closest_pair = []  # To store the closest pair
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            # Update the closest pair if a closer sum is found
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                closest_pair = [arr[left], arr[right]]
                
            # Adjust pointers based on the comparison of current_sum and target
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Exact match found
                return [arr[left], arr[right]]
        
        # Return the closest pair
        return closest_pair



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends