//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    int isValid(string str) {
        stringstream ss(str);
        int count =0;
        while(ss.good())
        {
            string s;
            getline(ss,s,'.');
            count++;
            
            if(s.empty())
            {
                return 0;
            }
            
            if(s.length()>1 && s[0] == '0')
            {
                return false;
            }
            
            int k = stoi(s);
            if(0>k || k>255)
            {
               return 0;
            }
        }
        
       return count == 4 ? 1: 0;
        
    }
};

//{ Driver Code Starts.

int main() {
    // your code goes here
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        // if (s.size() == 3) {
        //     cout << "false" << endl;
        //     return 0;
        // }
        Solution ob;
        bool f = ob.isValid(s);
        if (f)
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }
    return 0;
}
// } Driver Code Ends