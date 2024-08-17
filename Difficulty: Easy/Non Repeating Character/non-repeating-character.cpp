//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    //Function to find the first non-repeating character in a string.
    char nonrepeatingCharacter(string S)
    {
        map<int,char> m1;
        map<char,int> m2;
        for(int i=0;i<S.size();i++){
            m1[i]=S[i];
        }
        for(int i=0;i<S.size();i++){
            m2[S[i]]++;
        }
        for(auto i:m1){
            char c=i.second;
            if (m2[c]==1){
                return c;
            }
        }
        return '$';
    }

};
//{ Driver Code Starts.

int main() {
	
	int T;
	cin >> T;
	
	while(T--)
	{
	
	    string S;
	    cin >> S;
	    Solution obj;
        char ans = obj.nonrepeatingCharacter(S);
        
        if(ans != '$')
	    cout << ans;
        else cout << "-1";
            
        cout << endl;
	    
	}
	
	return 0;
}

// } Driver Code Ends