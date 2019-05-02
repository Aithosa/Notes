int isSorted(int* array, int length)
{
	int index;
	for (array[index]=0; index<length-1; index++)
	{
		if (array[index] > array[index+1])
		{
			return 0;
		}
	}
	return 1;
}