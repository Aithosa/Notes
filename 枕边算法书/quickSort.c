quicksort(list)
{
	if (length(list) < 2)
	{
		return list;
	}

	x = pickPivot(list)
	list1 = {y in list where y < x}
	list2 = x
	list3 = {y in list where y > x}
	quicksort(list1)
	quicksort(list3)
	return concatenate(list1, list2, list3)
}