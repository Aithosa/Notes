char* me;
void main(void)
{
	printf(me);
	putchar(13); // 回车
	putchar(34); // 双引号
	printf(me);
	putchar(34);
	putchar(';');
}

char* me = "void main(void)\
{\
	printf(me);\
	putchar(13);\
	putchar(34);\
	printf(me);\
	putchar(34);\
	putchar(';');\
}\
char* me = \
"