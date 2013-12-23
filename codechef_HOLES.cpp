#include <cstdio>
#include <map>
using namespace std;

map <char, int> hole_num;

void getHoles(char *S)
{
int count = 0;
	while(*S != '\0')
	{
	count += hole_num[*S];
	S++;
	}

printf("%d\n", count);
}

int main()
{
int T, i;
char S[40][100];

hole_num['A'] = hole_num['D'] = hole_num['O'] = hole_num['P'] = hole_num['Q'] = hole_num['R'] = 1;
hole_num['B'] = 2;

scanf("%d", &T);
getchar();

	for(i=0; i<T; i++)
	gets(S[i]);

	for(i=0; i<T; i++)
	getHoles(S[i]);

return 0;
}
