//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    int isPrime(int N){
        if(N%N == 0 && sqrt(N)>1)
        {
            int tmp = sqrt(N);
            for(int i=2;i<=tmp;i++)
            {
                if(N%i == 0)
                {
                    return 0;
                }
            }
            return 1;
        }
            
        return 0;
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.isPrime(N) << endl;
    
cout << "~" << "\n";
}
    return 0; 
}
// } Driver Code Ends