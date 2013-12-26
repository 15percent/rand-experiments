#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector <int> arr;

int mobster(int N, int demand, int i)
{
int temp;
	while(i<N)
	{

	if( arr[i] < demand)
		{
		temp = mobster(N, demand-arr[i], i+1);
//		if(temp == 0) return 0;
		if(temp) {printf("%d ", arr[i]);return 1;}
		}

	else if( arr[i] == demand) {printf("%d ", arr[i]);return 1;}

	else if( arr[i] > demand) return 0;

	temp = mobster(N, demand, i+1);
	if(temp == 0) return 0;
	else return 1;
	}
}

int main()
{
int T, i, k, temp, N, demand;

scanf("%d", &T);

	for(k=0; k<T; k++)
	{
		scanf("%d %d", &N, &demand);

		arr.clear();
		for(i=0; i<N; i++)
		{
		scanf("%d", &temp);
		arr.push_back(temp);
		}

		sort(arr.begin(), arr.end());
		temp = mobster(N, demand, 0);
		if(temp == 0) printf("= No\n");
		else printf("= Yes\n");
	}


return 0;
}
