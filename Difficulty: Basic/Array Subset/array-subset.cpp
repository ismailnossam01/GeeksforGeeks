//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

string isSubset(int a1[], int a2[], int n, int m) ;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        int a1[n], a2[m];

        for (int i = 0; i < n; i++) {
            cin >> a1[i];
        }
        for (int i = 0; i < m; i++) {
            cin >> a2[i];
        }

        cout << isSubset(a1, a2, n, m) << endl;
    
cout << "~" << "\n";
}
    return 0;
}

// } Driver Code Ends


string isSubset(int a1[], int a2[], int n, int m) {
    map<int,int> mpp;
    
    for(int i=0;i<n;i++)
    {
        mpp[a1[i]]++;
    }
    
    for(int j=0;j<m;j++)
    {
        if(mpp.find(a2[j]) != mpp.end() && mpp[a2[j]] != 0)
        {
            mpp[a2[j]]--;
        }
        else
        {
            return "No";
        }
    }
    return "Yes";
}