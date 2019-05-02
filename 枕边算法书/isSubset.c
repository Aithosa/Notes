int i;
int j;

int a[m] = {};
int b[n] = {};

for (i=0; i<m; i++)
{
	for(j=0; j<n; j++)
	{
		if (a[i] == b[j])
		{
			break;
		}

		if (j == (n-1))
		{
			return false;
		}
	}
}
return true;