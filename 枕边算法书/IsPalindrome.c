int isPalindrome(char* inputString);

void main(int argc, char** args)
{
	int result;

	if (arg < 2)
		{
			printf("Usage: Palindrome inputString \n");
			return;
		}
		result = isPalindrome(args[1]);

		if (result)
		{
			printf("it is palindrome \n");
		}
		else
		{
			printf("it is not palindrome \n");
		}
}

int isPalindrome(char* inputString)
{
	int index;
	int length = strlen(inputString);
	int testEndingIndex = length / 2 ;
	for (index=0; index<testEndingIndex; index++)
	{
		if (inputString[index] != inputString[length-1-index])
		{
			return 0;
		}
		return 1;
	}
}