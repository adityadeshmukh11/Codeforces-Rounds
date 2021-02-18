#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s1,s2;
	cin>>s1>>s2;
	int k=stoi(s1)+stoi(s2);
	string s3=to_string(k);
    string p,q,z;
    for(int i=0;i<s1.size();i++) if (s1[i]!='0')p+=s1[i];
    for(int i=0;i<s2.size();i++) if (s2[i]!='0')q+=s2[i]; 
    for(int i=0;i<s3.size();i++) if (s3[i]!='0')z+=s3[i]; 
    if(stoi(p)+stoi(q)==stoi(z)) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
    // cout<<p<<q<<endl;
 
    return 0;
}