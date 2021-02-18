#include <bits/stdc++.h>
using namespace std;
int isprime(int n,int m)
{
	int flag=0;
	for(int i=2;i<=m/2;i++)
	{
		if(m!=2 && m%i!=0)	continue;
		else return 0;
	}
	return 1;
}
int main()
{
	
		string s;
		int n,m,flag=0;
		cin>>n>>m;
		for(int i=n+1;i<=m;i++)
			{flag=isprime(n,i);
			 if(flag==1 && i==m) {flag=1;break;}
			 else 
			 	{ if(flag==1 && i!=m) {flag=0; break;}
			 	}
			}
		if(flag==1) s="YES";
		else s="NO";
		cout<<s<<endl;
		// cout<<min_<<endl;
	
 return 0;
}
