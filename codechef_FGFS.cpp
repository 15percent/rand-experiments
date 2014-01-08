#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

vector <long long int> s, f, p, diff;
vector< pair <long long int, long long int> > arr;

bool something(pair <long long int> i, pair <long long int> j)
{
return i.second < j.second;
}

int main()
{
int T, i, N, j;
long long int K, s1, f1, p1;
pair <long long int, long long int> temp;

scanf("%d", &T);

	for(i=0; i<T; i++)
	{
	scanf("%d %lld", &N, &K);

	arr.clear();
	for(j=0; j<N; j++)
	{
	scanf("%lld %lld %lld", &s1, &f1, &p1);
	temp.first = s1;
	temp.second = f1;
	arr.push_back(temp);
	}

sort(arr.begin(), arr.end(), something);

printf("%lld %lld\n", arr[0].first, arr[0].second);
	}


return 0;
}
