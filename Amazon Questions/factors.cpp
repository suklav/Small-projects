#include <iostream>
using namespace std;




void Divisors(int n,int k)
{
	int count=0,flag=0;
	
	for (int i = 1; i <= n; i++)
		if (n % i == 0)
		{
		 	count++;
		 	if(count==k)
		 	{
				cout<<" "<<i;
				flag=1;
			}
		}
		if(!flag)
		  cout<<"-1";
}

/* Driver program to test above function */
int main()
{
	cout <<"The divisors of 100 are: \n";
	Divisors(100,30);
	return 0;
}

