#include <bits/stdc++.h>
using namespace std;
int findS(int s) 
{ 
    int sum = 0; 
  
    // Start adding cubes of  
    // the numbers from 1 
    for (int n = 1; sum < s; n++)  
    { 
        sum += n * n * n; 
  
        // If sum becomes equal to s 
        // return n 
        if (sum == s) 
            return n; 
    } 
  
    return -1; 
} 

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        if(findS(n)!=0) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
        


 
    return 0;
}