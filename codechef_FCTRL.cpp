#include <cstdio>

int calc(int N)
{
int count = 0, i;

	if(N<10) return 0;

	for(i=10; i<N; i+=10)
	count++;

return count;
}

int main()
{
int T, N[100000], i, temp;

scanf("%d", &T);

	for(i=0; i<T; i++)
	{
	scanf("%d\n", &temp);
	N[i] = temp;
	printf("%d\n", N[i]);
	}

	for(i=0; i<T; i++)
	printf("%d\n", N[i]);



return 0;
}
