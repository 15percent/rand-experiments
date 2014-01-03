#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

vector <int> arr;
map <int, int> hashfunc;

void gethashed(long long int M)
{
long long int i;
int j, flag;

	for(i=2; i<=M; i++)
	{
	if(hashfunc[i]) continue;

	flag=0;
	for(j=2; j<=sqrt(i); j++)
	if(i%j==0) {flag++; break;}

	if(!flag)
		{
		for(j=2; i*j <= M; j++)
		hashfunc[i*j]++;
		}
	}
}

int main()
{
int T, i, j;
long long int N ,M, max = 0;

scanf("%d", &T);

	for(i=0; i<T; i++)
	{
	scanf("%lld %lld", &N, &M);
	arr.push_back(N);
	arr.push_back(M);
	if(M>max) max = M;
	}

	hashfunc[1]++;
	gethashed(max);

	for(i=0; i<arr.size(); i+=2)
	{
	for(j=arr[i]; j<=arr[i+1]; j++)
	if(!hashfunc[j]) printf("%d\n", j);
	printf("\n");
	}


return 0;
}
